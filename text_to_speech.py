import os
from time import sleep

import discord
import requests
from discord.utils import get

from dotenv import load_dotenv

from helper_functions import connect_to_voice

API_URL = 'http://api.voicerss.org/?key={0}&hl={1}&src={2}'
FILE_PATH = 'audio/TTS_result.mp3'

ENGLISH_LANG = 'en-us'
SLOVENIAN_LANG = 'sl-si'

text_example = 'Hello,%20world!'

load_dotenv()
API_KEY = os.getenv('TTS_API_KEY')


def save_text_to_speech(language, text):
    result = requests.get(API_URL.format(API_KEY, language, text))
    with open(FILE_PATH, 'wb') as f:
        f.write(result.content)


def get_text_to_speech(language, text):
    return requests.get(API_URL.format(API_KEY, language, text)).content


async def play_text_to_speech(ctx, bot, language, text):
    await connect_to_voice(ctx)
    guild = ctx.guild
    voice_client: discord.VoiceClient = get(bot.voice_clients, guild=guild)

    save_text_to_speech(language, text)

    while not os.path.exists(FILE_PATH):
        sleep(0.1)

    audio_source = discord.FFmpegPCMAudio(FILE_PATH)
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    while voice_client.is_playing():
        sleep(0.1)

    os.remove(FILE_PATH)

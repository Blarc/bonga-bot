import os
from time import sleep

import discord
import requests
from discord.utils import get

from dotenv import load_dotenv

from helper_functions import connect_to_voice

API_URL = 'http://api.voicerss.org/?key={0}&hl={1}&r={2}&src={3}'
FILE_PATH = 'audio/TTS_result.mp3'

ENGLISH_LANG = 'en-us'
SLOVENIAN_LANG = 'sl-si'

text_example = 'Hello,%20world!'

load_dotenv()
API_KEY = os.getenv('TTS_API_KEY')


def save_text_to_speech(language, speed, text):
    result = requests.get(API_URL.format(API_KEY, language, speed, text))
    with open(FILE_PATH, 'wb') as f:
        f.write(result.content)


def get_text_to_speech(language, text):
    return requests.get(API_URL.format(API_KEY, language, text)).content


def parse_input(args):
    language = SLOVENIAN_LANG
    speed = 0

    args = list(args)
    start_index = 0
    for i in range(len(args)):
        if args[i] == '-h' or args[i] == '-help':
            return "help", 0, 0
        elif args[i] == '-l':
            i += 1
            language = args[i]
            start_index += 2

        elif args[i] == '-s':
            i += 1
            speed = int(args[i])

            if speed < -10:
                speed = -10
            elif speed > 10:
                speed = 10

            start_index += 2

    return language, speed, start_index


async def play_text_to_speech(ctx, bot, language, speed, text):
    await connect_to_voice(ctx)
    guild = ctx.guild
    voice_client: discord.VoiceClient = get(bot.voice_clients, guild=guild)

    save_text_to_speech(language, speed, text)

    while not os.path.exists(FILE_PATH):
        sleep(0.1)

    audio_source = discord.FFmpegPCMAudio(FILE_PATH)
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

    while voice_client.is_playing():
        sleep(0.1)

    os.remove(FILE_PATH)


async def text_to_speech_command(ctx, bot, args):
    language, speed, start_index = parse_input(args)

    if language == 'help':
        return await ctx.send(
            'Available commands:\n'
            '`-h` prints this\n'
            '`-l` sets language (e.g. sl-si, hr-hr, fr-fr)\n'
            '`-s` sets speed (from -10 to 10)\n'
            '(sauce: http://www.voicerss.org/api/)'
        )

    await play_text_to_speech(ctx, bot, language, speed, '%20'.join(args[start_index:]))

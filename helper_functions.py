import discord
from discord.utils import get


def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


async def connect_to_voice(ctx):
    if not is_connected(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()


def play_audio(ctx, bot, path):
    guild = ctx.guild
    voice_client: discord.VoiceClient = get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(path)
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

import os

import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def vrata(ctx):
    if not is_connected(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    guild = ctx.guild
    voice_client: discord.VoiceClient = get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio('audio/vrata.mp3')
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)


@bot.command(pass_context=True)
async def juric(ctx):
    channel = ctx.message.channel
    await channel.send(file=discord.File('img/juric.jpg'))


@bot.command(pass_context=True)
async def zvok(ctx):
    channel = ctx.message.channel
    await channel.send(file=discord.File('audio/vrata.mp3'), content="-play file")


@bot.command(pass_context=True)
async def github(ctx):
    await ctx.send('https://github.com/Blarc/bonga-bot')


@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run(TOKEN)

import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from helper_functions import connect_to_voice, play_audio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def vrata(ctx):
    connect_to_voice(ctx)
    play_audio(ctx, bot, 'audio/vrata.mp3')


@bot.command(pass_context=True)
async def juric(ctx):
    channel = ctx.message.channel
    await channel.send(file=discord.File('img/juric.jpg'))


@bot.command(pass_context=True)
async def github(ctx):
    await ctx.send('https://github.com/Blarc/bonga-bot')


@bot.command(pass_context=True)
async def helpMe(ctx):
    await ctx.send('https://github.com/Blarc/bonga-bot/blob/main/README.md')


@bot.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run(TOKEN)

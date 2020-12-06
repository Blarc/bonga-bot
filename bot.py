import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from helper_functions import play_audio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(pass_context=True)
async def vrata(ctx):
    await play_audio(ctx, bot, 'audio/vrata.mp3')


@bot.command(pass_context=True)
async def mike(ctx):
    await play_audio(ctx, bot, 'audio/mike.mp3')


@bot.command(pass_context=True)
async def burgundy(ctx):
    await play_audio(ctx, bot, 'audio/burgundy.mp3')


@bot.command(pass_context=True)
async def shesaid(ctx):
    await play_audio(ctx, bot, 'audio/thatswhatshesaid.mp3')


@bot.command(pass_context=True)
async def caga(ctx):
    await play_audio(ctx, bot, 'audio/caga.mp3')


@bot.command(pass_context=True)
async def doma(ctx):
    await play_audio(ctx, bot, 'audio/doma.mp3')


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


@bot.command(pass_context=True)
async def test(ctx):
    await play_audio(ctx, bot, 'http://fridom.si/wp-content/uploads/2019/12/01-Habilitacija.mp3')


bot.run(TOKEN)

import os
import discord
import logging

from discord.ext.commands import bot
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
client = discord.Client()


class Main:
    def __init__(self):
        replacelater = 'replacelater'


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(token)

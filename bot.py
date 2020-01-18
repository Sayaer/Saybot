import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

extensions = [
    "Cogs.AdminCog.admin"
]

prefix = '!'

# client configuration


# setup the bot
bot = commands.Bot(command_prefix=prefix, help_command=None, description=None)

for extension in extensions:
    try:
        print(f'extension name: {extension}')
        bot.load_extension(extension)
        # logging info here
    except Exception as e:
        print(f'Could not load: {extension}')
        # logging info here

print('Checking commands')
for command in bot.commands:
    if command is not None:
        print(f'Command: {command}')
    else:
        print('Command not found')

# run the bot
print('Starting bot')
bot.run(token)


#!/urs/bin/env python3
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import unsync
import asyncio
import logging
import re
import sys
from typing import IO
import urllib.error
import urllib.parse
import aiofiles
import aiohttp
from aiohttp import ClientSession
from colorama import Fore

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()
# TODO: Identify if cogs are being loaded once or not
extensions = [
    "Cogs.AdminCog.admin"
    # "Cogs.DragaliaCog.dragalia" seems to be pulling the URL multiple times? Check this in a bit
]

# TODO: This currently logs to the console which is fine, but needs to be more customized and log to a file
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt=Fore.YELLOW + "%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True


# TODO: Create Saybot, still needs help command, case info,
bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('!'))


# change presence
# on guild join
# on guild leave
# guild metrics (in / members?)

# TODO: Make this a debug only level command
@commands.command(name='ShutdownBot')
@commands.has_permissions(manage_roles=True)
async def shutdown_bot(ctx):
    '''
    This is for debug purposes only and will need to be removed later
    :param ctx:
    :return:
    '''
    print(Fore.BLUE + 'Attempting a safe bot shutdown')
    await ctx.send('Attempting to safe shutdown the bot')
    sys.exit(1)

bot.add_command(shutdown_bot)

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print(Fore.RED + f'Failed to load extension: {extension}')

    bot.run(token)

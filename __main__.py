import discord
import logging
from discord.ext.commands import when_mentioned_or, Bot

# Setup the logger, check if this needs further implementation
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = Bot(
    command_prefix=when_mentioned_or('!')
)

# needs token bot.run()

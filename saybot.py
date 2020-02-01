#!/urs/bin/env python3
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from loguru import logger

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

extensions = [
    "Cogs.AdminCog.admin",
    "Cogs.DragaliaCog.dragalia"
]

logger.add("Logging/discord.log")


bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))


@client.event
async def on_ready():
    logger.info("Saybot is ready.")


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
            logger.info(f"Loaded extension: {extension}")
        except Exception as error:
            logger.warning(f"Failed to load extension {extension}")
    # bot.run is blocking, no code below this will run.
    bot.run(token)

import discord
from urllib.parse import urlparse
from loguru import logger
from discord.ext.commands import Bot
from discord.ext import commands

base_url = 'https://dragalialost.gamepedia.com/'


def setup(bot):
    bot.add_cog(Dragalia(bot))
    print('adding the Dragalia cog')

#TODO: This is intended to validate a URL so we don't send something broken or malicious, need to define further
def url_validator(url):
    try:
        result = urlparse(url)
        return logger.info(all([result.scheme, result.netloc, result.path]))
    except:
        return False


class Dragalia(commands.Cog):
    """
    This cog contains commands for Dragalia Lost.

    Currently using gamepedia as a reference.
    """

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name='chara', help='Look up character info')
    async def chara(self, ctx, character_name):
        test_url = base_url + character_name
        logger.info(f"Testing URL: {test_url}")
        if url_validator(test_url) is not False:
            await ctx.send(test_url)
            logger.info(f"Successfully sent {test_url}")
        else:
            await ctx.send("Could not find")
            logger.debug(f"Could not identify {test_url}")
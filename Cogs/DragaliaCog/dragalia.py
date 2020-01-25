import discord
import requests
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
from discord.ext import commands

URL = 'https://dragalialost.gamepedia.com/Adventurer_Grid'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# pull relevant dragalia pages once, store / iterate / work with them from there
# chara command needs to be modified so the links are dynamically created (may be better?)


def setup(bot):
    bot.add_cog(Dragalia(bot))
    print('adding the Dragalia cog')





class Dragalia(commands.Cog):
    """
    This cog contains commands for Dragalia Lost.
    """
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name='chara', help='Look up character info')
    async def chara(self, ctx, character_name):
        print('looking it up!')
        character_page = soup.find('a', text=character_name)
        if character_page is not None:
            print(f'Found {character_page}')
            print(f'Link: https://dragalialost.gamepedia.com/{character_name}')
            await ctx.send(f'Link: https://dragalialost.gamepedia.com/{character_name}')
        else:
            print('Not found')
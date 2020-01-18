import discord
import os

from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.ext import commands


def setup(bot):
    bot.add_cog(Admin(bot))
    print('adding the cog')


class Admin(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    # this works - test - not recommended, acts as a catch-all and must be parsed correctly
    # @commands.Cog.listener()
    # async def on_message(self, message):
    # print(message.content)

    # this works - test
    # @commands.command(name='hello')
    # async def hello(self, ctx):
    #   await ctx.send('Hey')

    @commands.command(name='create_channel', help='Creates a new channel.')
    @commands.has_permissions(manage_channels=True)
    async def create_channel(self, ctx, channel_name):
        """
        Anyone with manage_channels can create a channel, but not delete.
        :param ctx:
        :param channel_name:
        :return:
        """
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_text_channel(channel_name)

    @commands.command(name='delete_channel', help='Deletes a channel')
    @commands.has_permissions(administrator=True)
    async def delete_channel(self, ctx, channel_name):
        """
        Requires administrator permissions in order to delete, this action is permanent.
        :param ctx:
        :param channel_name:
        :return:
        """
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if existing_channel:
            print(f'Deleting channel: {channel_name}')
            await existing_channel.delete()

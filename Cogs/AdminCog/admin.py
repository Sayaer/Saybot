import asyncio

import discord
from discord import client
from discord.ext.commands import Bot
from discord.ext import commands
from loguru import logger


def setup(bot):
    bot.add_cog(Admin(bot))
    print('adding the Admin cog')


class Admin(commands.Cog):
    """
    This cog contains server-management and administration functionality,
    it needs to be further developed for multi-server support.
    """

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
    """
    Manual command entries.
    """

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

    @commands.command(name='add_role', help='Add a role to a user')
    @commands.has_permissions(manage_roles=True)
    async def add_role(self, ctx, role_name, user: discord.Member = None):
        """
        Add a role to a user, defaults to user invoking if member is None
        :param ctx:
        :param role_name:
        :param user:
        :return:
        """
        # Need to check if role exists, then see if user already has role, catch any exceptions, then add the role

    @commands.command(name='remove_role', help='Remove a role from a user')
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self, ctx, role_name, user: discord.Member = None):
        """
        Remove a role from a user, defaults to user invoking if member is None
        :param ctx:
        :param role_name:
        :param user:
        :return:
        """
        if user is None:
            user = ctx.author
        await self.remove_role(ctx, user, role_name)

    """
    Automated management tasks
    """
    # This will need to be tested, if functional may only need minor modification to meet basic needs
    @commands.Cog.listener
    async def on_member_join(self, ctx, member: discord.member):
        logger.add(f"Sleeping for 60 seconds then adding {member}to general chat")
        await asyncio.sleep(60)
        await ctx.add_role('visitor', member)
        await ctx.move_to('channel', member)



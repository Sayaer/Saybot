# Code for configuring a server from within discord
import os
import discord
import json

from discord.ext import commands

bot = commands.Bot(command_prefix='!')
client = discord.Client()


async def create_channel(ctx, channel_name =''):
    guild = ctx.guild
    await ctx.send(response)


import discord
from discord.ext.commands import Bot
from discord.ext import commands


def setup(bot):
    bot.add_cog(MysteryTrain(bot))
    print('adding the Admin cog')


class MysteryTrain(commands.Cog):
    """
    This cog contains runs a mini-game created for Ludum Dare 46, participants in the "Mystery Train"
    channel will be randomly assigned a role (investigator / murderer), investigators must use the clue prompts
    to figure out who the murderer is before the train reaches it's destination.
    """

    def __init__(self, bot: Bot):
        self.bot = bot


    passengers_and_items = {}

    def start_mystery_train(self):
        for member in discord.Guild.members:
            print(member)

    start_mystery_train()
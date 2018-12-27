# Author: David Neal
# Man I think I got everything setup right.
# Thanks Alex for the assistance! :D

import discord
import random
from random import choice
from enum import Enum
from discord.ext import commands


class DavidTest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Bot command that displays pong."""
        await ctx.send("Pong (b ᵔ▽ᵔ)b")


# Sets up the cog
def setup(bot):
    bot.add_cog(DavidTest(bot))

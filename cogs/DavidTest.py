# Author: David Neal
# Man I think I got everything setup right.
# Thanks Alex for the assistance! :D

import discord
import random
import time
from random import choice
from discord.ext import commands


class DavidTest:

    def __init__(self, bot):
        self.bot = bot
        self.loot = ["Sword", "Shield", "Gun", "Knife", "Textbook", "Umbrella"
                     "Bomb", "Robot", "Bow (no arrows)", "Bow (with arrows)",
                     "Pokeball", "Yugioh Card", "Shoes", "Shirt"]

    @commands.command()
    async def ping(self, ctx):
        """Bot command that displays pong."""
        await ctx.send("Pong (b ᵔ▽ᵔ)b")

    @commands.command()
    async def lootbox(self, ctx):
        """Returns a random object from chest after 5 seconds"""
        await ctx.send("Do Dododo! You got a " + choice(self.loot) + "!")


# Sets up the cog
def setup(bot):
    bot.add_cog(DavidTest(bot))

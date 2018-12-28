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
        """Returns a random object from chest."""
        rand = random.randint(1, 100000)
        if rand % 2 == 0:
            await ctx.send("Do Dododo! You got a " + choice(self.loot) + "!")
        else:
            money = str(random.randint(1, 1000000))
            await ctx.send("Cha-Ching! You got " + money + " g")

    @commands.command()
    async def bomb(self, ctx):
        """Makes a second bomb that counts down and
           detonates in 5 seconds"""
        # bomb & explode may not work as intended
        bomb = ":bomb:"
        explode = ":boom:"
        time.sleep(1)
        msg = await ctx.send("5.. ")
        timer = ['4', '3', '2', '1']
        for num in timer:
            time.sleep(1)
            edit_message(msg, msg + num + ".. ")
        await ctx.send(explode + "**B O O M**" + explode)


# Sets up the cog
def setup(bot):
    bot.add_cog(DavidTest(bot))

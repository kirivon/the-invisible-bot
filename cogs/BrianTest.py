# Comedic functions for uwu
# Author: Brian Wong

import discord
import random
from discord.ext import commands

class BrianTest:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async.def druggie(self, ctx, user: discord.Member):
        """Determines if user is a druggie"""
        value = random.randint(1, 100)
        if value % 2 == 0:
            await ctx.send(user.mention + "is a druggie")
        else
            await ctx.send(user.mention + "is not a druggie")
    
    
    
    
  
def setup(bot):
    bot.add_cog(BrianTest(bot))

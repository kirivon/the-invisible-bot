# Author: Brian Wong

import discord
import random
from discord.ext import commands

class BrianTest:

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command
    async.def rngesus(self, ctx, range):
        await ctx.send("Your number is " + random.randint(1, range))
    
    
    
    
  
def setup(bot):
    bot.add_cog(BrianTest(bot))

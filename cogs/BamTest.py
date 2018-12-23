# the invisible bot's emotions testing 2

# Author: An T. Vo

import discord  # import discord files?
import random   # to generate random numbers
from discord.ext import commands  # import commands from it?


# from redis import Redis, RedisError # maybe not

# =============================================================================
# Types and constants
# =============================================================================

# =============================================================================
# Base decision tree
# =============================================================================


class BamboozledTest:
    """ 0.2 Greeting accordance to 6 basic moods
        -   1 = MAD
        -   2 = SCARED
        -   3 = JOYFUL
        -   4 = POWERFUL
        -   5 = PEACEFUL
        -   6 = SAD


        Avoid using: N/A
        Arguments: N/A

        0.1. class Lamb will now prompt a user greeting for now
    """



    def __init__(self, 
                 bot):       # view: python3 is good, view: python is bad for sublime
        self.bot = bot

    greeting = [    "(╯°□°)╯︵ ┻━┻ GTFO",
                    "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ OH YEAH, MY DUDE!!!!!", 
                    "( ︶︿︶)_╭∩╮ ",
                    "| (• ◡•)| (❍ᴥ❍ʋ ) darn right, mah homie!",
                    "\"(Ó_Ò\")\"  oh....kay" 
                ]  


    async def on_message(self, message): 
        """Defines bot behavior when a message is posted to channel"""
        # Do something
        # ctx == self, technically, but self is used for instance (or abstract, in C++) class
        #                           where ctx is used for methods 
        
        if message.content.startswith("$bam")
            ctx = await self.bot.get_context(message)       # convert the result to bot class => ctx = bot.context
            await ctx.send(":pikachu: ")                         # so that we can use ctx.send



    @commands.command()
    async def ciao(self, ctx):
        """ 0.2. Greeting accordance to mood
            0.1. Saying "hello"
        """

        mood = random.randint(1,6)             # generate a random mood like 
                                               # my cousin's wife

        await ctx.send(self.greeting[mood-1])       # array max index is n -1 

# Sets up the cog
def setup(bot):
    bot.add_cog(BamboozledTest(bot))

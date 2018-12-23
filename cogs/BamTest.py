# the invisible bot's emotions

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


    @commands.command()
    async def ciao(self, ctx):
        """ 0.2. SGreeting accordance to mood
            0.1. Saying "hello"
        """

        mood = random.randint(1,6)             # generate a random mood like 
                                               # my cousin's wife
        greeting[2] = { "(╯°□°)╯︵ ┻━┻ GTFO",
                        "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",
                        "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ Hello, my dude!!!", 
                        "( ︶︿︶)_╭∩╮ 'sup",
                        "| (• ◡•)| (❍ᴥ❍ʋ) how are you doing, fam?"
                        "\"(Ó_Ò\")\"  hi......"}
        await ctx.send(greeting[mood-1])       # array max index is n -1 


# Sets up the cog
def setup(bot):
    bot.add_cog(BamboozledTest(bot))
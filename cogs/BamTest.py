# Author: Bamboozled

import discord  # import discord files?
from discord.ext import commands  # import commands from it?

# from redis import Redis, RedisError # maybe not

# =============================================================================
# Types and constants
# =============================================================================

# =============================================================================
# Base decision tree
# =============================================================================


class BamboozledTest:
    """ 0.1. class Lamb will now prompt a user greeting for now

        Avoid using: N/A
        Arguments: N/A
    """

    def __init__(self, 
                 bot):       # testing fam again
        self.bot = bot


    @commands.command()
    async def ciao(self, ctx):
        """ 0.2. Saying "hello" accordance to mood
            0.1. Saying "hello"
        """

        mood = 1             # will make it random
        greeting1[2] = {"Hello, my dude","(╯°□°)╯︵ ┻━┻ GTFO"}
        await ctx.send(greeting[mood])


# Sets up the cog
def setup(bot):
    bot.add_cog(BamboozledTest(bot))
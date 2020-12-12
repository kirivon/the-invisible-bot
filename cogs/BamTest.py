# The invisible bot's emotion.

# 0.3. Too messy. Will use double array next time. Still running 0.2.

# Author: James Emerson (An Vo)

import discord  # import discord files?
import random  # to generate random numbers
from discord.ext import commands  # import commands from it?
from random import choice
# from redis import Redis, RedisError # maybe not

# =============================================================================
# Base decision tree
# =============================================================================


class BamboozledTest(commands.Cog, name="Bam Cog"):
    """ 0.3 Expand the emotional spectrum (maybe will use union)
        -   1 - 10 = ANGER
            + 1. HURT
            + 2. THREATENED
            + 3. HATEFUL
            + 4. MAD
            + 5. AGGRESSIVE
            + 6. FRUSTRATED
            + 7. DISTANT
            + 8. CRITICAL        
        -   11 - 20 = FEAR
        -   21 - 30 = HAPPY         JOYFUL + POWERFUL + PEACEFUL
        -   31 - 40 = SURPRISE
        -   41 - 50 = DISGUST
        -   51 - 60 = SAD       


        Avoid using: N/A
        Arguments: N/A
        
        0.2 Greeting accordance to 6 basic moods
        -   1 = MAD
        -   2 = SCARED
        -   3 = JOYFUL
        -   4 = POWERFUL
        -   5 = PEACEFUL
        -   6 = SAD
        0.1. class Lamb will now prompt a user greeting for now        
    """

    def __init__(self,
                 bot):  # view:python3 is good, view: python is bad for sublime
        self.bot = bot

    # =============================================================================
    # Types and constants
    # =============================================================================

    """
    # 0.3.
    greeting = [
                    "(╯°□°)╯︵ ┻━┻ GTFO",                                                # 1
                    "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",                                                 # 2
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ OH YEAH, MY DUDE!!!!!",          # 3
                    "<:pikachu:512132390920126474> （・□・；）(」゜ロ゜)」 Σ(゜ロ゜;)"             # 4
                    " щ(゜ロ゜щ) ┌╏ º □ º ╏┐ NAN-TAH-NOH?（○□○）∴(O艸O★)", 
                    "uhhhhhhh -(≖д≖﹆)"                                ,                # 5
                    "\"( _ _ \")\" oh....kay"                                             # 6
                ]
    old greeting

    """
    # 0.2.
    uwu_greeting = [
                    "(╯°□°)╯︵ ┻━┻ WHO WOKE ME UP!!!???", 
                    "༼;´༎ຶ ۝ ༎ຶ༽ I'M NOT IGNORED~~~~~~~",
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ HOWDY, MY DUDE!!!!!",
                    "( ︶︿︶)_╭∩╮", 
                    "| (• ◡•)| (❍ᴥ❍ʋ ) what's up, mah homie!!??",
                    "\"( Ó_Ò \")\" h...hi......."
                ]

    uwu_mood = [
                    "(╯°□°)╯︵ ┻━┻ GTFO", 
                    "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ OH YEAH, MY DUDE!!!!!",
                    "( ︶︿︶)_╭∩╮", 
                    "| (• ◡•)| (❍ᴥ❍ʋ ) darn right, mah homie!",
                    "\"( Ó_Ò \")\" oh....kay"
                ]


    async def on_message(self, message):
        """ 0.1 giving out opnions accordance to moods

            outline: 1. if the content starts with :thonking
                        a. count if there is only 1 :thonking
                        b. if there is only, run the fortune of wheel to generate an opinion
        """

        activate_emoji = "<:thonking:455992031752355870> "
        if message.content.startswith(activate_emoji):
            ctx = await self.bot.get_context(message)
            mood = random.randint(1, 6)               # generate a random mood like
                                                      # my cousin's wife
            await ctx.send(self.uwu_mood[mood-1])     # we can use ctx.send

  
    @commands.command()
    async def ciao(self, ctx):
        """ 0.2. Greeting accordance to moods
            0.1. Saying "hello"
        """

        mood = random.randint(1, 6)
        await ctx.send(self.uwu_greeting[mood - 1])  # array max index is n -1

    @commands.command()
    async def sure(self, ctx, arg):
        """ # 0.1. Spongebod Bob mocking tone = randomly capitalize letters
        https://cdn.discordapp.com/attachments/505902755097870346/527064513120436235/image0.png

            Incoming: 0.2 replace some letters with different letters to increase mocking for example
            "good" = "gud"

            #Argument: arg
        """

        mocking = arg 
        
        mocking = mocking.lower()
        mocking_first_letter = mocking[0]
        mocking = mocking[1:]
        mocking = ''.join(choice((str.upper, str.lower))(index) for index in mocking)
        spongebob_meme = "https://cdn.discordapp.com/attachments/505902755097870346/527064513120436235/image0.png"
        await ctx.send("{} \n".format(spongebob_meme))
        await ctx.send("*{}{}*".format(mocking_first_letter, mocking))
        

# Sets up the cog
def setup(bot):
    bot.add_cog(BamboozledTest(bot))

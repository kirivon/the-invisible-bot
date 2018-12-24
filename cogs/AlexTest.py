from datetime import datetime
import discord
import random
from random import choice
from enum import Enum
from discord.ext import commands


class RPS(Enum):
    rock = "\N{MOYAI}"
    paper = "\N{PAGE FACING UP}"
    scissors = "\N{BLACK SCISSORS}"


class RPSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPS.rock
        elif argument == "paper":
            self.choice = RPS.paper
        elif argument == "scissors":
            self.choice = RPS.scissors
        else:
            raise


class AlexTest:

    def __init__(self, bot):
        self.bot = bot
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    @commands.command()
    async def latency(self, ctx):
        """Bot command that returns the latency in ms"""
        ping_ = self.bot.latency
        ping = round(ping_ * 1000)
        await ctx.send(f"Your ping is {ping}ms")

    @commands.command()
    async def punch(self, ctx, user: discord.Member):
        """Punches the user mentioned"""
        await ctx.send("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

    @commands.command()
    async def info(self, ctx, member: discord.Member):
        """Tells you some info about the member."""
        if member is ctx.message.author:
            pronoun = "Your"
        else:
            pronoun = "Their"
        name = f"{member.name}#{member.discriminator}"
        status = member.status
        joined = member.joined_at
        role = member.top_role
        msg = "{0} name is {1}. {0} status is {2}. They joined at {3}. {0} rank is {4}."
        await ctx.send(msg.format(pronoun, name, status, joined, role))

    @commands.command()
    async def roles(self, ctx, member: discord.Member):
        """Tells you a member's roles."""
        msg = " {0}'s highest role is {0.top_role}."
        await ctx.send(msg.format(member))

    @commands.command()
    async def mentionable(self, ctx, role: discord.Role):
        """checks if a role is mentionable and then mentions them"""
        if role.mentionable:
            msg = " {0} is able to mentioned.... mentioning now {0.mention}."
        else:
            msg = " {0} can not be mentioned :c. "
        await ctx.send(msg.format(role))

    @commands.command()
    async def benhammer(self, ctx, member: discord.Member):
        """A test ban function, does not actually ban just sends a message"""
        if member is ctx.message.author:
            await ctx.channel.send("You cannot ban yourself!")
            return
        # pylint: disable=W1401
        await ctx.send(
            f"{member} is beNNed  ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿ !"
        )

    @commands.command()
    async def avatar(self, ctx, user: discord.User):
        """Create URL of the persons avatar"""
        msg = " URL being created for user ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) " + user.avatar_url
        await ctx.send(msg)

    @commands.command()
    async def hugs(self, ctx, user: discord.Member, intensity: int = 1):
        """Because everyone likes hugs Up to 10 intensity levels."""
        name = user.display_name
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ{} ⊂(´・ω・｀⊂)".format(name)
        await ctx.send(msg)

    @commands.command()
    async def ed(self, ctx):
        """ed function returns a random quote"""
        edMessages = [
            'Alright _raises arms_ let\'s get started',
            'hah hah. I\'m just testing you guys',
            'I swear I\'m not making this up', 'So the exam is today, right?',
            'D\'aw you guys are no fun'
        ]
        msg = random.choice(edMessages)
        edmoji = " <:ed:505909298245926932> "
        await ctx.send(edmoji + msg + edmoji)

    @commands.command()
    async def botstatus(self, ctx, message=None):
        """Sets the bot's playing status, leaving empty will use default"""
        if message:
            game = discord.Game(message)
            await self.bot.change_presence(status=discord.Status.online, activity=game)
        else:
            game = discord.Game("with unicode faces")
            await self.bot.change_presence(status=discord.Status.online, activity=game)

    @commands.command()
    async def flips(self, ctx):
        """Flips a coin"""
        await ctx.send("*flips a coin and..." + choice(["HEADS!*", "TAILS!*"]))

    @commands.command()
    async def _8ball(self, ctx, question: str):
        """Ask 8 ball a question
        Questions must end with a question mark.
        Questions need double quotes "question here?"
        """
        if question.endswith("?") and question != "?":
            await ctx.send("`" + choice(self.ball) + "`")
        else:
            await ctx.send("That does not look like a question.")

    @commands.command()
    async def rps(self, ctx, user_choice: RPSParser):
        """Play Rock Paper Sciccors with uwuBot"""
        author = ctx.message.author
        player_choice = user_choice.choice
        uwu_choice = choice((RPS.rock, RPS.paper, RPS.scissors))
        situations = {
            (RPS.rock,     RPS.paper): False,
            (RPS.rock,     RPS.scissors): True,
            (RPS.paper,    RPS.rock): True,
            (RPS.paper,    RPS.scissors): False,
            (RPS.scissors, RPS.rock): False,
            (RPS.scissors, RPS.paper): True
        }
        if uwu_choice == player_choice:
            outcome = None  # Tie
        else:
            outcome = situations[(player_choice, uwu_choice)]

        if outcome is True:
            await ctx.send("{} You win {}!"
                           "".format(uwu_choice.value, author.mention))
        elif outcome is False:
            await ctx.send("{} You lose {}!"
                           "".format(uwu_choice.value, author.mention))
        else:
            await ctx.send("{} We're square {}!"
                           "".format(uwu_choice.value, author.mention))

    @info.error
    async def info_error(self, ctx, error):
        """If user DNE, prints error"""
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')


# Sets up the cog
def setup(bot):
    bot.add_cog(AlexTest(bot))

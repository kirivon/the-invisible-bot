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
    async def avatar(self, ctx, txt: str = None):
        """Creates big boi of users avatar"""
        if txt:
            try:
                user = ctx.message.mentions[0]
            except IndexError:
                user = ctx.guild.get_member_named(txt)
            if not user:
                user = ctx.guild.get_member(int(txt))
            if not user:
                user = self.bot.get_user(int(txt))
            if not user:
                await ctx.send('Could not find user.')
                return
        else:
            user = ctx.message.author
        if user.avatar_url_as(static_format='png')[54:].startswith('a_'):
            avi = user.avatar_url.rsplit("?", 1)[0]
        else:
            avi = user.avatar_url_as(static_format='png')
        em = discord.Embed(colour=0x708DD0)
        em.set_image(url=avi)
        await ctx.send(embed=em)

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
            await ctx.send("set bot status to..." + message)
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

    @commands.command()
    async def roleinfo(self, ctx, msg):
        """Get more info about a specific role.
        You need to quote roles with spaces.
        You may also specify a server to check the role for.
        """
        guild = ctx.message.guild
        guild_roles = ctx.message.guild.roles
        for role in guild_roles:
            if msg.lower() == role.name.lower() or msg == role.id:
                all_users = [str(x) for x in role.members]
                all_users.sort()
                all_users = ', '.join(all_users)
                em = discord.Embed(title='Role Info', color=role.color)
                em.add_field(name='Name', value=role.name)
                em.add_field(name='ID', value=role.id, inline=False)
                em.add_field(name='Users in this role', value=str(len(role.members)))
                em.add_field(name='Role color hex value', value=str(role.color))
                em.add_field(name='Role color RGB value', value=role.color.to_rgb())
                em.add_field(name='Mentionable', value=role.mentionable)
                if len(role.members) >= 1:
                    em.add_field(name='All users', value=all_users, inline=False)
                else:
                    em.add_field(name='All users',
                                 value='There are no users in this role!', inline=False)
                em.add_field(name='Created at', value=role.created_at.__format__('%x at %X'))
                em.set_thumbnail(
                    url='http://www.colorhexa.com/{}.png'.format(str(role.color).strip("#")))
                return await ctx.send(content=None, embed=em)
        await ctx.send(self.bot.bot_prefix + 'Could not find role ``{}``'.format(msg))

    @commands.command()
    async def userinfo(self, ctx, *, name=""):
        """Get user info. Ex: uwu.userinfo @user"""
        if ctx.invoked_subcommand is None:
            if name:
                try:
                    user = ctx.message.mentions[0]
                except IndexError:
                    user = ctx.guild.get_member_named(name)
                if not user:
                    user = ctx.guild.get_member(int(name))
                if not user:
                    user = self.bot.get_user(int(name))
                if not user:
                    await ctx.send('Could not find user.')
                    return
            else:
                user = ctx.message.author

            if user.avatar_url_as(static_format='png')[54:].startswith('a_'):
                avi = user.avatar_url.rsplit("?", 1)[0]
            else:
                avi = user.avatar_url_as(static_format='png')
            if isinstance(user, discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"
                voice_state = None if not user.voice else user.voice.channel

            em = discord.Embed(timestamp=ctx.message.created_at, colour=0x708DD0)
            em.add_field(name='User ID', value=user.id, inline=True)
            if isinstance(user, discord.Member):
                em.add_field(name='Nick', value=user.nick, inline=True)
                em.add_field(name='Status', value=user.status, inline=True)
                em.add_field(name='In Voice', value=voice_state, inline=True)
                em.add_field(name='Game', value=user.activity, inline=True)
                em.add_field(name='Highest Role', value=role, inline=True)
            em.add_field(name='Account Created',
                         value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
            if isinstance(user, discord.Member):
                em.add_field(name='Join Date', value=user.joined_at.__format__(
                    '%A, %d. %B %Y @ %H:%M:%S'))
            em.set_thumbnail(url=avi)
            em.set_author(name=user)
            await ctx.send(embed=em)

    @commands.command()
    async def myroles(self, ctx, *, user=None):
        """Check the roles of a user."""
        if not user:
            member = ctx.message.author
        else:
            try:
                member = ctx.message.mentions[0]
            except IndexError:
                member = ctx.guild.get_member_named(user)
            if not member:
                member = ctx.guild.get_member(int(user))
            if not member:
                member = self.bot.get_user(int(user))
        if not member:
            await ctx.send("That user couldn't be found. Please check your spelling and try again.")
        elif len(member.roles[1:]) >= 1:
            embed = discord.Embed(title="{}'s roles".format(member.name), description="\n".join(
                [x.name for x in member.roles[1:]]), colour=member.colour)
            await ctx.send("", embed=embed)
        else:
            await ctx.send("That user has no roles!")


# Sets up the cog
def setup(bot):
    bot.add_cog(AlexTest(bot))

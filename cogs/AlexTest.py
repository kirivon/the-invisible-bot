from datetime import datetime
import discord
from discord.ext import commands


class AlexTest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def latency(self, ctx):
        """Bot command that returns the latency in ms"""
        ping_ = self.bot.latency
        ping = round(ping_ * 1000)
        await ctx.send(f"Your ping is {ping}ms")

    @commands.command()
    async def punch(self,ctx, user: discord.Member):
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
    async def currtime(self, ctx):
        """Returns current 12 hour local time"""
        now = datetime.now()
        msg = now.strftime("Current time: %I:%M:%S %p")
        await ctx.send(msg)



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
        await ctx.send(f"{member} is beNNed  ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿ !")


    @commands.command()
    async def avatar(self, ctx, user: discord.User):
        """Create URL of the persons avatar"""
        msg = " URL being created for user ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) " + user.avatar_url
        await ctx.send(msg)


    @commands.command()
    async def hug(self, user: discord.Member, intensity: int = 1):
        """Because everyone likes hugs
        Up to 10 intensity levels."""
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
        await self.bot.say(msg)




    @info.error
    async def info_error(self, ctx, error):
        """If user DNE, prints error"""
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member')




# Sets up the cog
def setup(bot):
    bot.add_cog(AlexTest(bot))

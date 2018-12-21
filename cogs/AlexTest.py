import discord
from discord.ext import commands


class AlexTest:
    """Class is just basic bot and user interaction"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pong(self, ctx):
        """Bot command that returns the name of the invoker 
        and the name of the server"""
        author = ctx.author.name
        server = ctx.guild.name
        await ctx.send("Pong from {} from {}!".format(author, server))
    
    @commands.command()
    async def punch(self, ctx, user: discord.Member):
        """Punches the user mepntions"""
        await ctx.send("ONE PUNCH! And " + user.mention + "is out! ლ(ಠ益ಠლ)")
        
    @commands.command()
    async def info(self, ctx, member: discord.Member):
        """Tells you some info about the member."""
        fmt = " {0} joined on {0.joined_at} and has {1} roles."
        await ctx.send(fmt.format(member, len(member.roles)))

    @info.error
    async def info_error(self, ctx, error):
        """If User DNE, print error"""
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...')



def setup(bot):
    """Sets up the cog"""
    bot.add_cog(AlexTest(bot))

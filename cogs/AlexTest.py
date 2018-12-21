import discord
from discord.ext import commands


class AlexTest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pong(self, ctx):
        """Bot command that returns the name of the invoker 
        and the name of the server"""
        author = ctx.author.name
        server = ctx.guild.name
        await ctx.send("Pong from {} from {}!".format(author, server))


# Sets up the cog
def setup(bot):
    bot.add_cog(AlexTest(bot))

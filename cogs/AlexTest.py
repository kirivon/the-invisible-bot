import discord
from discord.ext import commands


class AlexTest:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def pong(self, ctx):
        #Returns ping when called
        author = ctx.message.author.name
        server = ctx.message.server.name
        await bot.say("Pong from {} from {}!".format(author,server))




# Sets up the cog
def setup(bot):
    bot.add_cog(AlexTest(bot))

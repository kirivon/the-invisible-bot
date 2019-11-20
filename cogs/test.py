"""
Testing of how many times a client greets the bot
"""

# Author: Lennard Huslik

import discord
from discord.ext import commands
from redis import Redis, RedisError


class Test(commands.Cog, name='Test Cog'):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        """Defines bot behavior when a message is posted to channel"""
        # Do something
        # ctx == self, technically, but self is used for instance (or abstract, in C++) class
        # 							where ctx is used for methods

    @commands.command()  # <---------- using a class for a method
    async def echo(self, ctx, arg):
        """Bot command that causes the bot to echo the argument it is passed"""
        await ctx.send(arg)

    @commands.command()
    async def hello(self, ctx):
        """Bot command that replies to the user with a greeting and the 
           number of times greeted """

        # Open connection to local redis server
        redis = Redis(
            host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

        try:  # Greets with greeting count if redis connection successful
            hello_count = redis.incr("hellos")
            ordinal = hello_count % 100
            suffix_list = {
                1: "st",
                2: "nd",
                3: "rd",
            }
            if ordinal > 10 and ordinal < 20:
                suffix = "th"
            else:
                ordinal = ordinal % 10

            try:
                suffix = suffix_list[ordinal]
            except:
                suffix = "th"

            name = ctx.author.nick
            if name is None:
                name = ctx.author.name

            msg = "Hello " + name + "! This is the " + \
                str(hello_count) + suffix + " time somone has greeted me!"
            await ctx.send(msg)
        except RedisError:  # Catch if redis connection fails
            await ctx.send("Hello!")
            print("Cannot connect to Redis!")


# Sets up the cog
def setup(bot):
    bot.add_cog(Test(bot))

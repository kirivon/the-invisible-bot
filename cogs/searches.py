import discord
import json
import urllib.request
from redis import Redis, RedisError
from discord.ext import commands


class Searches:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gi(self, ctx, *args):
        """Bot command that concocts the passed arguments together as a single
        string, then returns the first Google image result for that string"""

        # Load the keys from the config file stored in the base directory
        with open("config.json") as config_file:
            config = json.load(config_file)
            GOOGLEAPIKEY = config["GoogleAPIKey"]
            SEARCHENGINEID = config["SearchEngineID"]

        # Open connection to local redis server
        redis = Redis(
            host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

        # Creates a key for the user's name that expires in 1 hour
        if redis.get(ctx.author.name) == None:
            redis.set(ctx.author.name, 1, ex=3600)
        else:  # If the key exists, do not run the API search until it expires
            msg = "Please wait " + str(redis.ttl(
                ctx.author.name)) + " seconds before trying again."
            await ctx.send(msg)
            return

        searchstring = ""
        # Concocts the args into a single string
        if len(args) > 1:
            for x in args:
                searchstring += x
                # Adds a "+" between each arg
                if len(x) != len(args) - 1:
                    searchstring += "+"
        elif len(args) == 1:
            searchstring = args[0]
        else:
            return

        # Defines URL for Google Custom Search JSON API
        url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&num=1&q={}searchType=image".format(
            GOOGLEAPIKEY, SEARCHENGINEID, searchstring)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            res = response.read()  # Returns byte string encoded JSON response

        tmp = res.decode("utf-8")  # Decodes bytestring using utf-8 encoding
        json_res = json.loads(tmp)  # Loads decoded bytestring to JSON obj
        msg = json_res["items"][0]["link"]
        await ctx.send(msg)


# Sets up the cog
def setup(bot):
    bot.add_cog(Searches(bot))

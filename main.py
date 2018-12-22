import discord
import json
from discord.ext import commands

# Read the bot token and desired prefix from the config file
with open("config.json") as config_file:
    config = json.load(config_file)
    TOKEN = config["bot_token"]
    PREFIX = config["bot_prefix"]

# Discord.py class used to interact with Discord WebSocket and API
# Using the Bot subclass of discord.client and the specified prefix
bot = commands.Bot(command_prefix=PREFIX)

# Define extensions
extensions = ["cogs.test", "cogs.AlexTest", "cogs.searches", "cogs.BamTest", "cogs.BrianTest"]


@bot.event
async def on_ready():
    """Defines bot behavior when it is sucessfully loaded"""
    print("Logged in as {0.user}".format(bot))


# Loads the listed extensions
for extension in extensions:
    try:
        bot.load_extension(extension)
    except Exception as error:
        print("{} cannot be loaded. [{}]".format(extension, error))

# Blocking call that abstracts away the event loop initialization
# Must be the last function called!
bot.run(TOKEN)

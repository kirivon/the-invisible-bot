"""
Testing of how many times a client greets the bot
"""


# Author: Bamboozled

import discord  					# import discord files?
from discord.ext import commands	# import commands from it?
# from redis import Redis, RedisError # maybe not

# =============================================================================
# Types and constants
# =============================================================================

# =============================================================================
# Base decision tree
# =============================================================================

class BamboozledTest:
	""" 0.1. class Lamb will now prompt a user greeting for now

		Avoid using: N/A
		Arguments: N/A
	"""

	def __init__(self,
				 bot):			# testing
		self.bot = bot

	@commands.command()
	async def chao(self, ctx):
		""" 0.1. Saying "hello"
		"""
		greeting = "Hello, my dude"
		await ctx.send(greeting)

def setup(bot):
	""" not sure what this does, setting up?
	"""
	bot.add_cog(BamboozledTest(bot))
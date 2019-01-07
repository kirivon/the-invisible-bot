# Author: Nick Poole

import discord
import random
from random import choice
from discord.ext import commands
import json

class NickTest:

	def __init__(self,bot):
		self.bot = bot

	@commands.command()
	async def choose(self, ctx, *args):
		"""Chooses user-defined set of choices
			Usage: uwu.choose choose1;choose2;choose3;...;chooseN"""
		choices = args.join()
		myList = choices.split(";")
		msg = random.choice(myList)
		thonk = " <:thonking:455992031752355870> "
		await ctx.send(thonk + msg)



def setup(bot):
	bot.add_cog(NickTest(bot))
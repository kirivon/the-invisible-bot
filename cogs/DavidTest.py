# Author: David Neal
# Man I think I got everything setup right.
# Thanks Alex for the assistance! :D

import discord
import random
from random import choice
from enum import Enum
from discord.ext import commands


class davidTest:

    @commands.command()
    async def ping():
        await ctx.send("Pong (b ᵔ▽ᵔ)b")

import nextcord
from nextcord.ext import commands, tasks
from nextcord.ext.commands.core import check
from nextcord.utils import get
import asyncio


@bot.command()
async def test(ctx):
    await ctx.send("test")

token=""

bot.run(token)
import typing
import discord
from discord.ext import commands
import time
import asyncio

def setup(bot):
    bot.add_cog(Sleep(bot))
    print("sleep_cog loaded")

class Sleep(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sleep(self, ctx, *args):
        async with ctx.channel.typing():
            asyncio.sleep(5)
            return

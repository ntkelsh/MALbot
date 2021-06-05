import typing
import discord
from discord.ext import commands
import time

def setup(bot):
    bot.add_cog(Sleep(bot))

class Sleep(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sleep(self, ctx, *args):
        async with ctx.channel.typing():
            time.sleep(5)
            return

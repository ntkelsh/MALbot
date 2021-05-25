import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Ready(bot))


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('------------------------------------------')
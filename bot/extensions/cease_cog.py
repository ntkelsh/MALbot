import discord
from discord.ext import commands
from .utils import embed_this

def setup(bot):
    bot.add_cog(Cease(bot))

class Cease(commands.Cog):
    
    def __init__(self, bot, cease: bool):
        self.bot = bot
        self.cease = cease or False

    @commands.command(aliases = ['bully'])
    async def cease(self, ctx):
        self.cease = not self.cease

        if self.cease:
            await embed_this("Bullying activated")
        else:
            await embed_this("Bullying deactivated")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 298616928405028864:
            if self.cease:
                await message.delete()


    
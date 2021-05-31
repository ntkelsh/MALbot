import discord
from discord.ext import commands
from .utils import error
import random

def setup(bot):
    bot.add_cog(Embed(bot))
    print("embed_cog loaded.")

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed")
    async def embedthis(self, ctx, *args, member: discord.Member = None):
        if len(args) < 1:
            await self.embed_this("You need to enter a message.", ctx)
            return
        
        text = ' '.join(args)

        # the * unpacks a tuple into function arguments
        embed = discord.Embed(title=ctx.author.name, color=discord.Colour.from_rgb(*rgb_random()))
        embed.add_field(name= "Message", value = text)

        await ctx.channel.send(embed=embed)
        await ctx.message.delete()

def rgb_random() -> ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

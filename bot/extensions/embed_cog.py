import discord
from discord.ext import commands
from .utils import embed_this, get_footer, random_color

def setup(bot):
    bot.add_cog(Embed(bot))
    print("embed_cog loaded.")

class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="embed")
    async def embedthis(self, ctx, *args, member: discord.Member = None, title: str = None, footer: str = None):

        member = member or ctx.author
        footer = footer or get_footer()

        if len(args) < 1:
            await self.embed_this("You need to enter a message.", ctx)
            return
        
        text = ' '.join(args)

        embed = discord.Embed(color=random_color())
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        
        embed.add_field(name= "Message", value = text)

        embed.set_footer(text=footer)

        await ctx.channel.send(embed=embed)
        await ctx.message.delete()

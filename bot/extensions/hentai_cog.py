import discord
from discord.ext import commands
from hentai import Hentai, Utils, Format
from .utils import embed_this, get_footer, random_color

def setup(bot):
    bot.add_cog(Comic(bot))
    print("hentai_cog loaded.")

class Comic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(aliases=['hentai'])
    async def doujin(self, ctx, *args, member: discord.Member = None):

        member = member or ctx.author

        if not ctx.channel.is_nsfw():
            await embed_this("Not an NSFW channel", ctx)
            return

        id = None

        if len(args) > 1:
            await embed_this("Wrong number of arguments.", ctx)
            return

        if len(args) == 1:
            if not Hentai.exists(int(args[0])):
                await embed_this("Not a valid number.", ctx)
                return
            id = args[0]

        if len(args) < 1:
            id = Utils.get_random_id()

        d = Hentai(id)

        embed = discord.Embed(title=d.title(Format.Pretty), color=random_color())
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.add_field(name="Start Reading", value=d.url)
        embed.add_field(name="Favorites", value=f"❤ {d.num_favorites}")
        embed.set_thumbnail(url=d.thumbnail)
        embed.set_footer(text=get_footer())
        await ctx.channel.send(embed=embed)
        await ctx.message.delete()
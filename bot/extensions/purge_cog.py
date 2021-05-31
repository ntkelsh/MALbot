import discord
from discord.ext import commands
from .utils import embed_this

def setup(bot):
    bot.add_cog(Purge(bot))
    print("purge cog loaded.")

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role(590814399556616193, 748632414477353080, 810288123728756747, 765683894132932648)
    async def purge(self, ctx, *args, member: discord.Member = None):

        if len(args) > 1:
            await self.embed_this("Wrong number of arguments", ctx)
            return

        try:
            val = int(args[0])
            await ctx.channel.purge(limit=val)
            await self.embed_this("Purged " + val + " messages.", ctx, discord.Color.blue())
            return
        except ValueError:
            await self.embed_this("Not a valid number", ctx)
            return


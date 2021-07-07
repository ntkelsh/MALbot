import discord
from discord.ext import commands
from discord.ext.commands.core import has_any_role
from .utils import embed_this, random_color

def setup(bot):
    bot.add_cog(Cease(bot))
    print("cease_cog loaded")

class Cease(commands.Cog):
    
    def __init__(self, bot, m=False, c=False):
        self.bot = bot
        self.m = m
        self.c = c

    @has_any_role(274039052444106753, 274037079887970315) #god, solar
    @commands.command(aliases = ['bullym'])
    async def m(self, ctx):
        self.m = not self.m

        if self.m:
            await embed_this("Bullying activated", ctx)
        else:
            await embed_this("Bullying deactivated", ctx)

    def carson_bully_check(ctx):
        return ctx.message.author.id in [191044716521848833, 230181249212350465, 194892498504646666] #ian, andrew, nathan

    @commands.check(carson_bully_check)
    @commands.command(aliases = ['bullyc'])
    async def c(self, ctx):
        self.c = not self.c

        if self.c:
            await embed_this("Bullying activated", ctx)
        else:
            await embed_this("Bullying deactivated", ctx)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.id == 298616928405028864: #michael
            if self.m:
                await ctx.delete()
        elif ctx.author.id == 189228138654334976: #carson
            if self.c:
                content = ctx.content
                await ctx.delete()
                await embed_this(content, ctx, ctx.author, color=random_color())


    
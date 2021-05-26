import discord
from discord.ext import commands
import json
import os
import sys
from extensions.utils import write_json, read_json, restart

"""class Bot(discord.Client):

    async def purge(self, ctx, args=[]):
        if not await self.check_permissions(ctx):
            return
            
        if len(args) < 1 or len(args) > 1:
            await self.error("Wrong number of arguments.", ctx)
            return

        num_messages = int(args[0])
        await ctx.channel.purge(limit=num_messages)

    async def check_permissions(self, ctx):
        for r in ctx.author.roles:
            p = r.permissions
            if p.administrator:
                return True
        await self.error("Invalid permissions to use that command.", ctx)
        return False

    async def success(self, ctx):
        embed = discord.Embed(title="Success!", color = discord.Color.blue())
        await ctx.channel.send(embed=embed)

    async def help(self, ctx):
        embed = discord.Embed(title="Commands:", color = discord.Color.orange())
        embed.add_field(name="doujin", value = "doujin [number]")
        embed.add_field(name="purge", value = "purge [number]")
        embed.add_field(name="embed", value = "embed [message]")
        await ctx.channel.send(embed=embed)"""


if __name__ == '__main__':
    settings = read_json()
    prefix = settings['prefix']

    #print(settings['token'][1::2])
    #cannot put actual token on github

    bot = commands.Bot(command_prefix=prefix)

    extensions = [
        "extensions.hentai_cog",
        "extensions.shitpost_cog",
        "extensions.embed_cog",
        "extensions.ready_cog",
    ]

    for e in extensions:
        bot.load_extension(e)

    bot.run(settings['token'][1::2])
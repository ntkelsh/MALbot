import discord

async def error(self, message: str, ctx):
    embed = discord.Embed(title=message, color = discord.Color.red())
    await ctx.channel.send(embed=embed)
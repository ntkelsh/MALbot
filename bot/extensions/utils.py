import discord
import json

async def embed_this(self, message: str, ctx, color: discord.Color = discord.Color.red()):
    embed = discord.Embed(title=message, color = discord.Color.red())
    await ctx.channel.send(embed=embed)

def write_json():
    with open("settings.json", "w") as file:
        json.dump(settings, file)

def read_json() -> {}:
    with open("settings.json", "r") as file:
        return json.load(file)

def restart():
        os.execv(__file__, sys.argv)
import discord
import json

async def error(self, message: str, ctx):
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
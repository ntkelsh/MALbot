import discord
import json
import time
import random
import os
import sys
import json

async def embed_this(message: str, ctx, color: discord.Color = discord.Color.red()):
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

def get_time() -> str:
    return time.strftime("%I:%M %p")

def get_footer() -> str:
    return "Today at " + get_time()

def rgb_random() -> ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_color() -> discord.Colour:
    # the * unpacks a tuple into function arguments
    return discord.Colour.from_rgb(*rgb_random())
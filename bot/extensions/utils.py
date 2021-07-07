import discord
from discord.ext import commands
import json
from datetime import datetime
import pytz
import random
import os
import sys
import json
import typing
from pygicord import Paginator

async def embed_this(message: str, ctx, author: discord.Member = None,
        footer: str = None, color: discord.Color = discord.Color.red()):

    footer = footer or get_footer()
    embed = discord.Embed(title=message, color=color)
    if author:
        embed.set_author(name=author.name, icon_url=author.avatar_url)
    embed.set_footer(text=footer)
    await ctx.channel.send(embed=embed)

def write_json(settings):
    with open(".settings.json", "w") as file:
        json.dump(settings, file)

def read_json() -> {}:
    with open("settings.json", "r") as file:
        return json.load(file)

def restart():
        os.execv(__file__, sys.argv)

def get_time() -> str:
    pacific = pytz.timezone('US/Pacific')
    datetime_pacific = datetime.now(pacific)
    return datetime_pacific.strftime("%I:%M %p")

def get_footer() -> str:
    return "Today at " + get_time()

def rgb_random() -> typing.Tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_color() -> discord.Colour:
    # the * unpacks a tuple into function arguments
    return discord.Colour.from_rgb(*rgb_random())

async def multi_embed(embeds: typing.List[discord.Embed], ctx, timeout=90, compact=False, has_input=True):
    paginator = Paginator(pages=embeds, timeout=timeout, compact=compact, has_input=has_input)
    await paginator.start(ctx)
    await paginator.stop()
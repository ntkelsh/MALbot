import discord
from discord.ext import commands
from extensions.utils import write_json, read_json, restart

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
        "extensions.sleep_cog",
        "extensions.anilist.anilist_cog",
        "extensions.anilist.anime_cog",
        "extensions.anilist.manga_cog",
        "extensions.cease_cog"
        "extensions.ready_cog"
    ]

    for e in extensions:
        bot.load_extension(e)

    bot.run(settings['token'][1::2])

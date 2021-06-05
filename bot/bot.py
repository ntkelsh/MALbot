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
        #"extensions.purge_cog",
        "extensions.ready_cog",
    ]

    for e in extensions:
        bot.load_extension(e)

    bot.run(settings['token'][1::2])
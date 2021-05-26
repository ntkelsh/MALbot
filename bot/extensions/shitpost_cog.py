import discord
from discord.ext import commands
import json
from pyyoutube import Api
from .utils import read_json

youtube_api = read_json()['youtube'][1::2]
api = Api(api_key=youtube_api)

def setup(bot):
    bot.add_cog(Shitpost(bot))
    print("shitpost_cog loaded")

class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        words = message.content.split(" ")

        watch_str = "https://www.youtube.com/watch?v="
        embed_str = "https://www.youtube.com/embed/"

        url = None
        for w in words:
            if w.find(watch_str) != -1:
                index = w.index(watch_str)
                url = w[index:index + len(watch_str) + 11] # this is in case words letters are before or after the link
            elif w.find(embed_str) != -1:
                index = w.index(embed_str)
                url = w[index:index + len(embed_str) + 11]

        if url is not None:
            video_id = url.replace(watch_str, "").replace(embed_str, "")

            video = api.get_video_by_id(video_id=video_id)

            title = video.items[0].snippet.title
            
            if title.lower().find("shitpost") != -1 and title.lower().find("status") != -1:
                if not message.channel.is_nsfw():
                    print("shitpost status video found in wrong chat")
                    await message.delete()
                    return

            
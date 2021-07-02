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

        mobile_str = "https://m.youtube.com/watch?v="
        watch_str = "https://www.youtube.com/watch?v="
        embed_str = "https://www.youtube.com/embed/"
        short_str = "https://youtu.be/"
        y2u_str = "http://y2u.be/"

        link_prefixes = [
            "http://m.youtube.com/watch?v=",
            "https://m.youtube.com/watch?v=",
            "http://www.youtube.com/watch?v=",
            "https://www.youtube.com/watch?v=",
            "http://www.youtube.com/embed/",
            "https://www.youtube.com/embed/",
            "http://youtu.be/",
            "https://youtu.be/",
            "http://y2u.be/",
            "https://y2u.be/",
            "http://www.youtube.com/v/",
            "https://www.youtube.com/v/"
        ]

        url = None
        for w in words:
            for l in link_prefixes:
                if w.find(l) != -1:
                    index = w.index(l)
                    url = w[index + len(l): index + len(l) + 11]

            """if w.find(watch_str) != -1:
                index = w.index(watch_str)
                url = w[index:index + len(watch_str) + 11] # this is in case words letters are before or after the link
            
            elif w.find(embed_str) != -1:
                index = w.index(embed_str)
                url = w[index:index + len(embed_str) + 11]
            
            elif w.find(short_str) != -1:
                index = w.index(short_str)
                url = w[index:index + len(short_str) + 11]

            elif w.find(y2u_str) != -1:
                index = w.index(y2u_str)
                url = w[index:index + len(y2u_str) + 11]

            elif w.find(mobile_str) != -1:
                index = w.index(mobile_str)
                url = w[index:index + len(mobile_str) + 11]"""

        if url is not None:
            video_id = url

            video = api.get_video_by_id(video_id=video_id)

            title = video.items[0].snippet.title
            
            if title.lower().find("shitpost") != -1 and title.lower().find("status") != -1:
                if not message.channel.is_nsfw():
                    print("shitpost status video found in wrong chat")
                    await message.delete()
                    return

            
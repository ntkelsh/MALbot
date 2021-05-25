import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Shitpost(bot))
    print("shitpost_cog loaded")

class Shitpost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        #if the message contains any embeds
        if len(message.embeds) > 0:
            for e in message.embeds:
                if "shitpost" in e.title.lower():
                    if (message.channel.id != 845469773806305290):
                        print("shitpost status video found in wrong chat")
                        await message.delete()
                        return

            
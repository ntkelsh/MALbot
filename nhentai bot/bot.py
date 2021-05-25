import discord
from discord.ext import commands
import json
import os
import sys

"""class Bot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        print('------------------------------------------')

    async def on_message(self, message):

        if message.author == client.user:
            return

        if message.content.startswith(prefix):
            print('Parsing command')
            await self.parse_command(message.content, message)

    async def parse_command(self, message: str, ctx):
        message = message[len(prefix):]
        contents = message.split(' ')
        command = contents[0]
        args = contents[1:]

        if command == "doujin":
            if ctx.channel.is_nsfw():
                await self.doujin(ctx, args)
            else:
                await self.error("Not a NSFW channel", ctx)

        elif command == "embed":
            await self.embedthis(ctx, args)

        elif command == "purge":
            await self.purge(ctx, args)

        elif command == "help":
            await self.help(ctx)

        else:
            await self.error("Not a valid command. Please use **$help** for more info.", ctx)

        await ctx.delete()

    async def embedthis(self, ctx, args=[]):
        if len(args) < 1:
            await self.error("You need to enter a message.", ctx)
            return
        
        text = ' '.join(args)

        embed = discord.Embed(title=ctx.author.name, color=discord.Color.random())
        embed.add_field(name= "Message", value = text)

        await ctx.channel.send(embed=embed)

    async def purge(self, ctx, args=[]):
        if not await self.check_permissions(ctx):
            return
            
        if len(args) < 1 or len(args) > 1:
            await self.error("Wrong number of arguments.", ctx)
            return

        num_messages = int(args[0])
        await ctx.channel.purge(limit=num_messages)

    async def check_permissions(self, ctx):
        for r in ctx.author.roles:
            p = r.permissions
            if p.administrator:
                return True
        await self.error("Invalid permissions to use that command.", ctx)
        return False

    async def error(self, message: str, ctx):
        embed = discord.Embed(title=message, color = discord.Color.red())
        await ctx.channel.send(embed=embed)

    async def success(self, ctx):
        embed = discord.Embed(title="Success!", color = discord.Color.blue())
        await ctx.channel.send(embed=embed)

    async def help(self, ctx):
        embed = discord.Embed(title="Commands:", color = discord.Color.orange())
        embed.add_field(name="doujin", value = "doujin [number]")
        embed.add_field(name="purge", value = "purge [number]")
        embed.add_field(name="embed", value = "embed [message]")
        await ctx.channel.send(embed=embed)"""

def write_json():
    with open("settings.json", "w") as file:
        json.dump(settings, file)

def read_json() -> {}:
    with open("settings.json", "r") as file:
        return json.load(file)

def restart():
        os.execv(__file__, sys.argv)


if __name__ == '__main__':
    settings = read_json()
    prefix = settings['prefix']

    #print(settings['token'][1::2])
    #cannot put actual token on github

    bot = commands.Bot(command_prefix=prefix)

    extensions = [
        "extensions.hentai_cog"
    ]

    for e in extensions:
        bot.load_extension(e)

    bot.run(settings['token'][1::2])
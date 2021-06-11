import requests
import discord
from discord.ext import commands
from ..utils import embed_this, get_footer

def setup(bot):
    bot.add_cog(AniList(bot))
    print("anilist_cog loaded")

class AniList(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['user', 'list', 'anilist'])
    async def profile(self, ctx, arg):

            query = '''
            query ($name: String) {
                User(name: $name) {
                    avatar {
                        large
                        medium
                    }
                    favourites {
                        characters {
                            nodes {
                                name {
                                    first
                                    last
                                }
                                image {
                                    large
                                    medium
                                }
                            }
                        }
                    }
                    statistics {
                        anime {
                            count
                            meanScore
                            minutesWatched
                        }
                        manga {
                            count
                            meanScore
                            chaptersRead
                        }
                    }
                    siteUrl
                }
            }'''

            variables = {
                "name": arg
            }

            url = "https://graphql.anilist.co"

            response = requests.post(url, json={'query': query, 'variables': variables})

            json_data = response.json()
            print(json_data)

            if 'errors' in json_data:
                await embed_this(json_data['errors'][0]['message'], ctx)
            else:
                user = json_data['data']['User']

                siteUrl = user['siteUrl']
                avatar_url = user['avatar']['medium']
                stats = user['statistics']

                embed = discord.Embed(title=arg)
                embed.set_thumbnail(url=avatar_url)
                embed.add_field(name="Link", value=siteUrl, inline=False)
                embed.add_field(name="Days Watched", 
                    value="{:.1f}".format(stats['anime']['minutesWatched'] / 1440))
                embed.add_field(name="Chapters Read", value=stats['manga']['chaptersRead'])
                embed.set_footer(text=get_footer())

                await ctx.channel.send(embed=embed)

import requests
import discord
from discord.ext import commands
from .utils import embed_this, get_footer
import asyncio
import json
import re

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

    @commands.command(aliases=['show'])
    async def anime(self, ctx, *args, member: discord.Member = None):

        member = member or ctx.author

        name = ' '.join(args)

        query = '''
        query ($search: String) {
            Media (search: $search, type: ANIME) {
                title {
                    romaji
                    english
                    native
                }
                description (asHtml: false)
                siteUrl
                episodes
                season
                seasonYear
                genres
                tags {
                    name
                }
                averageScore
                popularity
                favourites
                externalLinks {
                    site
                    url
                }
                coverImage {
                    medium
                }
            }
        }
        '''

        variables = {
            "search": name
        }

        url = "https://graphql.anilist.co"

        response = requests.post(url, json={'query': query, 'variables': variables})

        json_data = response.json()

        if 'errors' in json_data:
            await embed_this(json_data['errors'][0]['message'], ctx)
        else:
            media = json_data['data']['Media']

            siteUrl = media['siteUrl']

            season = media['season'].lower().title() + " " + str(media['seasonYear'])

            description = media['description'].replace('<br>', '').replace('<br><br>', '')

            title = media['title']['romaji']
            if (media['title']['english'] is not None):
                title += " | " + media['title']['english']
        
            image = media['coverImage']['medium']

            embed = discord.Embed(title=title)
            embed.set_thumbnail(url=image)
            embed.add_field(name="Link", value=siteUrl)
            embed.add_field(name="Score", value=media['averageScore'])
            embed.add_field(name="Favorites", value=":heart: " + str(media['favourites']))
            embed.add_field(name='Description', value=description, inline=False)
            embed.set_footer(text=get_footer())

            await ctx.channel.send(embed=embed)

    @commands.command()
    async def manga(self, ctx, *args, member: discord.Member = None):

        member = member or ctx.author

        name = ' '.join(args)

        query = '''
        query ($search: String) {
            Media (search: $search, type: MANGA) {
                title {
                    romaji
                    english
                    native
                }
                description (asHtml: false)
                siteUrl
                genres
                tags {
                    name
                }
                averageScore
                popularity
                favourites
                externalLinks {
                    site
                    url
                }
                coverImage {
                    medium
                }
            }
        }
        '''

        variables = {
            "search": name
        }

        url = "https://graphql.anilist.co"

        response = requests.post(url, json={'query': query, 'variables': variables})

        json_data = response.json()

        if 'errors' in json_data:
            await embed_this(json_data['errors'][0]['message'], ctx)
        else:
            media = json_data['data']['Media']

            siteUrl = media['siteUrl']

            description = media['description'].replace('<br>', '').replace('<br><br>', '').replace('<i>', '').replace('</i>', '')

            title = media['title']['romaji']
            if (media['title']['english'] is not None):
                title += " | " + media['title']['english']

            image = media['coverImage']['medium']

            embed = discord.Embed(title=title)
            embed.set_thumbnail(url=image)
            embed.add_field(name="Link", value=siteUrl)
            embed.add_field(name="Score", value=media['averageScore'])
            embed.add_field(name="Favorites", value=":heart: " + str(media['favourites']))
            embed.add_field(name='Description', value=description, inline=False)
            embed.set_footer(text=get_footer())

            await ctx.channel.send(embed=embed)

        
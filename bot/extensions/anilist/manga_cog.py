from discord.ext import commands
import discord
import requests
from ..utils import embed_this, multi_embed
import typing

def setup(bot):
    bot.add_cog(Manga(bot))
    print("manga_cog added")

class Manga(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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
                characters {
                    nodes {
                        name {
                            first
                            middle
                            last
                            full
                        }
                        image {
                            medium
                        }
                        siteUrl
                        favourites
                        description
                    }
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
            await ctx.send(info(json_data))

# the first page containing name, description, score, favorites
def info(json_data) -> discord.Embed:
    media = json_data['data']['Media']

    siteUrl = media['siteUrl']

    description = media['description'].replace('<br>', '').replace('<br><br>', '').replace('<i>', '').replace('</i>', '')
    if len(description) > 500:
        description = description[0:500] + "..."

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

    return embed


# pages for the characters of the manga
def characters(json_data) -> typing.List[discord.Embed]:

    characters = json_data['data']['Media']['characters']['nodes']
    embeds = []

    for char in characters:
        name = char['name']['full']
        image = char['image']['medium']
        siteUrl = char['siteUrl']
        favorites = char['favourites']
        description = char['description']

        if len(description) > 500:
            description = description[0:500] + "..."

        e = discord.Embed(title=name)
        e.set_thumbnail(url=image)
        e.add_field(name="Link", value=siteUrl)
        e.add_field(name="Favorites", value=":heart: " + str(favorites))
        e.add_field(name="Description", value=description, inline=False)

        embeds.append(e)

    return embeds

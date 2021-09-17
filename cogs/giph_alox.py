#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#

import discord
import random
import string
import asyncio
import aiohttp
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException

#---------------------------------------------------------------------#
#SETTING THE COG 
#---------------------------------------------------------------------#

class giph_alox(commands.Cog):
    def __init__(self, client):
        self.client = client


#---------------------------------------------------------------------#
#KILL COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def kill(self, ctx, user: discord.Member):
        search = "kill"
        api_key = self.client.GiphyKey
        api_instance = giphy_client.DefaultApi()

        try:

            api_response = api_instance.gifs_search_get(api_key, search, limit=19, rating="g")
            list_gif = list(api_response.data)
            gif = random.choice(list_gif)

            embedKill = discord.Embed(title=f'{ctx.author.name} kills {user.name}', color = 3447003)
            embedKill.set_image(url=f'https://media.giphy.com/media/{gif.id}/giphy.gif')
            embedKill.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")

            await ctx.channel.send(embed=embedKill)
            
        except ApiException as e:
            print("Exception when calling API for Giphy")

#---------------------------------------------------------------------#
#BOOP COMMAND
#---------------------------------------------------------------------#
    @commands.command()
    async def boop(self, ctx, user: discord.Member):
        search = "boop"
        api_key = self.client.GiphyKey
        api_instance = giphy_client.DefaultApi()

        try:

            api_response = api_instance.gifs_search_get(api_key, search, limit=19, rating="g")
            list_gif = list(api_response.data)
            gif = random.choice(list_gif)

            embedBoop = discord.Embed(title=f'{ctx.author.name} boops {user.name}', color = 3447003)
            embedBoop.set_image(url=f'https://media.giphy.com/media/{gif.id}/giphy.gif')
            embedBoop.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")

            await ctx.channel.send(embed=embedBoop)
            
        except ApiException as e:
            print("Exception when calling API for Giphy")


#---------------------------------------------------------------------#
#GIF COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def gif(self, ctx, *, search ):
        api_key = self.client.GiphyKey
        api_instance = giphy_client.DefaultApi()

        try:
            api_response = api_instance.gifs_search_get(api_key, search, limit=19, rating="g")
            list_gif = list(api_response.data)
            gif = random.choice(list_gif)

            embedGif = discord.Embed(title=f'{search} in a gif', color = 3447003)
            embedGif.set_image(url=f'https://media.giphy.com/media/{gif.id}/giphy.gif')
            embedGif.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")

            await ctx.channel.send(embed=embedGif)

        except ApiException as e:
            print("Exception when calling API for Giphy")


#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#
def setup(client):
    client.add_cog(giph_alox(client))
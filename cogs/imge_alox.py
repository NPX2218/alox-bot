#---------------------------------------------------------------------#
#IMPORTING MODULES
#---------------------------------------------------------------------#

from math import e
from sys import platform
import discord
import sys
import random
import string
import asyncio
from discord import colour
from discord import embeds
from discord import widget
from discord.embeds import Embed, EmptyEmbed
from discord.ext import tasks, commands
import aiohttp
from discord.ext.commands import Bot, Cog
from discord_components import DiscordComponents, Button, ButtonStyle
from discord.ext.commands.converter import GameConverter
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class imge_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#TEXTIMG COMMAND
#---------------------------------------------------------------------#
    
    @commands.command()
    async def textimg(self, ctx, *, text = "Nothing Entered"):
        img = Image.open("cogs/Images_PILLOW/Solid_white.jpg")

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 100)
        w, h = font.getsize(text)

        draw.text(((2048-w)/2, (2048-h)/2), text, (0,0,0), font=font)

        img.save("cogs/Images_PILLOW/Saved_Images_PILLOW/Solid_white_writing.jpg")
        writing_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/Solid_white_writing.jpg", filename="Solid_white_writing.jpg")
        embedTextimg = discord.Embed(title=f'{text}, in an image', color = 3447003)
        embedTextimg.set_image(url="attachment://Solid_white_writing.jpg")
        embedTextimg.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=writing_file, embed=embedTextimg)


#---------------------------------------------------------------------#
#WANTED COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def wanted(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        wanted = Image.open("cogs/Images_PILLOW/wanted.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((300, 300))
        wanted.paste(pfp, (83, 221))
        wanted.save("cogs/Images_PILLOW/Saved_Images_PILLOW/wanted_profile.jpg")
        
        wanted_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/wanted_profile.jpg", filename="wanted_profile.jpg")
        embedWanted = discord.Embed(title=f'{user.name}, is wanted!', color = 3447003)
        embedWanted.set_image(url="attachment://wanted_profile.jpg")
        embedWanted.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=wanted_file, embed=embedWanted)

#---------------------------------------------------------------------#
#HIDE-FACE COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def hideface(self, ctx, user : discord.Member):
        if user == None:
            user = ctx.author
        
        hidetheface = Image.open("cogs/Images_PILLOW/hidetheface.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((252, 219))
        hidetheface.paste(pfp, (78, 598))
        hidetheface.save("cogs/Images_PILLOW/Saved_Images_PILLOW/hidetheface_profile.jpg")

        hide_face_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/hidetheface_profile.jpg", filename="hidetheface_profile.jpg")
        embedHideFace = discord.Embed(title=f'{user.name}, get masked!', color = 3447003)
        embedHideFace.set_image(url="attachment://hidetheface_profile.jpg")
        embedHideFace.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=hide_face_file, embed=embedHideFace)
#---------------------------------------------------------------------#
#HIDE FACE COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def burn(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        
        hidetheface = Image.open("cogs/Images_PILLOW/fireburn.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((215, 215))
        hidetheface.paste(pfp, (57, 127))
        hidetheface.save("cogs/Images_PILLOW/Saved_Images_PILLOW/burntheface_profile.jpg")

        burn_face_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/burntheface_profile.jpg", filename="burntheface_profile.jpg")
        embedBurnFace = discord.Embed(title=f'{user.name}, get burned!', color = 3447003)
        embedBurnFace.set_image(url="attachment://burntheface_profile.jpg")
        embedBurnFace.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=burn_face_file, embed=embedBurnFace)
#---------------------------------------------------------------------#
#SLAP COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def slap(self, ctx, user1 : discord.Member):
        user = ctx.author
        
        slaptheface = Image.open("cogs/Images_PILLOW/slap.jpg")
        asset = user.avatar_url_as(size= 128)
        asset1 = user1.avatar_url_as(size= 128)

        data = BytesIO(await asset.read())
        data1 = BytesIO(await asset1.read())

        pfp = Image.open(data)
        pfp1 = Image.open(data1)
        pfp = pfp.resize((355, 355))
        pfp1 = pfp1.resize((355, 355))

        slaptheface.paste(pfp1, (795, 312))
        slaptheface.paste(pfp, (446, 30))

        slaptheface.save("cogs/Images_PILLOW/Saved_Images_PILLOW/slapface_profile.jpg")

        burn_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/slapface_profile.jpg", filename="slapface_profile.jpg")
        embedBurn = discord.Embed(title=f'{user1.name}, get slapped!', color = 3447003)
        embedBurn.set_image(url="attachment://slapface_profile.jpg")
        embedBurn.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=burn_file, embed=embedBurn)

#---------------------------------------------------------------------#
#CRY COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def cry(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        
        cry_water_face = Image.open("cogs/Images_PILLOW/cry_water.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((235, 235))
        cry_water_face.paste(pfp, (351, 17))
        cry_water_face.save("cogs/Images_PILLOW/Saved_Images_PILLOW/crywaterface_profile.jpg")

        cry_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/crywaterface_profile.jpg", filename="crywaterface_profile.jpg")
        embedCry = discord.Embed(title=f'{user.name}, thanks for being a water source!', color = 3447003)
        embedCry.set_image(url="attachment://crywaterface_profile.jpg")
        embedCry.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=cry_file, embed=embedCry)

#---------------------------------------------------------------------#
#UGLY COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def ugly(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        
        ugly_face = Image.open("cogs/Images_PILLOW/ugly_close.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((109, 109))
        ugly_face.paste(pfp, (33, 28)) 
        ugly_face.paste(pfp, (307, 212))
        ugly_face.save("cogs/Images_PILLOW/Saved_Images_PILLOW/ugly_face_profile.jpg")

        ugly_file=discord.File("cogs/Images_PILLOW/Saved_Images_PILLOW/ugly_face_profile.jpg", filename="ugly_face_profile.jpg")
        embedUgly = discord.Embed(title=f'{user.name}, wow you are not good looking!', color = 3447003)
        embedUgly.set_image(url="attachment://ugly_face_profile.jpg")
        embedUgly.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(file=ugly_file, embed=embedUgly)
#---------------------------------------------------------------------#
#AVATAR COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, user : discord.Member=None): # set the member object to None
        if not user: # if member is no mentioned
            user = ctx.message.author # set member as the author

        avatar_url_png = user.avatar_url_as(format="png")
        avatar_url_jpg = user.avatar_url_as(format="jpg")
        avatar_url_webp = user.avatar_url_as(format="webp")

        buttons_avatar = [
                        Button(style=ButtonStyle.URL, label = "[JPG]",url=f'{avatar_url_jpg}'),
                        Button(style=ButtonStyle.URL, label = "[PNG]",url=f'{avatar_url_png}'),
                        Button(style=ButtonStyle.URL, label = "[WEBP]",url=f'{avatar_url_webp}'),
                    ]
        embedAvatar = discord.Embed(title = f'{user.name}\'s avatar', colour=3447003)
        embedAvatar.set_image(url = user.avatar_url)
        embedAvatar.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        await ctx.send(embed=embedAvatar, components = [buttons_avatar], timeout=15)


#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#
def setup(client):
    client.add_cog(imge_alox(client))
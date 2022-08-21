#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#

from math import e
from re import L
from sys import platform
import discord
import sys
import enchant
import random
import string
import asyncio
from discord import colour
from discord import embeds
from discord import widget
from discord.embeds import Embed, EmptyEmbed
from discord.ext import tasks, commands
import aiohttp
import datetime, time
from discord.ext.commands import Bot, Cog, has_permissions, GameConverter, Converter
#from discord.ext.commands.core import has_permissions
from discord_components import DiscordComponents, Button, ButtonStyle, component
#from discord.ext.commands.converter import GameConverter
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

import giphy_client
from giphy_client.rest import ApiException

from math import sqrt, pi

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class mode_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#BAN COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.User, *, reason = None):
        if reason == None:
            reason = "No Reason Provided"
        await ctx.guild.ban(user = member, reason=reason)
        embedBan = discord.Embed(title = f"Banned **{member.name}**", description=f"Reason: {reason}", color = 3447003)
        embedBan.add_field(name=f"{member.name} has been punished.", value=f"{ctx.author} has used the **ban hammer.**\nUse the command al.unban to unban the user.")
        embedBan.set_thumbnail(url="https://images.discordapp.net/avatars/653176856035721270/371bdaa0d44478e76b23929559750651.png?size=512  ")
        embedBan.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        await ctx.channel.send(embed=embedBan)

#---------------------------------------------------------------------#
#KICK COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.User, *, reason = None):
        if reason == None:
            reason = "No Reason Provided"
        await ctx.guild.kick(user = member, reason=reason)
        embedBan = discord.Embed(title = f"Kicked **{member.name}**", description=f"Reason: {reason}", color = 3447003)
        await ctx.channel.send(embed=embedBan)

#---------------------------------------------------------------------#
#UNBAN COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return


#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(mode_alox(client))

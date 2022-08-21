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

class cogs_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

    def is_permissions_allowed():
        async def predicate(ctx):
            if ctx.author.id == 581028448357842945:
                return 1
            else:
                print(f"{ctx.author} tried to use {ctx.command} but doesn't have permission!")
                return 0
        return commands.check(predicate)

#---------------------------------------------------------------------#
#RELOADING COGS COMMAND, NEED MY PERMISIONS TO USE
#---------------------------------------------------------------------#

    @is_permissions_allowed()
    @commands.command(hidden=True)
    async def reload(self, ctx, cog):
        cog = cog.lower()
        try:
            self.client.reload_extension(f"cogs.{cog}_alox")
            embedCogReload = discord.Embed(title="Reloaded Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Reloaded```", inline=False)
            await ctx.send(embed=embedCogReload)
        except Exception:
            embedCogReload = discord.Embed(title="Failed To Reload Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Reload``` ", inline=False)
            await ctx.send(embed=embedCogReload)

#---------------------------------------------------------------------#
#LOAD COGS COMMAND, NEED MY PERMISIONS TO USE
#---------------------------------------------------------------------#

    @is_permissions_allowed()
    @commands.command(hidden=True)
    async def load(self, ctx, cog):
        cog = cog.lower()
        try:
            self.client.load_extension(f"cogs.{cog}_alox")
            embedCogReload = discord.Embed(title="Loaded Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Loaded```", inline=False)
            await ctx.send(embed=embedCogReload)
        except Exception:
            embedCogReload = discord.Embed(title="Failed To Load Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Load``` ", inline=False)
            await ctx.send(embed=embedCogReload)

#---------------------------------------------------------------------#
#UNLOADING COGS COMMAND, NEED MY PERMISIONS TO USE
#---------------------------------------------------------------------#

    @is_permissions_allowed()
    @commands.command(hidden=True)
    async def unload(self, ctx, cog):
        cog = cog.lower()
        try:
            self.client.unload_extension(f"cogs.{cog}_alox")
            embedCogReload = discord.Embed(title="Unloaded Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Unloaded```", inline=False)
            await ctx.send(embed=embedCogReload)
        except Exception:
            embedCogReload = discord.Embed(title="Failed To Unload Cog", color = 3447003)
            embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Unload``` ", inline=False)
            await ctx.send(embed=embedCogReload)

#---------------------------------------------------------------------#
#COG COMMAND, NEED MY PERMISIONS TO USE
#---------------------------------------------------------------------#

    @is_permissions_allowed()
    @commands.command(hidden=True)
    async def cog(self, ctx, cog):
        cog = cog.lower()
        list = ""
        counter = -1
        ListOfCogs = self.client.cogs # this is a dictionary!
        for NameOfCog,TheClassOfCog in ListOfCogs.items(): # we can loop trough it!
            counter += 1
            if counter % 3 == 0:
                list += "\n"
                list += f"{NameOfCog}.py, "
            else:
	            list += f"{NameOfCog}.py, "
        embedCogMain = discord.Embed(title=f"Cog Lounge : __{cog}_alox.py__", description="Choose one from below", color = 3447003)
        embedCogMain.add_field(name="Cogs: ", value= f"""```{list}```""")
        embedCogMain.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Cog_font_awesome.svg/1200px-Cog_font_awesome.svg.png")

        embedNotHere = discord.Embed(title=f"You didnt choose an option!", color = 3447003)
        embedNotHere.add_field(name=f"{ctx.author.name}!", value = f"""```{ctx.author.name} did not react or Exited!\nUse the command again to gain access to the Lounge again!```""", inline=False)
        embedNotHere.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")

        buttons = [
                Button(style=ButtonStyle.green, label = f"Reload 🔃", id = "_reload"),
                Button(style=ButtonStyle.blue, label = f"Load 🔒", id = "_load"),
                Button(style=ButtonStyle.red, label = f"Unload 🔓", id = "_unload"),
                Button(style=ButtonStyle.grey, label = f"{cog}_alox.py ⚙",disabled=True),
                Button(style=ButtonStyle.red, label = f"Exit 🚪", id  = "_exit")
        ]

        msg = await ctx.send(embed=embedCogMain, components = [buttons])
        button_ids = ["_reload", "_unload", "_load", "_exit"]

        def disable_buttons():
            for t in buttons:
                t.style = ButtonStyle.grey
                t.disabled = True

        while True:
            try:
                res = await self.client.wait_for("button_click", check=lambda i: i.component.id in button_ids and i.author.id == 581028448357842945 and i.message.id == msg.id, timeout=20)
                global user_action
                if res.component.label == 'Reload 🔃':
                    user_action = "reload"
                    break
                elif res.component.label == 'Unload 🔓':
                    user_action = "unload"
                    break
                
                elif res.component.label == 'Load 🔒':
                    user_action = "load"
                    break
                
                elif res.component.label == 'Exit 🚪':
                    disable_buttons()
                    await res.respond(type = 7, embed = embedNotHere, components = [buttons])
                    user_action = None
                    break

            except asyncio.TimeoutError:
                disable_buttons()
                #await res.respond(embed=embedNotHere, components = [buttons], type = 7)
                await msg.edit(embed=embedNotHere, components = [buttons])
                user_action = None
                break
        
        if user_action == "reload":
            try:
                self.client.reload_extension(f"cogs.{cog}_alox")
                embedCogReload = discord.Embed(title="Reloaded Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Reloaded```", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)
            except Exception:
                embedCogReload = discord.Embed(title="Failed To Reload Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Reload``` ", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)
        elif user_action == "unload":
            try:
                self.client.unload_extension(f"cogs.{cog}_alox")
                embedCogReload = discord.Embed(title="Unloaded Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Unloaded```", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)
            except Exception:
                embedCogReload = discord.Embed(title="Failed To Unload Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Unload``` ", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)
        elif user_action == "load":
            try:
                self.client.load_extension(f"cogs.{cog}_alox")
                embedCogReload = discord.Embed(title="Loaded Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xUp:868791667107463200> | {cog}",value = f"```Succesfully Loaded```", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)
            except Exception:
                embedCogReload = discord.Embed(title="Failed To Load Cog", color = 3447003)
                embedCogReload.add_field(name = f"<a:xDown:868791666700599327> | {cog}", value = f"```Failed To Load``` ", inline=False)
                disable_buttons()
                await res.respond(embed=embedCogReload, components = [buttons], type = 7)

def setup(client):
    client.add_cog(cogs_alox(client))
#IMPORTING MODULES
import random
import os
import sys
import traceback
from discord import activity
from discord.embeds import Embed
from dotenv import load_dotenv
import string
import discord
import datetime, time
from discord_components import*
import asyncio
import urllib.parse, urllib.request, re
from discord.ext import commands
from discord.ext.commands.errors import ExtensionNotFound, MessageNotFound, MissingPermissions, MissingRequiredArgument
from discord.ext.commands import Bot, has_permissions, CheckFailure

#---------------------------------------------------------------------#
#SETTING THE BOT PREFIX & MORE THINGS
#---------------------------------------------------------------------#
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ["al.", "AL.","Al.",","], intents=intents, status=discord.Status.dnd, activity = discord.Game (f'al.help | V.0.2.7'))
client.BotVersion = 'V.0.2.7'
global startTime
client.startTime = time.time()
load_dotenv()
client.GiphyKey = os.getenv("GIPHY_API_KEY")
client.remove_command("help")

#---------------------------------------------------------------------#
#WHEN READY, GETTING ALL THE COGS
#---------------------------------------------------------------------#

@client.event
async def on_ready():
    print("")
    print("""

░█████╗░██╗░░░░░░█████╗░██╗░░██╗  ██████╗░░█████╗░████████╗
██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔══██╗██╔══██╗╚══██╔══╝
███████║██║░░░░░██║░░██║░╚███╔╝░  ██████╦╝██║░░██║░░░██║░░░
██╔══██║██║░░░░░██║░░██║░██╔██╗░  ██╔══██╗██║░░██║░░░██║░░░
██║░░██║███████╗╚█████╔╝██╔╝╚██╗  ██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░
    """)
    print('╔═════*.·:·.:·:·:·░░☽✧ AloX is Ready ✧☾░░:·.·:·.:·:··*═════╗')
    print("")

    DiscordComponents(client)
    for file in os.listdir("cogs"):
        if file.endswith(".py"):
            try:
                client.load_extension(f"cogs.{file.strip('.py')}")
                print(f'╔═══*.·:·.:·:·:·░░☽✧ Loaded {file} ✧☾░░:·.·:·.:·:·*═══╗')
            except Exception as e:
                print(f'╔═══*.·:·.░░☽✧ Could not load cog {file} ✧☾░░.·:·.*═══╗')
                print(e)

#---------------------------------------------------------------------#
#ON A COMMAND ERROR
#---------------------------------------------------------------------#

@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, commands.errors.CheckFailure):
        embedCommandError = discord.Embed(title="Looks like you cant use that", color = 3447003)
        embedCommandError.add_field(name = "<a:xDown:868791666700599327> | You are missing permissions!", value = f"```{ctx.command} Has Failed To Operate```", inline=False)
        await ctx.send(embed=embedCommandError)
    elif isinstance(exc, commands.CommandNotFound):
        pass
    elif isinstance(exc, MessageNotFound):
        pass
    elif isinstance(exc, MissingPermissions):
        embedCommandError = discord.Embed(title="Looks like you cant use that", color = 3447003)
        embedCommandError.add_field(name = "<a:xDown:868791666700599327> | You are missing permissions!", value = f"```{ctx.command} Has Failed To Operate```", inline=False)
        await ctx.send(embed=embedCommandError)
    else:
        await ctx.send(f"""``` al.{ctx.command} [Arguments]
        ^^^^^^^^^^^
{exc}```""")
        print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
        traceback.print_exception(type(exc), exc, exc.__traceback__, file=sys.stderr)

#---------------------------------------------------------------------#
#RUNNING THE DISCORD TOKEN
#---------------------------------------------------------------------#
load_dotenv()
client.run(os.getenv("TOKEN"))

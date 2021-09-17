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
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component
#from discord.ext.commands.converter import GameConverter
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

import giphy_client
from giphy_client.rest import ApiException

from math import sqrt, pi

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class test_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#TEST COMMAND
#---------------------------------------------------------------------#

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def embed(self, ctx, *args):
        args = " ".join(args[:])
        args =  args.split(',')
        color = args[1]
        embedEmbed = discord.Embed(title = args[0], color = discord.Color.blue())
        print(args)
        length_args = (len(args)-2)//2
        for counter in range(0, length_args):
            embedEmbed.add_field(name = args[counter+2], value=args[counter+3])
        await ctx.send(embed=embedEmbed)



#---------------------------------------------------------------------#
#BOOP TEST COMMAND
#---------------------------------------------------------------------#
     
    @commands.command()
    async def boop_test(self, ctx, user: discord.Member):
        search = "boop"
        api_key = self.client.GiphyKey
        api_instance = giphy_client.DefaultApi()

        try:

            api_response = api_instance.gifs_random_get(api_key, tag=search, rating="g", fmt='json')
            gif = api_response.data.image_original_url

            embedBoop = discord.Embed(title=f'{ctx.author.name} boops {user.name}', color = 3447003)
            embedBoop.set_image(url=gif)
            embedBoop.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")

            await ctx.channel.send(embed=embedBoop)
            
        except ApiException as e:
            print("Exception when calling API for Giphy")

#---------------------------------------------------------------------#
#TEST 2 COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def wordgame(self, ctx):
        random_container = ''
        channel = ctx.message.channel
        vowels = ['A', 'E', 'I', 'O', 'U']
        d = enchant.Dict("en_US")
        
        for counter in range(3):
            random_container += random.choice(vowels)
        await ctx.send(f'Send a random word containing **{random_container}**')
        
        '''
        if check_word == True:
        else:
        '''
        def check(m): 
            if m != None:
                check_word = d.check(m.content.lower())
                if random_container.lower() in m.content.lower() and check_word == True and m.author == ctx.author:
                    return True
                else:
                    return False
            else:
                ctx.channel.send('You didnt send anything!')
        try:
            msg = await self.client.wait_for('message', check=check, timeout=10)
            await channel.send(f'Correct {msg.content}!')
        except asyncio.TimeoutError:
            await ctx.send('You didnt respond in time!')
        except:
            print('You didnt do anything')

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#
#hug, roast 

    @commands.command()
    async def test(self, ctx, num : int):
        bar_start = "<:barstart:870650383830229022>"
        bar_middle = "<:barmiddle:870650383293382707>"
        bar_half = "<:barhalf:870650383670837348>"
        bar_mid = "<:barmid:870690900685226046>"
        bar_end = "<:barend:870651709775560724>"
        bar100end = "<:bar100end:870693168650264586>"
        num = 5 * round(num/5)
        main_num = num
        num = [int(a) for a in str(num)]
        if main_num == 95:    
            await ctx.send(f"{bar_start}{(bar_middle * 8)}{bar_half}")
        elif str(num[1]) == str(5):
            remainder = (100 - main_num)-5 
            remainder = [int(a) for a in str(remainder)]
            #10, 40, 5, 5r, 40p
            await ctx.send(f"{bar_start}{(bar_middle * (num[0]-1))}{bar_half}{(bar_mid * ((remainder[0])-1))}{bar_end}")
        elif main_num == 100:
            await ctx.send(f"{bar_start}{(bar_middle * 8)}{bar100end}")
        else: 
            remainder=(100 - main_num)
            remainder = [int(a) for a in str(remainder)]
            await ctx.send(f"{bar_start}{(bar_middle * (num[0]-1))}{(bar_mid * ((remainder[0])-1))}{bar_end}")

    @commands.command()
    async def test_cog(self, ctx):
        
        await ctx.send(list)

#TEST COMMANDS

    @commands.command()
    async def test_rps(self, ctx, user : discord.Member):

        embedRPC = discord.Embed(title="Rock, Paper or Scissors", description="Choose either one from the button shown below!", color = 3447003)
        embedRPC.set_thumbnail(url="https://www.esquireme.com/public/styles/full_img/public/images/2017/05/29/rock_paper_scissors__2x.png?itok=7H3NxSxN")

        embedNotHere = discord.Embed(title=f"Rock, Paper or Scissors", color = 3447003)
        embedNotHere.add_field(name=f"{ctx.author.name}!", value = f'```{ctx.author.name} did not react, or has exited!```', inline=False)
        embedNotHere.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")

        buttons = [
            Button(style = ButtonStyle.grey, label = "Rock 🤘", id = "_rock"),
            Button(style = ButtonStyle.red, label = "Paper 📃", id = "_paper"),
            Button(style = ButtonStyle.green, label = "Scissors ✂", id = "_scissors"),
            Button(style = ButtonStyle.red, label = "Exit 🚪", id = "_exit"),
        ]
        def disable_buttons():
            for t in buttons:
                t.style = ButtonStyle.grey
                t.disabled = True

        button_ids = ["_rock", "_paper", "_scissors", "_exit"]

        msg = await ctx.send(embed=embedRPC, components = [buttons])
        while True:
            try:
                global i
                res = await self.client.wait_for("button_click", check=lambda i: i.component.id in button_ids and i.author.id == ctx.author.id or i.author.id == user.id and i.message.id == msg.id, timeout=10)
                global user_action

                if res.component.id == '_rock' == ctx.author.id:
                    user_action = "rock"
                    break

                elif res.component.id == '_paper':
                    user_action = "paper"
                    break

                elif res.component.id == '_scissors':
                    user_action = "scissors"
                    break

                elif res.component.id == '_exit':
                    disable_buttons()
                    await res.respond(embed=embedNotHere, components = [buttons], type = 7)
                    user_action = None
                    break

            except asyncio.TimeoutError:
                disable_buttons()
                #await res.respond(embed=embedNotHere, components = [buttons], type = 7)
                await msg.edit(embed=embedNotHere, components = [buttons])
                user_action = None
                break
            
        async def embedRPCWin(end):
            embedRPCWin = discord.Embed(title="Rock, Paper or Scissors", description=f"""
            **CPU** vs **{ctx.author.name}**!
            \n**CPU:** {computer_action.title()}
            **USER:** {user_action.title()}
            """, color = 3447003)
            embedRPCWin.add_field(name=f"--------------------------------------------", value = f'{end}' , inline=False)
            embedRPCWin.set_thumbnail(url="https://www.esquireme.com/public/styles/full_img/public/images/2017/05/29/rock_paper_scissors__2x.png?itok=7H3NxSxN")
            disable_buttons()
            await res.respond(embed=embedRPCWin, components = [buttons], type=7)

        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        global end
        if user_action == computer_action:
            end = (f"```Both players selected {user_action}. It's a tie!```")
            await embedRPCWin(end)
        elif user_action == "rock":
            if computer_action == "scissors":
                end = ("```Rock smashes scissors! You win!```")
                await embedRPCWin(end)
            else:
                end = ("```Paper covers rock! You lose.```")
                await embedRPCWin(end)
        elif user_action == "paper":
            if computer_action == "rock":
                end = ("```Paper covers rock! You win!```")
                await embedRPCWin(end)
            else:
                end = ("```Scissors cuts paper! You lose.```")
                await embedRPCWin(end)
        elif user_action == "scissors":
            if computer_action == "paper":
                end = ("```Scissors cuts paper! You win!```")
                await embedRPCWin(end)
            else:
                end = ("```Rock smashes scissors! You lose.```")
                await embedRPCWin(end)
        else:
            end = None
            pass

    @commands.command()
    async def test_embed(self, ctx):
        embedTest = discord.Embed(title="Test embed", description="This is a test embed", color = 0x2F3136  )
        await ctx.send(embed=embedTest)
        
def setup(client):
    client.add_cog(test_alox(client))
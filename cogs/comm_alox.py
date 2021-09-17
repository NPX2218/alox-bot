#---------------------------------------------------------------------#
#IMPORTING MODULES
#---------------------------------------------------------------------#

from math import e
from sys import platform
import discord
import sys
import random
import string
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
import asyncio
from discord import colour
from discord import embeds
from discord import widget
from discord.embeds import Embed, EmptyEmbed
from discord.ext import tasks, commands
import aiohttp
from discord.ext.commands.converter import GameConverter

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#
 
class comm_alox(commands.Cog):
    def __init__(self, client):
        self.client = client
        
#---------------------------------------------------------------------#
#COMMANDS COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['commands'])
    async def help(self, ctx):
            page0 = discord.Embed(title="**HOW TO USE COMMANDS?**", description="", colour = 3447003)
            page0.add_field(name=' 1. 🏓 al.command [] | [] Means a parameter ', value='Most likely a ping @Person',inline=False)
            page0.add_field(name=' 2. 👨‍💻 You can also use their ID with Developer Mode', value= 'eg: 745406828401524222', inline=False)
            page0.add_field(name=' 3. 📖 Make sure to read how to use the full command', value= 'Some may need 2 parameters', inline=False)
            page0.add_field(name=' 4. 📱 There are 3 prefixes: "," and "al." and "AL."', value= 'Make sure there is a space after al.', inline=False)
            page0.add_field(name=' 5. 🆘 al.commmands | al.help"', value= 'Use either of these commands to get help / commands', inline=False)
            page0.add_field(name=f' 6. Ⓜ Join the main server: https://dsc.gg/alox',value='Many special things there!', inline=False)

            page1 = discord.Embed(title="**FUN COMMANDS AloX**", description="", colour = 3447003)
            page1.add_field(name=' 🐱‍💻 Hack', value=' `al.hack <>`', inline=True)
            page1.add_field(name=' ❎ Tic Tac Toe', value=' `al.tictactoe <> <>`', inline=True)
            page1.add_field(name=' 🅾 Tic Tac Toe Place', value=' `al.place <Num>`', inline=True)
            page1.add_field(name=' 👊 Fight', value='`al.fight <>`', inline=True)
            page1.add_field(name=' 💖 Match / Love Calculator', value='`al.match <User_1> <User_2>`',inline=True)
            page1.add_field(name=' 🔟 Numguess out of 10', value= '`al.numguess <0-10>`', inline=True)
            page1.add_field(name=' 😂 Memes from r/memes', value= '`al.meme`', inline=True)
            page1.add_field(name=' 🔨 Fake Ban', value= '`al.,ban`', inline=True)
            page1.add_field(name=' 🤘 Rock, Paper Scissors', value='`al.rps`',inline=True)
            page1.set_footer(text='<> Required | [] Optional')
            #Page 2
            page2 = discord.Embed(title="**MATH COMMANDS AloX**", description="", colour= 3447003)
            page2.add_field(name=' 2️⃣ Add', value=' `al.add <Num_1> <Num_2>`', inline=True)
            page2.add_field(name=' 🪓 Subtract', value=' `al.sub <Num_1> <Num_2>`', inline=True)
            page2.add_field(name=' 🔮 Divide', value=' `al.div <Num_1> <Num_2>`', inline=True)
            page2.add_field(name=' ❌ Multiply', value=' `al.mult <Num_1> <Num_2>`', inline=True)
            page2.add_field(name=' 💹 Odds', value=' `al.odds <Num_1> <Num_2>`', inline=True)
            page2.set_footer(text='<> Required | [] Optional')

            #Page 3
            page3 = discord.Embed(title="**IMAGE / MANIPULATION COMMANDS AloX**", description="", colour = 3447003)
            page3.add_field(name=' 🦢 Ugly', value=' `al.ugly [User]`', inline=True)
            page3.add_field(name=' 💵 Wanted', value=' `al.ping **OR** al.latency`', inline=True)
            page3.add_field(name=' 📔 Hide The Face', value=' `al.hideface [User]`', inline=True)
            page3.add_field(name=' 🔥 Burn', value=' `al.burn [User]`', inline=True)
            page3.add_field(name=' 🤚  Slap', value='`al.slap <User>`', inline=True)
            page3.add_field(name=' 😭 Cry', value=' `al.cry [User]`', inline=True)
            page3.add_field(name=' 🔤 Text', value=' `al.textimg <Text>`', inline=True)
            page3.add_field(name=' 💻 Avatar', value=' `al.avatar <User>`', inline=True)
            page3.set_footer(text='<> Required | [] Optional')
            
            #Page 4
            page4 = discord.Embed(title="**SEARCH COMMANDS AloX**", description="", colour = 3447003)
            page4.add_field(name=' 🧠 Google', value='`al.google <>`', inline=True) 
            page4.add_field(name=' 📫 YouTube', value='`al.youtube <>`', inline=True) 
            page4.add_field(name=' ⌚ UTC Timezone', value='`al.utc`', inline=True) 
            page4.set_footer(text='<> Required | [] Optional')

            #Page 5       
            page5 = discord.Embed(title="**USEFUL COMMANDS AloX**", description="", colour = 3447003)
            page5.add_field(name=' 🎹 AFK', value='`al.afk`', inline=True) 
            page5.add_field(name=' 💻 Remove AFK', value='`al.unafk`', inline=True) 
            page5.add_field(name=' ❔  Who is?', value='`al.whois <User>`', inline=True)
            page5.add_field(name=' 💁‍♀️  Docs', value='`al.docs`', inline=True)
            page5.add_field(name=' 😶 Say', value=' `al.say <>`', inline=True)
            page5.add_field(name=' 💄  Make Role', value='`al.makerole <Name>`', inline=True)
            page5.add_field(name=' 👩‍⚖️ Poll | Max 6', value='`al.poll <Title | Option 1 | Option 2>`', inline=True)
            page5.add_field(name=' 👻 Purge', value=' `al.purge <>`', inline=True)
            page5.set_footer(text='<> Required | [] Optional')

            #Page 6       
            page6 = discord.Embed(title="**GIPHY COMMANDS AloX**", description="", colour = 3447003)
            page6.add_field(name=' 📦 GIF', value='`al.afk <User>`', inline=True) 
            page6.add_field(name=' 🔪 GIF Kill', value='`al.kill <User> `', inline=True) 
            page6.add_field(name=' 👈 GIF Boop', value='`al.boop <User>`', inline=True)
            page6.set_footer(text='<> Required | [] Optional')

            #Page 10       
            page10 = discord.Embed(title="**OTHER**", description="", colour = 3447003)
            page10.add_field(name=' 👾 Creator', value=' `al.creator`', inline=True)
            page10.add_field(name=' 🏓 Ping', value=' `al. ping **OR** al. latency`', inline=True)
            page10.add_field(name=' 📊 Bot Stats', value=' `al. stats`', inline=True)
            page10.add_field(name=' 🕗 Uptime', value=' `al. uptime`', inline=True)
            page10.set_footer(text='<> Required | [] Optional')

            embeds = [page0, page1, page2, page3, page4, page5, page6, page10]
            page = 1
            buttons = [
                        Button(style=ButtonStyle.grey,emoji = self.client.get_emoji(874687192490999838), id = "_beg"),
                        Button(style=ButtonStyle.red, emoji = self.client.get_emoji(874687192281251841), id = '_prev'),
                        Button(style=ButtonStyle.grey, label = f"TOTAL PAGES {len(embeds)} ", id = '_page', disabled=True), 
                        Button(style=ButtonStyle.green, emoji= self.client.get_emoji(874687192574861322), id = '_next'),
                        Button(style=ButtonStyle.grey, emoji = self.client.get_emoji(874687192772009984), id = "_end"),
                      ]

            msg = await ctx.send(embed=embeds[0], components=[buttons])
            button_ids = ['_prev', '_page', '_next', "_end", "_beg"]
            while True:
                try:
                    res = await self.client.wait_for("button_click", check=lambda i: i.component.id in button_ids and i.author.id == ctx.author.id and i.message.id == msg.id, timeout=15)
                    if res.component.id == '_prev':
                        if page == 1:
                            page = len(embeds)
                        else:
                            page -= 1
                    elif res.component.id == '_next':
                        if page == len(embeds):
                            page = 1
                        else:
                            page += 1
                    elif res.component.id == "_end":
                        page = len(embeds)
                    elif res.component.id == "_beg":
                        page = 1
                            
                    await res.respond(type=7, embed=embeds[page-1], components=[buttons])   

                except asyncio.TimeoutError:
                    for t in buttons:
                        t.disabled = True
                    await msg.edit(embed=embeds[page-1], components=[buttons])
                    break

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(comm_alox(client))

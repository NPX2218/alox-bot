#---------------------------------------------------------------------#
#IMORTING THE MODULES
#---------------------------------------------------------------------#

import random
import os
import string
import discord
import asyncio
import urllib.parse, urllib.request, re
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType, component


#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class usef_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#AFK COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def afk(self, ctx):
        if '[AFK]' not in ctx.author.nick:
            current_nick = ctx.author.nick
            await ctx.send(f"{ctx.author.mention} has gone afk.")
            await ctx.author.edit(nick=f"[AFK] {ctx.author.nick}")
        else:
            await ctx.send('You are already afk!')


    @commands.command()
    async def unafk(self, ctx):
        if '[AFK]' in ctx.author.nick:
            current_nick = ctx.author.nick
            await ctx.send(f"{ctx.author.mention} has come back from being afk.")
            remove_afk = current_nick.lstrip("[AFK]")
            await ctx.author.edit(nick=f"{remove_afk}")
        else:
            await ctx.send('You aren\'t afk!')
#---------------------------------------------------------------------#
#RULES COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    @has_permissions(administrator=True)
    async def rules(self, ctx):
        embedRules = discord.Embed(title='Rules For AloX', colour = 3447003)
        embedRules.add_field(name='**__Main Rules__**', value=f"""
        1. Please do not use any of the censored words.
        2. Please do not use any sort of homophobic or racist language.
        3. Please do not swear at people e.g. Fuck you.
        6. Staff have the last say, please do not argue with them, if you disagree ask another member of staff for a second opinion.
        7. Please respect other members, this means moving on when someone feels uncomfortable with a topic, along with no malicious DMs etc.
        8. ANY sort of bullying will result in a temporary ban as this is absolutely unacceptable here.
        9. Do not bypass or evade any of these rules.
        10. Enjoy yourself
        """)
        embedRules.add_field(name='**__Punishment System__**', value=f"""
        Punishment System
        You will receive verbal warnings which come with a mute when you break a rule. Unless it is a severe break in rules then this will happen:

        Minor break in rules

        1st Warning: 30m mute
        2nd Warning: 1.5h mute
        3rd Warning: 5h mute
        4th Warning: 12h mute
        5th Warning: 1d mute

        Severe break in rules

        Note, severe break in rules get you a physical warning from carl bot

        1st Warning: 6h mute
        2nd Warning: 1d mute
        3rd Warning: 3d mute
        4th Warning: 1w temporary ban
        5th Warning: Permanent ban

        Admin+ are allowed to punish you how they see fit, these are only the guidelines for moderators.
        If you have any question do not hesitate to contact a moderator+.
        """)
        await ctx.send(embed=embedRules)

#---------------------------------------------------------------------#
#BOOSTER COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def booster(self, ctx):
        embedBooster = discord.Embed(title='Booster Perks For AloX', colour = 3447003)
        embedBooster.add_field(name='**__Booster Perks__**', value=f"""
        Single Booster Perks
        - Able to change nickname whenever you like.
        - More selection of colours.

        **__Double Booster__**
        - All of the above.
        - Snipe permission.
        """)
        await ctx.send(embed=embedBooster)

#---------------------------------------------------------------------#
#embed_poll COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def embed_poll(self, ctx, *args):
        await ctx.message.delete()
        reactions_poll = ['1️⃣', '2️⃣', '3️⃣','4️⃣','5️⃣', '6️⃣']
        args = " ".join(args[:])
        args = args.split('|')
        if len(args) > 7:
            await ctx.send('You can only have 6 Deciding factors!')
        else:
            embedPoll = discord.Embed(title=args[0], color = 3447003)
            for counter in range(len(args)-1):
                embedPoll.add_field(name =f"{reactions_poll[counter]} : {args[counter+1]}", value="\u200b",)
            embedPoll.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
            message = await ctx.send(embed=embedPoll)
            for counter in range(len(args)-1):
                await message.add_reaction(f"{reactions_poll[counter]}")

#---------------------------------------------------------------------#
#POLL COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def poll(self, ctx, *args):
        await ctx.message.delete()
        reactions_poll = ['1️⃣', '2️⃣', '3️⃣','4️⃣','5️⃣', '6️⃣']
        args = " ".join(args[:])
        args = args.split('|')
        if len(args) > 7:
            await ctx.send('You can only have 6 Deciding factors!')
        else:
            poll_message = f"**{args[0]}**\n"
            for counter in range(len(args)-1):
                poll_message += f"{reactions_poll[counter]} : **{args[counter+1]}**\n"
            message = await ctx.channel.send(poll_message)
            for counter in range(len(args)-1):
                await message.add_reaction(f"{reactions_poll[counter]}")

#---------------------------------------------------------------------#
#QUICKPOLL COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def quickpoll(self, ctx, *args):
        await ctx.message.delete()
        args = " ".join(args[:])
        poll_message = f"**{ctx.author} asks :** {args}\n"
        message = await ctx.channel.send(poll_message)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

#---------------------------------------------------------------------#
#DOCS ALOX COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=["website"])
    async def docs(self, ctx):
        embedDocs = discord.Embed(title='AloX Bot Website', colour = 3447003)
        embedDocs.add_field(name='The Link: ',value='https://alox-bot.gitbook.io/alox/')
        embedDocs.set_thumbnail(url='https://media.discordapp.net/attachments/864795080136458303/868111109767458847/frbSpqblAxkMSJCl-croppedxmuR2-png.png')

        buttons = [[
            Button(style=ButtonStyle.URL, label = "THE WEBSITE", url = 'https://alox-bot.gitbook.io/alox/'),
            Button(style=ButtonStyle.URL, label = "SUPPORT SERVER!",url=f'https://dsc.gg/alox'),
        ]]

        embedDocs.set_thumbnail(url="https://cdn.discordapp.com/attachments/864795079662895125/867517032105771028/image0.gif")

        await ctx.send(embed=embedDocs, components = buttons)

#---------------------------------------------------------------------#
#MAKE-ROLE COMMAND
#---------------------------------------------------------------------#

    @commands.command(name='makerole')
    @commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
    async def create_role(self, ctx, *, name):
        guild = ctx.guild
        await guild.create_role(name=name)
        embedRole = discord.Embed(title=f"Role Creation", colour = 3447003)
        embedRole.add_field(name = f'Role `{name}` has been created', value = "Successfully Created")
        await ctx.send(embed=embedRole)

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(usef_alox(client))

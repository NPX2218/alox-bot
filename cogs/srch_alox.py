#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#

import discord
import random
import string
import urllib.parse, urllib.request, re
import asyncio
from datetime import datetime, timezone
from discord import embeds
from discord.ext import commands

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#
class srch_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#SEARCHING GOOGLE COMMAND
#---------------------------------------------------------------------#    
    @commands.command()
    async def google(self, ctx, *search_args):
        args = " ".join(search_args[:])
        embedGoogle = discord.Embed(title="You Entered:", description=f'```{args} ```', color = 3447003)
        args = args.replace(" ", "+")
        embedGoogle.add_field(name="Link", value = f'https://www.google.com/search?q={args} ')
        embedGoogle.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Google_%22G%22_Logo.svg/2048px-Google_%22G%22_Logo.svg.png')
        embedGoogle.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")
        await ctx.send(embed=embedGoogle)

#---------------------------------------------------------------------#
#UTC COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def utc(self, ctx):
        time_utc = datetime.now(timezone.utc)
        string_date = time_utc.strftime("%A, %B %d, %Y, %I%p")
        time_utc_embed = discord.Embed(title='UTC TIME', description=f'```{string_date}```', color = 3447003)
        time_utc_embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsrVjfMBJotIJIdWEbqxYlFoA61e-9oASNAw&usqp=CAU')
        await ctx.send(embed=time_utc_embed)

#---------------------------------------------------------------------#
#YOUTUBE COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases = ["yt"])
    async def youtube(self, ctx,*, search):
        query_string = urllib.parse.urlencode({
            'search_query': search
        })

        html_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string
        )
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        
        embedYoutube = discord.Embed(title="You Entered:", description=f"```{search}```", color = 3447003, url = 'http://www.youtube.com/watch?v=' + search_results[0] )
        embedYoutube.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/YouTube_social_white_squircle_%282017%29.svg/1200px-YouTube_social_white_squircle_%282017%29.svg.png')
        embedYoutube.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")
        await ctx.send(embed=embedYoutube)
        await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#
  
def setup(client):
    client.add_cog(srch_alox(client))
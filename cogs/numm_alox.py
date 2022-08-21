#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#

import discord
import random
from discord.ext import commands
from math import sqrt, pi

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class numm_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#NUMGUESS COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def numguess(self, ctx, *, number=0):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        correct_number = random.choice(number_list)

        if number == correct_number:
            embedNumGuess = discord.Embed(title=f'The Number Was {correct_number}', color=3447003)
            embedNumGuess.add_field(name='You Picked The Correct Number! You Won', value="Thanks For Playing!")
        
        else:
            embedNumGuess = discord.Embed(title=f'The Number Was {correct_number}', color=3447003)
            embedNumGuess.add_field(name="Sorry, You Picked The Wrong Number", value="Thanks For Playing")
        embedNumGuess.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")        
        await ctx.send(embed=embedNumGuess)
    
#---------------------------------------------------------------------#
#ADDITION COMMAND
#---------------------------------------------------------------------#
    @commands.command()
    async def add(self, ctx, *nums):
        arg = " ".join(nums[:])
        args = arg.split(",")
        main = " + ".join(args[:])
        sum = 0
        for counter in range(len(args)):
            sum += float(args[counter])
        embedAdd = discord.Embed(title="Addition", color = 3447003)
        embedAdd.add_field(name=f"{main} = ", value = sum, inline=False)
        embedAdd.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedAdd.set_thumbnail(url='https://pixfeeds.com/images/31/603109/1280-plus-sign.png')
        await ctx.send(embed=embedAdd)
        
#---------------------------------------------------------------------#
#SUBTRACTION COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def sub(self, ctx, *nums):
        arg = " ".join(nums[:])
        args = arg.split(",")
        main = " - ".join(args[:])
        sum = 0
        for counter in range(len(args)):
            sum -= float(args[counter])
        embedSub = discord.Embed(title="Subtraction", color = 3447003)
        embedSub.add_field(name=f"{main} = ", value = sum, inline=False)
        embedSub.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedSub.set_thumbnail(url='https://pixfeeds.com/images/31/603109/1280-minus-sign.png')
        await ctx.send(embed=embedSub)

#---------------------------------------------------------------------#
#DIVISION COMMAND
#---------------------------------------------------------------------#
    @commands.command()
    async def div(self, ctx,*nums):
        arg = " ".join(nums[:])
        args = arg.split(",")
        main = " / ".join(args[:])
        sum = 0
        for counter in range(len(args)):
            sum /= float(args[counter])
        
        embedDiv = discord.Embed(title="Division", color = 3447003)
        embedDiv.add_field(name=f"{main} = ", value = sum, inline=False)
        embedDiv.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedDiv.set_thumbnail(url='https://pixfeeds.com/images/31/603109/1280-division.png')
        await ctx.send(embed=embedDiv)

#---------------------------------------------------------------------#
#MULTIPLICATION COMMAND
#---------------------------------------------------------------------#    
    @commands.command()
    async def mult(self, ctx, *nums):
        arg = " ".join(nums[:])
        args = arg.split(",")
        main = " * ".join(args[:])
        sum = 0
        for counter in range(len(args)):
            sum *= float(args[counter])
        
        embedMult = discord.Embed(title="Multiplication", color = 3447003)
        embedMult.add_field(name=f"{main} = ", value = sum, inline=False)
        embedMult.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedMult.set_thumbnail(url='https://pixfeeds.com/images/31/603109/1280-multiplication.png')
        await ctx.send(embed=embedMult)
    
#---------------------------------------------------------------------#
#ODDS COMMAND
#---------------------------------------------------------------------#    
    @commands.command()
    async def odds(self, ctx, odds_1 : int, odds_2 : int ):
        global chosenone
        global odds_final
        embedOdds = discord.Embed(title="Odds Picker", color = 3447003)
        chosenone = ""
        randominteger : int = random.randint(0,101)
        if randominteger >= odds_1:
            chosenone = odds_2
            odds_final = (f'Person 2 Wins! {odds_2}')
        else:
            chosenone = odds_1
            odds_final = (f'Person 1 Wins! {odds_1}')

        embedOdds.add_field(name=f"{odds_1} between {odds_2} = ", value = odds_final, inline=False)
        embedOdds.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedOdds.set_thumbnail(url='https://png.pngtree.com/png-vector/20191018/ourlarge/pngtree-question-mark-vector-icon-png-image_1824218.jpg')       
        await ctx.send(embed=embedOdds)
#---------------------------------------------------------------------#
#TRIANGLE COMMAND
#---------------------------------------------------------------------#
    @commands.command()
    async def triangle(self, ctx, base : float , height : float, hypotenuse : float ):
        embedTriangle = discord.Embed(title='Triangle\'s Values', colour = 3447003)
        embedTriangle.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Simple_triangle.svg/1200px-Simple_triangle.svg.png')
        embedTriangle.add_field(name = 'Values', value=f"""
        **Base:** ```{base}```
        **Height:** ```{height}```
        **Hypotenuse:** ```{hypotenuse}```
        """)
        embedTriangle.add_field(name = 'Area', value=f'{((base / 2) * height)}')
        embedTriangle.add_field(name = 'Perimeter', value=f'{base + height + hypotenuse}')
        await ctx.send(embed=embedTriangle)

#---------------------------------------------------------------------#
#PYTHAGORAS COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def pythag(self, ctx, base : float, height : float):
        embedPythag = discord.Embed(title='Triangle\'s Hypotenuse', colour = 16776960)
        embedPythag.set_thumbnail(url='https://www.piday.org/wp-content/uploads/2019/06/word-image-20.png')
        embedPythag.add_field(name = 'Values', value=f"""
        **Base:** ```{base}```
        **Height:** ```{height}```
        **Hypotenuse:** ```{sqrt(base * base + height * height)}```
        """)
        await ctx.send(embed=embedPythag)

#---------------------------------------------------------------------#
#CIRCLE COMMAND
#---------------------------------------------------------------------#

    @commands.command() 
    async def circle(self, ctx, radius : float):
        embedCircle = discord.Embed(title='Circle\'s Values', colour = 3447003 )
        embedCircle.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Circle_-_black_simple.svg/768px-Circle_-_black_simple.svg.png')
        embedCircle.add_field(name='Values', value=f"""
        **Radius**: ```{radius}```
        **Diameter**: ```{radius**2}```
        **Area:** ```{pi*(radius**2)}```
        **Circumfrence:** ```{2*pi*radius}```
        """)
        await ctx.send(embed=embedCircle)

#---------------------------------------------------------------------#
#LATENCY / PING COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        server_ping = round(self.client.latency * 1000)
        embedlatency = discord.Embed(title="PING LATENCY", description= f"```{server_ping}ms```",color = 3447003)
        embedlatency.set_thumbnail(url="https://i2.wp.com/blog.3balls.com/wp-content/uploads/2014/08/Ping-logo.jpg?resize=625%2C203")
        await ctx.send(embed=embedlatency)

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(numm_alox(client))
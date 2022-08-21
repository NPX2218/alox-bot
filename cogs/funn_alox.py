#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#

import discord
import random
import string
from discord import user
from discord.flags import PublicUserFlags
from discord_components import DiscordComponents, Button, ButtonStyle, component
import asyncio
import aiohttp
from discord.ext import commands

#---------------------------------------------------------------------#
#SETTING THE COG 
#---------------------------------------------------------------------#

class funn_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#8-BALL COMMAND
#---------------------------------  ------------------------------------#

    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        embed8ball = discord.Embed(title=f"8-Ball Guesser", color = 3447003)
        responses = [
                    "It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        embed8ball.add_field(name=f"RESULTS", value = f"Question: ```{question.title()}```\nAnswer: ```{random.choice(responses)}```" , inline=False)
        embed8ball.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embed8ball.set_thumbnail(url='https://www.pngkit.com/png/detail/81-816632_8-ball-8-ball-black-and-white.png')
        await ctx.send(embed=embed8ball)

#---------------------------------------------------------------------#
#FIGHT COMMAND
#---------------------------------------------------------------------#


    @commands.command()
    async def fight(self, ctx,*, user: discord.Member):
        await ctx.send(f"""👊 **FIGHT** 🦵
🔻 {user.name}
🔺 {ctx.author.name}
                """)
        embedStart = discord.Embed(title=f"Fight Against {user.name} and {ctx.author.name}", color = 3447003)
        embedStart.add_field(name=f"{ctx.author.name} Started a fight | {user.name} needs to choose an option from below", value = f'👊 : `Punch`\n🦵 : `Kick`\n⛔ : `Block`\n🏃‍♂️ : `Run Away`' , inline=False)
        embedStart.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        embedStart.set_thumbnail(url="https://media.discordapp.net/attachments/693517202879414312/860599179578966056/Fight_icon.png")
        
        embedNotHere = discord.Embed(title=f"Fight Against {user} and {ctx.author}", color = 3447003)
        embedNotHere.add_field(name=f"{user.name} IS NOT HERE!", value = f'{user.mention} did not react!' , inline=False)
        embedNotHere.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
                
        buttons = [
            Button(style=ButtonStyle.grey, label = "👊 Punch", id = '_punch'),
            Button(style=ButtonStyle.grey, label = f"🦵 Kick", id = '_kick'), 
            Button(style=ButtonStyle.green, label="⛔ Defend", id = '_block'),
            Button(style=ButtonStyle.red, label = "🏃‍♂️ Run away", id = '_run')
            ]
        def disable_buttons():
            for t in buttons:
                t.style = ButtonStyle.grey
                t.disabled = True
            

        button_ids = ["_punch", "_kick", "_block", "_run"]
        msg = await ctx.send(embed=embedStart, components = [buttons])
        async def embedfight(fightresponse):
            embedFight = discord.Embed(title=f"Fight Against {user.name} and {ctx.author.name}", color = 3447003)
            embedFight.add_field(name=f"RESULTS", value = f'`{fightresponse}`' , inline=False)
            embedFight.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")            
            embedFight.set_thumbnail(url="https://media.discordapp.net/attachments/693517202879414312/860599179578966056/Fight_icon.png")
            disable_buttons()
            await res.respond(embed=embedFight, components=[buttons], type=7)

        while True:
            try:
                res = await self.client.wait_for("button_click", check=lambda i: i.component.id in button_ids and i.author.id == user.id and i.message.id == msg.id, timeout=5)
                if res.component.label == '👊 Punch':
                    fightresponses = [
                    f"{user.name} punches and {ctx.author.name} passes out",
                    f"{user.name} punches, but then {ctx.author.name} uppercuts {user.name}",
                    f"{ctx.author.name} Sends a left hook towards {user.name} and knocks them out",
                    f"{user.name} Thrust's their fist towards {ctx.author.name} and wins!",
                    ]
                    await embedfight(random.choice(fightresponses))
                    break

                elif res.component.label == '🦵 Kick':
                    fightresponses = [
                    f"{user.name} kickes and {ctx.author.name} passes out",
                    f"{user.name} kickes, but then {ctx.author.name} trips {user.name}",
                    ]
                    await embedfight(random.choice(fightresponses))
                    break           

                elif res.component.label == '⛔ Defend':
                    fightresponses = [f"{user.name} Blocks and {ctx.author.name} runs out of stamina",
                    f"{user.name} Blocks, but then {ctx.author.name} punches them on the leg!",
                    ]
                    await embedfight(random.choice(fightresponses))
                    break

                elif res.component.label == '🏃‍♂️ Run away':
                    fightresponses = [f"{user.name} Runs away, What a wimp",
                    f"Goodbye {user.name} is such a wimp! They ran away!",
                    ]
                    await embedfight(random.choice(fightresponses))
                    break

            except asyncio.TimeoutError:
                disable_buttons()
                #await res.respond(embed=embedNotHere, components=[buttons], type = 7)
                await msg.edit(embed=embedNotHere, components=[buttons])
                break
        

#---------------------------------------------------------------------#
#LOVE / MATCH COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['love'])
    async def match(self, ctx, user_1 : discord.Member, user_2 : discord.Member = None):
        if user_2 == None:
            user_2 = ctx.author
        if user_1 == user_2:
            await ctx.send('They probably love themself.')
        else:
            percent_love = random.randint(10,101)
            bar_start = "<:barstart:870650383830229022>"
            bar_middle = "<:barmiddle:870650383293382707>"
            bar_half = "<:barhalf:870650383670837348>"
            bar_mid = "<:barmid:870690900685226046>"
            bar_end = "<:barend:870651709775560724>"
            bar100end = "<:bar100end:870693168650264586>"
            num = 5 * round(percent_love/5)
            main_num = num
            num = [int(a) for a in str(num)]

            if main_num == 95:    
                var = (f"{bar_start}{(bar_middle * 8)}{bar_half}")
            elif str(num[1]) == str(5):
                remainder = (100 - main_num)-5 
                remainder = [int(a) for a in str(remainder)]
                #10, 40, 5, 5r, 40p
                var =  (f"{bar_start}{(bar_middle * (num[0]-1))}{bar_half}{(bar_mid * ((remainder[0])-1))}{bar_end}")
            elif main_num == 100:
                var = (f"{bar_start}{(bar_middle * 8)}{bar100end}")
            else:   
                remainder=(100 - main_num)
                remainder = [int(a) for a in str(remainder)]
                var = (f"{bar_start}{(bar_middle * (num[0]-1))}{(bar_mid * ((remainder[0])-1))}{bar_end}")

            embedLove = discord.Embed(title = f'Love Between {user_1.name} and {user_2.name}', description=f'{var}', color = 3447003)
            embedLove.add_field(name="[]———— ❤ Results ❤ ————[]", value = f'Match amount: {percent_love}%') 
            embedLove.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
            if percent_love > 60:
                embedLove.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Heart_coraz%C3%B3n.svg/1200px-Heart_coraz%C3%B3n.svg.png')
                heart = "💗"
            else:    
                embedLove.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Broken_heart_SVG.svg/782px-Broken_heart_SVG.svg.png')
                heart = "💔"

            components = [[
                Button(style=ButtonStyle.red, label = f"{user_1.name}"),
                Button(style=ButtonStyle.grey, label = f"{heart}"),
                Button(style=ButtonStyle.red, label = f"{user_2.name}"),
                
            ]]

            await ctx.send(f"""💗 **MATCH MAKING** 💗
🔻 {user_1.name}
🔺 {user_2.name}
            """)
            await ctx.send(embed=embedLove, components = components)

#---------------------------------------------------------------------#
#CHECK-DMS COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['Hack'])
    async def hack(self, ctx,*, user : discord.Member):
        embedhack = discord.Embed(title="HACK", description="*The completely real and life changing hack has been completed*", color = 3447003)
        ip = ".".join(map(str, (random.randint(0, 255) 
                                for _ in range(4))))
        message = await ctx.send(f'[▝] **Collecting Username:** {user}')
        await asyncio.sleep(3)
        await message.edit(content='[▖] **Collecting Password**')
        await asyncio.sleep(3)
        await message.edit(content='[▝] **Bypassing 2FA**')
        await asyncio.sleep(3)
        await message.edit(content='[▖] **Checking Dms**')
        await asyncio.sleep(3)
        emailhack = ""
        passhack = ""
        for counter in range(1,7):            
            emailhack = emailhack + (''.join(random.choice(string.ascii_letters)))
            passhack = passhack + (''.join(random.choice(string.ascii_lowercase)))
    
        await message.edit(content=f'[▝] **Email Information Located**\n**Email:** {emailhack}@gmail.com\n**Password:** {passhack}')
        await asyncio.sleep(3)
        await message.edit(content=f'[▖] Collecting Details, **IP Address:** {ip}')
        await asyncio.sleep(3)
        dmsresponses = ["Lol im such a idiot",
                        "I hate you",
                        "I love You",
                        f"My discord password is {passhack}",
                        "Where is the money",
                        "My Visa CVV is 423",
                        "My Apple giftcards number is 194649242",
                        "2FA Has blocked message output",
                        "I am stupid lol",
                        "I need help",
                        "Im Married to you",
                        "I cheated on the test"]
        await message.edit(content=f'[▝] **Most recent message:** {random.choice(dmsresponses)}')
        await asyncio.sleep(3)

        trojan_counter = 0
        for counter in range(5):
            await asyncio.sleep(1)
            await message.edit(content=f'[▖] **Injecting Trojan:** {trojan_counter}%  ')
            trojan_counter +=25
        await asyncio.sleep(3)

        percent_counter = 0
        for counter in range(5):
            await asyncio.sleep(1)
            await message.edit(content=f'[▝] **Setting up bank account:** {percent_counter}%')
            percent_counter +=25

        await asyncio.sleep(2)
        await message.edit(content=f'[▖] Removing all traces from discriminator **#{user.discriminator}**')
        await asyncio.sleep(3)
        await message.edit(content=f'[▖] The hack has been **completed**')
        embedhack.add_field(name="PERSON TARGETED", value = f"```{user}```", inline=False)
        embedhack.add_field(name="IP ADDRESS", value = f"```{ip}```", inline=False)
        embedhack.add_field(name="EMAIL AND PASSWORD", value = f"```Email: {emailhack}@gmail.com \nPassword: {passhack}```", inline=False)
        embedhack.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author}")
        await ctx.send(embed=embedhack)

#---------------------------------------------------------------------#
#MEME REDDIT COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/memes.json") as response:
                j = await response.json()

        data = j["data"]["children"][random.randint(0, 25)]["data"]
        image_url = data["url"]
        title = data["title"]
        upvotes = data["ups"]
        comments = data["num_comments"]
        embedRedditMeme = discord.Embed(description=f"[**{title}**]({image_url})", color=3447003)
        embedRedditMeme.set_image(url=image_url)
        embedRedditMeme.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author} | 🔼 {upvotes} | 💬 {comments}")
        await ctx.send(embed=embedRedditMeme)

#---------------------------------------------------------------------#
#FAKE BAN COMMAND
#---------------------------------------------------------------------#
        
    @commands.command(name=',ban')
    async def _ban(self, ctx, user : discord.Member, *reason):
        reason = " ".join(reason[:])
        await ctx.send(f'Banned **{user}** Reason: {reason}')

#---------------------------------------------------------------------#
#ROCK PAPER SCISSORS COMMAND
#---------------------------------------------------------------------#
    @commands.command()
    async def rps(self, ctx):

        embedRPC = discord.Embed(title="Rock, Paper or Scissors", description="Choose either one from the button shown below!", color = 3447003)
        embedRPC.add_field(name=f"{ctx.author.name} Started a Rock, Paper, Scissors game against CPU", value = f'🤘 : `Rock`\n📃 : `Paper`\n✂ : `Scissors`\n🚪 : `Exit`' , inline=False)
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
                res = await self.client.wait_for("button_click", check=lambda i: i.component.id in button_ids and i.author.id == ctx.author.id and i.message.id == msg.id, timeout=10)
                global user_action
                if res.component.id == '_rock':
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

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#
     
def setup(client):
    client.add_cog(funn_alox(client))
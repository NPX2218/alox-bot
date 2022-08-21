#---------------------------------------------------------------------#
#IMPORTING THE MODULES
#---------------------------------------------------------------------#
import discord
import asyncio
import sys
import random
import datetime, time
import discord_components
import PIL
from discord_components import component
import psutil
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle


#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class misc_alox(commands.Cog):
    def __init__(self, client):
        self.client = client

#---------------------------------------------------------------------#
#CREATOR COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def creator(self, ctx):
        embedCreator = discord.Embed(title="Dev Team", description="```Neel```", color = 3447003)
        embedCreator.add_field(name="Est: 24/06/2021", value = "```Updates coming!```", inline=False)
        embedCreator.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHiFRLnG1vyP3euoRf4fGNzqmW-ao7MJ4Vlw&usqp=CAU')
        await ctx.send(embed=embedCreator)

#---------------------------------------------------------------------#
#WHO IS? COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def whois(self, ctx, user : discord.Member):
        if user is None:
            user = ctx.author
        global emoji_status
        users_status = user.status
        if str(users_status) == 'offline':
            emoji_status = '<:offline:864457214668701696>'
        elif str(users_status) == 'idle':
            emoji_status = '<:idle:864457214726635570>'
        elif str(users_status) == 'online':
            emoji_status = '<:online:864457214713921536>'
        elif str(users_status) == 'dnd':
            emoji_status = '<:dnd:864457214592286790>'
        else:
            emoji_status = "Fail"

        rolelist = [r.mention for r in user.roles if r != ctx.guild.default_role]
        roles = ", ".join(rolelist)
        if len(rolelist) > 20:
            roles = 'Too many roles to list'
        else:
            pass

        avatar_url_jpg = user.avatar_url_as(format="jpg")
        embedWho = discord.Embed(title = f'Statistics for {user.name}', description = user.mention, color = 3447003)
        embedWho.add_field(name="📛 Name", value=f"{user.name}")
        embedWho.add_field(name="🕺 Discriminator", value=f"#{user.discriminator}")
        embedWho.add_field(name="🐕 Nickname", value=f"{user.nick}")
        embedWho.add_field(name="⚔ Avatar URL", value=f"[[Click here]]({avatar_url_jpg})")
        embedWho.add_field(name="👶 Account created", value=f"{user.created_at}")
        embedWho.add_field(name="💪 Joined Server", value=f"{user.joined_at}")
        embedWho.add_field(name="🔝 Top Role", value=f"{user.top_role.mention}")
        embedWho.add_field(name="🤖 Bot", value=f"{user.bot}")
        embedWho.add_field(name="🗽 User Status", value=f"{users_status} | {emoji_status}")
        embedWho.add_field(name="🆔 User ID", value=f'{user.id}')
        embedWho.add_field(name='🗿 Roles', value=f'{roles}', inline=False)
        embedWho.set_footer(text=f"Requested by {ctx.author}", icon_url=f"{ctx.author.avatar_url}")
        embedWho.set_thumbnail(url=f"{user.avatar_url}")
        await ctx.send(embed=embedWho)

#---------------------------------------------------------------------#
#STATS COMMAND
#---------------------------------------------------------------------#

    @commands.command(aliases=['info'])
    async def stats(self, ctx):
        pythonVersion_1 = sys.version_info
        pythonVersion = f"{pythonVersion_1.major}.{pythonVersion_1.minor}.{pythonVersion_1.micro}"
        dpyVersion = discord.__version__
        PILVersion = PIL.__version__
        dpycompVersion = discord_components.__version__
        PsutilVersion = psutil.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(self.client.users)
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-self.client.startTime))))
        botLatency = round(self.client.latency * 1000)


        settings = "<:settings:880806862348484678>"
        sound = "<:sound:880806862239461417>"
        info = "<:info:880806862411419689>"
        stats = "<:stats:880806862419791893>"
        check = "<:check:880806862293958736>"

        embedStats = discord.Embed(title='AloX STATS',color = 3447003, description= f"""
        **General Statistics**‎‎‎‎‎‎‎
        {info} Servers: `{serverCount}`
        👥 Members: `{memberCount}`
        📞 Bot Prefix's: `"," and "al." and "AL."`
        {stats} Bot Version: `{self.client.BotVersion}`
        {check} Bot Latency : `{botLatency}ms`""", inline=True)

        embedStats.add_field(name="**Modules & Python**", value=f"""
        💬 Discord Version: `{dpyVersion}`
        🐍 Python Version: `{pythonVersion}`
        🛌 Pillow Version: `{PILVersion}`
        〽 Disc-Comp Version: `{dpycompVersion}`
        💻 Psutil Version: `{PsutilVersion}`""", inline=True)

        embedStats.add_field(name='**Computer Usage**', value=f"""
        {info} CPU Usage: `{psutil.cpu_percent()}%`
        {info} RAM Usage: `{psutil.virtual_memory().percent}%`
        {check} Uptime: `{uptime}`""", inline=True)

        embedStats.add_field(name='**Description**',value="""
        `AloX is a multipurpose yet unique bot, made specifically with the user in mind. Its been coded with hours of hard work from our dev team!. AloX is a top bot!`
        """,inline=False)

        button_stats= [Button(style=ButtonStyle.URL, label = "JOIN MY SUPPORT SERVER!",url=f'https://dsc.gg/alox')]
        embedStats.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Emoji_u1f4c8.svg/768px-Emoji_u1f4c8.svg.png')
        await ctx.send(embed=embedStats, components = button_stats )

#---------------------------------------------------------------------#
#PURGE COMMAND
#---------------------------------------------------------------------#

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount : int):
            await ctx.channel.purge(limit=amount+1)
            embedPurge = discord.Embed(title='Purged Messages', description=f'Purged {amount} Messages', color = 3447003)
            embedPurge.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")
            await ctx.send(embed=embedPurge, delete_after=2)

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You cant use that!")

#---------------------------------------------------------------------#
#SAY COMMAND
#---------------------------------------------------------------------#

    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def say(self, ctx, *words):
        await ctx.message.delete()
        words = " ".join(words[:])
        await ctx.send(f'{words}')

#---------------------------------------------------------------------#
#DEV-LOG COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def dev(self, ctx):
        embedDev = discord.Embed(title=f'Dev Logs: `{self.client.BotVersion}`', description=f"""
        __**Whats happened / happening in Version {self.client.BotVersion}?**__
        **1)** Code Clean Up | Done?: ✅
        **2)** Add another Image Maniupulation command | Done?: ✅ (textimg)
        **3)** Add Errors for each command | Done?: ✅
        **4)** Brainstorm more ideas for commands | Done?:❌
        **5)** Fix up whois? command | Done?: ✅ (Merged with status)
        **6)** Fix up avatar with buttons? | Done?: ✅
        **7)** Make all image manipulation commands in embeds | Done?: ✅
        **8)** Fix the uptime command and make the AFK command | Done?: ✅
        **9)** Use buttons for as many commands as possible | Done?: ❌
        """, color = 3447003)
        embedDev.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLSM0lHH8K_ftDVzpcSgii4uS5uZ0-TQMlSwvz0T=s900-c-k-c0x00ffffff-no-rj')
        embedDev.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author}")
        await ctx.send(embed=embedDev)

#---------------------------------------------------------------------#
#UPTIME COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def uptime(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-self.client.startTime))))
        embedUptime = discord.Embed(title='UPTIME', description=f'{uptime}', color = 3447003)
        embedUptime.set_thumbnail(url='https://cdn.iconscout.com/icon/free/png-512/downtime-1851050-1569037.png')
        await ctx.send(embed=embedUptime)

#---------------------------------------------------------------------#
#COIN-FLIP COMMAND
#---------------------------------------------------------------------#

    @commands.command()
    async def coin(self, ctx):
        coin_outputs = ["Heads", "Tails"]
        embedCoin = discord.Embed(title = 'Coin Flip', description=f'{random.choice(coin_outputs)}', color = 3447003)
        embedCoin.set_thumbnail(url='https://i.pinimg.com/originals/66/14/8f/66148fb9fe7ad469c5049a02e6a5c2ac.png')
        embedCoin.set_footer(icon_url=ctx.author.avatar_url, text = f"Requested by {ctx.author }")
        await ctx.send(embed=embedCoin)

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(misc_alox(client))

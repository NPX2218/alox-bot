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

#---------------------------------------------------------------------#
#SETTING THE COG
#---------------------------------------------------------------------#

class tict_alox(commands.Cog):
    def __init__(self, client):
        self.client = client


#---------------------------------------------------------------------#
#TIC-TAC-TOE COMMAND
#---------------------------------------------------------------------#
    
    global checkWinner
    global winningConditions
    global gameOver
    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True
    board = []
    #DEFINING THE WINNING CONDITIONS
    winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    #WHEN THE USER STARTS THE COMMAND
    @commands.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member = None):
        if p2 == None:
            p2 = ctx.author
        if p1 == p2:
            await ctx.channel.send("Mention another player that isn't yourself to play against!")
        global count
        global player1
        global player2
        global turn
        global gameOver
        

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            # print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + board[x]

            #DETERMING WHO GOES FIRST
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("<@" + str(player1.id) + "> is starting.")
            elif num == 2:
                turn = player2
                await ctx.send("<@" + str(player2.id) + "> is starting.")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")

    #COMMAND IF THE GAME IS ACTIVE THEN:
    @commands.command()
    async def place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
                    checkWinner(winningConditions, mark)
                    if gameOver == True:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")

                    #SWITCHING TURNS
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the al.tictactoe command.")

    #CHECKING THE WINNER 
    def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

    #IF THE USER USES THE COMMAND IN A WRONG WAY
    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention another player for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@58102844835784294523>).")

    #IF THE USER PLACES IN THE WRONG PLACE
    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")

#---------------------------------------------------------------------#
#ADDING THE COG
#---------------------------------------------------------------------#

def setup(client):
    client.add_cog(tict_alox(client))
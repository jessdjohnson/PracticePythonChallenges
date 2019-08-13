# -*- coding: utf-8 -*-
"""
Challenge 27: Tic Tac Toe Draw
For prompt, visit: https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

Goal: Check if someone has won a game of tic tac toe.

Jess Johnson, 08/13/2019
"""
import random
   
def initializeGame():
    game = [[0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]]
    return game


def nextMove(player, game):
    print('Player ' + str(player) +'\'s turn. Please input row, col values for where you would like to play then press return.')
    inputs = [int(x) for x in input().split(', ')]
    game[inputs[0]][inputs[1]] = player
    return game


def checkForWin(board):
    #check rows
    winner = 'none'
    for i in range(0,3):
        if (board[i][0] == board[i][1]== board[i][2]):
            winner = board[i][0]

    #check columns
    for i in range(0,3):
        if (board[0][i] == board[1][i]== board[2][i]):
            winner = board[0][i]
            
    #check crosses
    if (board[0][0] == board[1][1]== board[2][2]):
        winner = board[0][0]

    if (board[2][0] == board[1][1]== board[0][2]):
        winner = board[2][0]    

    if winner == 0 or winner == 'none':
        print('There is no winner')
        winner = 'none'
    else: 
        print('Winner is: ' + str(winner))

    return winner


if __name__ == "__main__":
    winner = 'none'
    #choose random first player
    player = random.randint(1,3)
    game = initializeGame()
    
    while winner == 'none':
        player = ((player+2)%2)+1 #next player
        game = nextMove(player, game) #get next move from player and put onto board
        winner = checkForWin(game) #check for a win.

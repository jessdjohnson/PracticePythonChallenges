# -*- coding: utf-8 -*-
"""
Challenge 26: Check Tic Tac Toe
For prompt, visit: https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

Goal: Check if someone has won a game of tic tac toe.

Jess Johnson, 08/13/2019
"""

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
        winner = 0
    else: 
        print('Winner is: ' + str(winner))

    return winner
    
if __name__ == "__main__":
    game = [[1, 2, 0], 
            [2, 1, 0],
            [2, 1, 1]]
    winner = checkForWin(game)

    winner_is_2 = [[2, 2, 0],
    	[2, 1, 0],
    	[2, 1, 1]]
    winner = checkForWin(winner_is_2)

    winner_is_1 = [[1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 1]]
    winner = checkForWin(winner_is_1)

    winner_is_also_1 = [[0, 1, 0],
    	[2, 1, 0],
    	[2, 1, 1]]
    winner = checkForWin(winner_is_also_1)

    
    no_winner = [[1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 2]]
    winner = checkForWin(no_winner)
    
    also_no_winner = [[1, 2, 0],
    	[2, 1, 0],
    	[2, 1, 0]]
    winner = checkForWin(also_no_winner)

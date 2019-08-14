# -*- coding: utf-8 -*-
"""
Challenge 29: Tic Tac Toe Game
For prompt, visit: https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

Goal: Check if someone has won a game of tic tac toe.

Jess Johnson, 08/13/2019
"""
import random
   
def initializeGame():
    game = [[0, 0, 0], 
            [0, 0, 0],
            [0, 0, 0]]
    return game


def nextMove(player, game, moves):
    if moves != 9:        
        print('Player ' + str(player) +'\'s turn. Please input row, col values for where you would like to play then press return.')
        inputs = [int(x) for x in input().split(', ')]
        counter = 0
        while (game[inputs[0]][inputs[1]] != 0) and (counter < 50):
            print('The selected space is already occupied.  Please pick again')
            print('Player ' + str(player) +'\'s turn. Please input row, col values for where you would like to play then press return.')
            inputs = [int(x) for x in input().split(', ')]
            counter += 1
            
        if counter != 49:
            game[inputs[0]][inputs[1]] = player
        else:
            print('Player ' + str(player) + ' forfeited their turn by repeatedly selecting taken spaces.')
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

def printGameboard(game):
    horizontal_size = 3
    
    base_h = ' ---'
    base_v = '|   '    
    horizontal_line = base_h*horizontal_size + ' '
    lines = []
    for i in range(0,3):
        lines.append(horizontal_line) 
        this_line = ''
        for j in range(0,3):
            if game[i][j] == 0:
                next_space = base_v
            elif game[i][j] == 1:
                next_space = '| X '
            elif game[i][j] == 2:
                next_space = '| O '
            else:
                print('Error')
            this_line = this_line + next_space
        lines.append(this_line)
    lines.append(horizontal_line)
    
    print('Current Board: ')
    for i in lines:
        print(i)
        

if __name__ == "__main__":
    winner = 'none'
    #choose random first player
    player = random.randint(1,3)
    game = initializeGame()
    moves = 0
    while (winner == 'none'):
        if (moves < 10):
            player = ((player+2)%2)+1 #next player
            moves += 1
            game = nextMove(player, game, moves) #get next move from player and put onto board
            winner = checkForWin(game) #check for a win.
            printGameboard(game) 
        else:
            winner = 'no winner'
            print('The game is a stalemate!')
        
# -*- coding: utf-8 -*-
"""
Challenge 24: Draw a game board
For prompt, visit: hthttps://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

Goal: Draw the following:
     --- --- --- 
    |   |   |   | 
     --- --- ---  
    |   |   |   | 
     --- --- ---  
    |   |   |   | 
     --- --- --- 
Jess Johnson, 08/12/2019
"""

def printGameboard(horizontal_size,vertical_size):
    base_h = ' ---'
    base_v = '|   '
    horizontal_line = base_h*horizontal_size + ' '
    vertical_line = base_v*horizontal_size + '|'
    
    lines = []
    for i in range(0,vertical_size):
        lines.append(horizontal_line)
        lines.append(vertical_line)
    lines.append(horizontal_line)
    
    print(str(horizontal_size) + ' x ' + str(vertical_size) + ' Board: ')
    for i in lines:
        print(i)

def getUserBoardSize():
    print('What size board would you like to see?  Please input a horizonal size followed by a space and then the vertical size.  Press return when done.')
    input_list = [int(x) for x in input().split(' ')]
    return input_list[0], input_list[1]

if __name__ == "__main__":
    print('Sample Boards:')
    printGameboard(3,3)      
    printGameboard(8,8)      
    printGameboard(3,4)
    
    x,y = getUserBoardSize()
    printGameboard(x,y)
    

      

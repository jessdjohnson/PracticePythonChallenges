# -*- coding: utf-8 -*-
"""
Challenge 8: Rock Paper Scissors
For prompt, visit: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
 
Goal: Make a two-player Rock-Paper-Scissors game.  

Jess Johnson, 08/09/2019
"""

def getRPS(player_num):
    print("Player " + str(player_num) + " please input an r for rock, p for paper, or s for scissors.")
    rps = input().strip('\n')
    if (rps == 'r') or (rps == 'p') or (rps == 's'):
        return rps
    else:
        return ' '

if __name__ == '__main__':
    done = False
    while (done == False):
        print()
        user1= getRPS(1)
        user2 = getRPS(2)
        
        #rock beat scissors
        if (user1 == ' ') or (user2 == ' '):
            print('\nOne of the input arguments was invalid, please try again.')
        elif ((user1 == 'r') and (user2 == 'r')) or ((user1 == 's') and (user2 == 's')) or ((user1 == 'p') and (user2 == 'p')):
                print('\nTie, please play again.')
        elif ((user1 == 'r') and (user2 == 's')) or ((user1 == 's') and (user2 == 'p')) or ((user1 == 'p') and (user2 == 'r')):
            print('\nPlayer 1 wins! ' + user1 + ' beats ' + user2)
        else:
            print('\nPlayer 2 wins! ' + user2 + ' beats ' + user1)
            
        #scissors beats paper
        
        # paper beats rock
        print("\nIf you are done playing rock paper scissors, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True      
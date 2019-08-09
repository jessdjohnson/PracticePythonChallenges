# -*- coding: utf-8 -*-
"""
Challenge 9: Guessing Game One
For prompt, visit: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
 
Goal: Generate a random number in [1,9]. Ask user to guess the number, then tell them too low, too high or right.
Extra: Keep track of how many guesses. 

Jess Johnson, 08/09/2019
"""
import random

def getGuess():
    print('Guess a number 1-9 and press enter:')
    num = int(input().rstrip('\n'))
    return num

if __name__ == '__main__':
    true_number = random.sample(range(1,9), k = 1)
    true_number = true_number[0]
    guess_counter = 0
    done = False
    while (done == False):
        number = getGuess()
        guess_counter += 1
        
        if number < true_number:
            print('Too Low.')
        elif number > true_number: 
            print('Too High.')
        else: 
            print('Just right! That took you ' + str(guess_counter) + ' guesses.')
            done = True      

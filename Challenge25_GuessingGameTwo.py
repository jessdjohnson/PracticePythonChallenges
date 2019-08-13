# -*- coding: utf-8 -*-
"""
Challenge 25: Guessing Game Two
For prompt, visit: https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html

Goal: User has a number between 0, 100 in mind, program guesses number.  User says too high, too low, or your number. 
Program prints out how many guesses to get the number.  

Note: Binary search will obviously be the optimal way to search.... to stealing that from exercise. 20
Jess Johnson, 08/13/2019
"""
import math

def generateGuess(guesses, high_low):
    if high_low == 'h':
        #select mid-point, last-guess to R
         guesses = [guesses[0], math.floor((guesses[0]+guesses[1])/2), guesses[1]]       
    elif high_low == 'l': 
        #select mid-point, last guess to L
         guesses = [guesses[1], math.floor((guesses[1]+guesses[2])/2), guesses[2]]    
    else:
        print('I guessed right! Yay!')        
    return guesses

def checkGuess(guesses):
    guessed_right = False
    print('Was your number: ' + str(guesses[1]) + '?')
    print('If I pick too high, enter "high".  If I pick too low, enter "low".  If I guess right, press return!')
    user_response = input()
    high_low = ''
    if user_response == 'high':
        high_low = 'h'
        print("Okay, I guessed too high, let's try again.")
    elif user_response == "low":
        print("Okay, I guessed too low, let's try again.")
        high_low = 'l'
    else:
        guessed_right = True        
    return guessed_right, high_low


if __name__ == "__main__":
    print('Pick a number between 0 and 100.  I will guess your number.')
    print("Let's see how many guesses it takes me.\n")
    
    guessed_right = False
    num_guesses = 1
    guesses = [0, 50, 101]
    guessed_right, high_low = checkGuess(guesses)
   
    while guessed_right != True:
        guesses = generateGuess(guesses, high_low)
        guessed_right, high_low = checkGuess(guesses)
        num_guesses += 1
        
    print('Your number was: ' +str(guesses[1]) + '. I got it in ' + str(num_guesses) + ' guesses.')
    

      

# -*- coding: utf-8 -*-
"""
Challenge 18: Cows and Bulls
For prompt, visit: https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html

Goal: Create program to play "cows and bulls".

Jess Johnson, 08/12/2019
"""
import random

def getCowsAndBulls(rand_num, user_guess):
    str_rand = str(rand_num).zfill(4)
    str_user = str(user_guess).zfill(4)
    
    num_cows = 0       
    num_bulls = 0
    for index, char in enumerate(str_rand):
        if (char == str_user[index]):
                num_cows += 1      
        else:
            for index2,char2 in enumerate(str_user):
                if (index != index2) and (char == char2):
                    num_bulls += 1
                    break
    
    return num_cows, num_bulls

def getUserNum():
    print("Guess a 4 digit number and then press enter:")
    num = int(input())
    return num

def getRandomNum():
    number = random.randint(0, 10000)
    return number

if __name__ == "__main__":
    comp_num = getRandomNum()
    cows = 0
    bulls = 0
    guesses = 0
    print("Welcome to a game of Cows and Bulls.  Try to guess the four digit number I'm thinking of.")
    print("I will give you a cow for every number you guess that is a right number in the right position and bull for every digit that's part of my number but that you put in the wrong location.")
    print("Let's play!")
    while cows != 4:
        guesses += 1
        user_num = getUserNum()
        cows, bulls = getCowsAndBulls(comp_num, user_num)
        print("Cows: " + str(cows) + ", Bulls: " + str(bulls))
    print("Congrats, you found the number! It took you " + str(guesses) + " guesses.")
    
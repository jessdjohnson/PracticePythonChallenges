# -*- coding: utf-8 -*-0
"""
Challenge 2: Odd or Even
For prompt, visit:https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Goal: Ask user for a number. Print a message to the user telling them if it's odd or even.

Jess Johnson, 08/09/2019
"""

def getNum():
    print('Please input an integer number and press return:')
    num = int(input())
    return num

def isOdd(num):
    if (num%2 == 1):
        odd = True
    else:
        odd = False
        
    return odd

if __name__ == '__main__':    
    done = False
    while done == False:
        
        number = getNum()
        odd = isOdd(number)
        if odd:
            print('Your number is odd.')
        else:
            print('Your number is even.')
        
        print("If you are done testing numbers, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True
            

        
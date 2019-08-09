# -*- coding: utf-8 -*-
"""
Challenge 13: Fibonacci
For prompt, visit: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Goal: Ask user for a number and generate fibonnachi sequence of that length.
    
Jess Johnson, 08/09/2019
"""


def getNum():
    print("Please length of Fibonnaci sequence you'd like to see.")
    num = int(input())
    return num

def getFibonnaciSequence(user_number):
    fibonnaci = []
    if user_number >= 1:
        fibonnaci.append(1)
    if user_number >= 2:
        fibonnaci.append(1)
        for i in range(2, user_number):
            fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
    return fibonnaci

if __name__ == '__main__':
    done = False
    while (done == False):
        user_number = getNum()
        fibonnaci = getFibonnaciSequence(user_number)
        
        print('Your fibannaci sequence of length '+ str(user_number) + ' is as follows:')
        print(fibonnaci)

        print("\nIf you are done looking at Fibonnaci sequences, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True            


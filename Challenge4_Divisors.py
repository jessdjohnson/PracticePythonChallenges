# -*- coding: utf-8 -*-
"""
Challenge 4: Divisors
For prompt, visit: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Goal:Create a program that asks the user for a number and prints out a list of the divisors of that number.
    
Jess Johnson, 08/09/2019
"""

def getNum():
    print("Please input an integer number you'd like to know the divisors of.")
    num = int(input())
    return num

if __name__ == '__main__':
    done = False
    while (done == False):
        user_number = getNum()
        
        divisors = []
        for i in range(1, user_number):
            if (user_number%i == 0):
                divisors.append(i)

        if (len(divisors) == 1):
            print("\nYou've found a prime number! The only divisor of " + str(user_number) + " is the number 1.")
        else:
            print('\nDivisors of ' + str(user_number) + ' are:')
            print(divisors)
            
        print("\nIf you are done testing numbers, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True            
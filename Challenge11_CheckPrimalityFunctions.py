# -*- coding: utf-8 -*-
"""
Challenge 11: Check Primality Functions
For prompt, visit: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

Goal: Ask the user for a number and determine whether the number is prime or not....
(I DID THIS ALREADY IN challenge 4.... so....this is the same code modified to just return prime or not prime.)
    
Jess Johnson, 08/09/2019
"""

def getNum():
    print("Please input an integer number you'd like to test the primality of.")
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
            print("\nThe number you've entered is not prime.  It's divisors are " + str(user_number) + ' are:')
            print(divisors)
            
        print("\nIf you are done testing numbers, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True      


# -*- coding: utf-8 -*-
"""
Challenge 3: List Less Than Ten
For prompt, visit: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html\

Goal: Create a program that has a list and prints out all the elements of the list that are less than 5.

Extras: Ask the user for a number and returns a list with only elements smaller than that given number

Jess Johnson, 08/09/2019
"""

def getNum():
    print('Please input an integer number for testing or press return for the default value of 5:')
    num = input()
    if num == '':
        num = 5
    else:
        num = int(num)
    return num
    
if __name__ == '__main__':
    
    print('Original List:')
    print(numbers)
    
    numbers =[1, 1, 2, 3, 5, 13, 21, 34, 55, 89]
    user_number = getNum()
    
    
    print('\nNumbers in list less than ' + str(user_number) + ':')
    for num in numbers:
        if num < user_number:
            print(num)
            
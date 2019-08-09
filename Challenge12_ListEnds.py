# -*- coding: utf-8 -*-
"""
Challenge 12: List Ends
For prompt, visit: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

Goal: Write a program that takes a list of numbers and makes a new list of only the first and last element of the list.  Code must be inside a function.

Jess Johnson, 08/09/2019
"""

def returnFirstLast(input_list):
    return input_list[0], input_list[-1]

def getList():
    print('Please input a list of space separated integers.  When done, press return.')
    input_list = list(map(int, input().rstrip('\n').split(' ')))        
    return input_list

if __name__ == '__main__':
    user_list = getList()
    print('Your list was: ')
    print(user_list)
    
    first, last = returnFirstLast(user_list)
    print('The first element of the list was: ' + str(first))
    print('The last  element of the list was: ' + str(last))
    
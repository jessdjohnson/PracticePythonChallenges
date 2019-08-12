# -*- coding: utf-8 -*-
"""
Challenge 20: Element Search
For prompt, visit: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

Goal: Write a function that takes an ordered list of numbers and another number and decides whether the number is in the list and returns a boolean

Extras: use binary search

Jess Johnson, 08/12/2019
"""

import math

def getList():
    print('Please input an ordered list of space separated numbers and press enter.')
    input_list = [int(x) for x in input().split(' ')]
    return input_list

def getNumber():
    print("Please input a number you'd like to check the list for and press enter.")
    number = int(input())
    return number

def slowSearch(number, input_list):
    in_list = False
    checked = 0
    while ((in_list == False) and checked < len(input_list)):
        if input_list[checked] == number:
            in_list = True
        else:
            checked += 1
            
    return in_list

def binarySearch(number, input_list):
    L = 0
    R = len(input_list)-1
    while L <= R:
        #print('L' + str(L))
        #print('R' + str(R))
        m = math.floor((L+R)/2)
        #print('m' + str(m) + '\n')
        if input_list[m] < number:
            L = m+1
        elif input_list[m] > number:
            R = m-1
        else:
            return m
    return False

if __name__ == "__main__":
    input_list = getList()
    number = getNumber()
    
    #in_list = slowSearch(number, input_list)
    
    in_list = binarySearch(number, input_list)
    
    if in_list:
        print('The number ' + str(number) + ' is in the list.')
    else:
        print('The number ' + str(number) + ' is NOT in the list.')

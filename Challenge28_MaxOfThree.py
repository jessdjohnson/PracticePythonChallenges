# -*- coding: utf-8 -*-
"""
Challenge 28: Max of Three
For prompt, visit: https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

Goal: Implement a function that takes as an input three variables and returns the largest of the three (without the max function)!

Jess Johnson, 08/13/2019
"""

def maxFun(a,b,c):
    
    our_list = [a, b, c]
    maximum = float("-inf")
    for i in our_list:
        if i > maximum:
            maximum = i
    return maximum

if __name__ == "__main__":
    maximum = maxFun(3, 6, 82)
    print("The maximum value was " + str(maximum))
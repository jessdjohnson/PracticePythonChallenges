# -*- coding: utf-8 -*-
"""
Challenge 15: Reverse Word Order
For prompt, visit: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Goal: Take in a string containing multiple words, print back the same string with work order reversed.

Jess Johnson, 08/09/2019
"""

def getString():
    print('Please input a string of space separated words then press return:')
    string = input().rstrip('\n').split(' ')
    return string

if __name__ == "__main__":
    user_string = getString()
    reverse_string = user_string[::-1]
    result = ' '.join(reverse_string)
    print(result)



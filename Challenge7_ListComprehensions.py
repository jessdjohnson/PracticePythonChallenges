# -*- coding: utf-8 -*-
"""
Challenge 7: List Comprehensions
For prompt, visit:https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
 
Goal: Create a single line of python that takes a list and makes a new list with only the even elements in it.

Jess Johnson, 08/09/2019
"""

a = [1,4,9,16,25,36,49,64,81, 100]
b = [elem for elem in a if (elem%2 == 0)]
print(b)
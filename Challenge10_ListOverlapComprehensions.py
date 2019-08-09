# -*- coding: utf-8 -*-
"""
Challenge 10: List Overlap Comprehensions
For prompt, visit: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
 
Goal: Generate a random number in [1,9]. Ask user to guess the number, then tell them too low, too high or right.
Extra: Keep track of how many guesses. 

Jess Johnson, 08/09/2019
"""

import random

def repeatForNewLists():
    list_lengths = range(16)
    len_a = random.sample(list_lengths, k=1)
    len_b = random.sample(list_lengths, k=1)
    len_a = len_a[0]
    len_b = len_b[0]

    population = range(26)
    a = random.sample(population, k=len_a)
    b = random.sample(population, k=len_b)
    
    common_elements = [elem_a for elem_a in a for elem_b in b if elem_a == elem_b]
    
    print('\nRandomly generated lists with values in [0, 25]:')
    print('\nList A:')
    print(a)
    print('\nList B:')
    print(b)
    print('\nCommon elements:')
    if (len(common_elements) == 0):
        print('Lists have no common elements.')
    else:
        print(common_elements)
    
if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    common_elements = [elem_a for elem_a in a for elem_b in b if elem_a == elem_b]
    
    print('Default Lists:')
    print('\nList A:')
    print(a)
    print('\nList B:')
    print(b)
    print('\nCommon elements:')
    print(common_elements)
    
    done = False
    while (done == False):
        repeatForNewLists()
        
        print("\nIf you are done generating lists, input 'y' otherwise press any key to continue.")
        user_input = input('').split(" ")[0]
        if (user_input == 'y'):
            done = True     
            
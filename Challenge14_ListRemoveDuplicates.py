# -*- coding: utf-8 -*-
"""
Challenge 14: List Remove Duplicates
For prompt, visit: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

Goal: Write a function that takes a list and returns a new list that contains all the elements of the first list minus duplicates.

Extras: write this with a loop and write it with sets.

Jess Johnson, 08/09/2019
"""

def deduplicate_using_lists(input_list):
    output_list = []
    for elem in input_list:
        if elem not in output_list:
            output_list.append(elem)   
    return output_list

def deduplicate_using_sets(input_list):
    output_list = list(set(input_list))
    return output_list
  
def getList():
    print('Please input a list of space separated integers.  When done, press return.')
    input_list = list(map(int, input().rstrip('\n').split(' ')))        
    return input_list

if __name__ == '__main__':
    user_list = getList()
    print('Your list was: ')
    print(user_list)
    
    dedupped = deduplicate_using_lists(user_list)
    print('Your deduplicated list (using loops) is: ')
    print(dedupped)

    dedupped_sets = deduplicate_using_sets(user_list)
    print('Your deduplicated list (using sets) is: ')
    print(dedupped_sets)
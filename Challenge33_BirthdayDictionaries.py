# -*- coding: utf-8 -*-
"""
Challenge 33: Birthday Dictionaries
For prompt, visit: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

Goal: Part 1 of 4. Create a dictionary of names and birthdays.  

Jess Johnson, 08/14/2019
"""

def getBirthday(name):
    if name in dictionary:
        birthday = dictionary[name]
    else:
        birthday = ''
    return birthday

def getDictionary():
    dictionary = {'Albert Einstein': '03/14/1879',
            'Benjamin Franklin': '01/17/1706',
            'Ada Lovelace': '12/10/1815',
            'Donald Trump': '06/14/1946',
            'Rowan Atkinson': '01/6/1955'}
    return dictionary

def getUserRequestedName():
    print("Who's birthday do you want to look up? Enter a name and press return.")
    name = input()
    return name

if __name__ == "__main__":    
    print('Welcome to the birthday dictionary.  We know the birthdays of:')
    dictionary = getDictionary()
    names = dictionary.keys()
    for name in names:
        print(name)
    name = getUserRequestedName()
    birthday = getBirthday(name)
    if birthday == '':
        print('We do not have ' + name + "'s birthday.")
    else:
        print(name + "'s birthday is " + birthday)

    
    

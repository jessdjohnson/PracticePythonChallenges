# -*- coding: utf-8 -*-
"""
Challenge 34: Birthday JSON
For prompt, visit: https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

Goal: Part 2 of 4. Load birthday dictionary from JSON

Jess Johnson, 08/14/2019
"""

import json

def loadDictionaryFromJSON(filename):
    with open(filename, "r") as f:
        dictionary = json.load(f)
    return dictionary


def getDictionary():
    dictionary = {'Albert Einstein': '03/14/1879',
            'Benjamin Franklin': '01/17/1706',
            'Ada Lovelace': '12/10/1815',
            'Donald Trump': '06/14/1946',
            'Rowan Atkinson': '01/6/1955'}
    return dictionary

def writeDictionaryToJSON(dictionary):
    filename = "birthdays_Challenge34.json"
    with open(filename, "w") as f:
        json.dump(dictionary, f)
    print('Wrote birthdays into: ' + filename)
    return filename
if __name__ == "__main__":
    dictionary = getDictionary()
    json_file = writeDictionaryToJSON(dictionary)
    print('Original Dictionary:')
    print(dictionary)
    
    print('\nCool beans.  Now let\'s reload that.')
    dictionary2 = loadDictionaryFromJSON(json_file)
    print('Dictionary from JSON:')
    print(dictionary2)
    
    print('Hey, they look the same.  Amazing!')
# -*- coding: utf-8 -*-
"""
Challenge 35: Birthday Months
For prompt, visit: https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

Goal: Part 3 of 4. Load birthday dictionary from JSON.  Extract months of birthdays. And count numbers per month.

Jess Johnson, 08/14/2019
"""
import json
from collections import Counter

def extractMonthCounts(dictionary):
    months_list = []
    for i in dictionary:
        temp = dictionary[i]
        months_list.append(temp[0:2])
    counts = Counter(months_list)
    
    return counts

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
    json_file = "birthdays_Challenge34.json"
    dictionary2 = loadDictionaryFromJSON(json_file)
    print('Dictionary from JSON:')
    print(dictionary2)
    
    month_counts = extractMonthCounts(dictionary2)
    print(month_counts)
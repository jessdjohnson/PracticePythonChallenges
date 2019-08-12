# -*- coding: utf-8 -*-
"""
Challenge 22: Read from File
For prompt, visit: https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

Goal: Given file with list of names, count the names in the file and print out results to screen.

Jess Johnson, 08/12/2019
"""
import collections

def getNameList():
    filename = "InputFile_Challenge22.txt"
    name_list = []
    with open(filename, 'r') as open_file:
        line = open_file.readline()
        while line:
            name_list.append(line.rstrip('\n'))
            line = open_file.readline()        
    return name_list
    
    
if __name__ == "__main__":
    
    text = getNameList()
    print(collections.Counter(text))
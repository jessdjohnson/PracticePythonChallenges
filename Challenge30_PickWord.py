# -*- coding: utf-8 -*-
"""
Challenge 30: Pick Word
For prompt, visit: https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

Goal: Part 1 of Hangman, write a function that picks a random word from a dictionary file .

Jess Johnson, 08/13/2019
"""
import random
import os
import linecache

def getWordFromFile():
    dictionary_length = 267751
    random_line_num = random.randint(1, dictionary_length+1)
    
    current_dir = os.getcwd()
    filename = current_dir + '\\' + 'dictionary_Challenge30.txt'
    
    word = linecache.getline(filename, random_line_num).rstrip('\n')
    return word

if __name__ == "__main__":
    word = getWordFromFile()
    print(word)
    
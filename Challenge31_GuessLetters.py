# -*- coding: utf-8 -*-
"""
Challenge 31: Guess Letters
For prompt, visit: https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

Goal: Part 2 of Hangman, Guessing letters of a word.  

Jess Johnson, 08/14/2019
"""

def guessLetter(letter, word, blank):
    temp = ''
    first_time = 0
    for index, char in enumerate(word):
        if (letter == char):
            if first_time == 0:
                print('Good guess! ' + char + ' is in the word')
                first_time = 1
            temp = temp + letter
        else:
            temp = temp + blank[index]
    if first_time == 0:
        print("I'm sorry, " + letter + " is not in the word.")
    blank = temp
    print(blank)
    return blank

def getLetter():
    print('Guess a letter and press return.')
    letter = input()
    return letter

if __name__ == "__main__":
    print('Welcome to Hangman!')
    word = 'TEST'
    blank = '_'*len(word)
    while blank != word:
        letter = getLetter()
        blank = guessLetter(letter, word, blank)
    print('You found the word. Great job!')
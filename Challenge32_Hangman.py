# -*- coding: utf-8 -*-
"""
Challenge 32: Hangman
For prompt, visit: https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

Goal: Part 3 of Hangman, putting it all together.  Players have 6 guesses (head, body, 2 legs, and 2 arms)


Jess Johnson, 08/14/2019
"""

import random
import os
import linecache

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
        add_a_guess = 1
        print("I'm sorry, " + letter + " is not in the word.")
    else:
        add_a_guess = 0
    blank = temp
    print(blank)
    return blank, add_a_guess

def getLetter(already_guessed, blank): 
    letter = ''
    while (letter == ''):
        print('Guess a letter and press return.')
        print('Here are your previous guesses:')
        print(already_guessed)
        letter = input()
        char = [char for char in already_guessed if (char == letter)]
        char2 = [temp for temp in blank if (temp == letter)]
        if (char != []) or (char2 != []):
            letter = ''
            print("You've already guessed that letter, try again.")
    return letter

def getWordFromFile():
    dictionary_length = 267751
    random_line_num = random.randint(1, dictionary_length+1)
    
    current_dir = os.getcwd()
    filename = current_dir + '\\' + 'dictionary_Challenge30.txt'
    
    word = linecache.getline(filename, random_line_num).rstrip('\n')
    return word

def addBodyPart(part, lines):
    
    if part == 'head':
        lines[2] = '    |     O'
    elif part == 'left_arm':
        lines[3] = '    |    ['
    elif part == 'body':
        lines[3] = '    |    [|'
    elif part == 'right_arm':
        lines[3] = '    |    [|]'
    elif part == 'left_leg':
        lines[4] = '    |    ⅃'
    elif part == 'right_leg':
        lines[4] = '    |    ⅃ L'
        lines.append("You've unfortunately been hanged.")
    else:
        print("please input a valid body  part")
    
    return lines

def createHangmanPlatform():

    lines = []
    lines.append('    _______    ')    
    lines.append('    |     |   ')
    lines.append('    |')
    lines.append('    |')
    lines.append('    |')
    lines.append('    |         ')
    lines.append('____|_________')
    return lines
    
def printPic(lines):
    for line in lines:
        print(line)
        
if __name__ == "__main__":
    
    for part in body_parts:
        lines = addBodyPart(part, lines)
        printPic(lines)
        print('\n')
        

if __name__ == "__main__":
    print('Welcome to Hangman!')
    print("I'm going to think of a word for you to guess. Guess letters one at a time.")
    print('Please enter capital letters.  You have up to 6 incorrect guesses before you get hanged.')
    word = getWordFromFile()
    blank = '_'*len(word)
    print('The word is ' + str(len(word)) + ' letters long.')
    print(blank)
    already_guessed = []
    num_guesses = 0
    lines = createHangmanPlatform()
    body_parts = ['head','left_arm','body','right_arm','left_leg','right_leg']

    while blank != word:
        if num_guesses < 6:
            letter = getLetter(already_guessed, blank)
            blank, add_a_guess = guessLetter(letter, word, blank)
            num_guesses += add_a_guess
            print('You have ' + str(6 - num_guesses) + ' remaining.')
            if add_a_guess:
                already_guessed.append(letter)
                lines = addBodyPart(body_parts[num_guesses-1], lines)
                printPic(lines)
                print('\n')
                
            if (blank == word):
                print('You found the word. Great job!')
        else:
            print("I'm sorry, you were unable to guess the word before being hanged.")
            print("The word was:")
            print(word)
            blank = word
            
    
 
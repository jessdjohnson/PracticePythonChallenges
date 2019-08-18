# -*- coding: utf-8 -*-
"""
Challenge 37: Draw Hangman

Goal:  Write function to add body parts to image of person being hung for hangman game

    ______
    |     |
    |     O
    |    [|]
    |    ⅃ L
    |
____|_________

Jess Johnson, 08/15/2019
"""

def addBodyPart(part, lines):
    
    if part == 'head':
        lines[3] = '    |     O'
    elif part == 'left_arm':
        lines[4] = '    |    ['
    elif part == 'body':
        lines[4] = '    |    [|'
    elif part == 'right_arm':
        lines[4] = '    |    [|]'
    elif part == 'left_leg':
        lines[5] = '    |    ⅃'
    elif part == 'right_leg':
        lines[5] = '    |    ⅃ L'
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
    lines = createHangmanPlatform()
    
    body_parts = ['head','left_arm','body','right_arm','left_leg','right_leg']
    for part in body_parts:
        lines = addBodyPart(part, lines)
        printPic(lines)
        print('\n')
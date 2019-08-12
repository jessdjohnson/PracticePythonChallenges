# -*- coding: utf-8 -*-
"""
Challenge 21: Write to a file
For prompt, visit: https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

Goal: Write something to a file.

Extras: Let the user select the filename.

Jess Johnson, 08/12/2019
"""

import os

def getFilename():
    your_dir = os.getcwd()
    print('Currently working in directory: ' + your_dir)
    
    print('\nPlease input the name of a file to write to and press return.')
    filename = input().rstrip('\n')
    
    print('\nNow writing to file: ' + your_dir + '/' + filename)
    filename = your_dir + '/' + filename
    return filename

if __name__ == "__main__":
    
    filename = getFilename()
    with open(filename, 'w') as open_file:
        open_file.write('A string to write')
        
    

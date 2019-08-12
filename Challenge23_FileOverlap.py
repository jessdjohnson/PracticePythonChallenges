# -*- coding: utf-8 -*-
"""
Challenge 23: File Overlap
For prompt, visit: https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

Goal: Given two .txt files with list of numbers in them, find the numbers that overlap.

Jess Johnson, 08/12/2019
"""
import os

def getList(filename):
    name_list = []
    with open(filename, 'r') as open_file:
        line = open_file.readline()
        while line:
            name_list.append(int(line.rstrip('\n')))
            line = open_file.readline()        
    return name_list
    
def getOverlaps(numbers1, numbers2):
    overlap = []
    for num  in numbers1:
        if num in numbers2:
            overlap.append(num)            
    return overlap
    
if __name__ == "__main__":
    current_dir = os.getcwd()
    filename1 = current_dir + "\\" + "InputFile1_Challenge23.txt"
    filename2 = current_dir + "\\" + "InputFile2_Challenge23.txt"

    numbers1 = getList(filename1)
    numbers2 = getList(filename2)
    overlaps = getOverlaps(numbers1, numbers2)

    print('Overlaps:')
    print(overlaps)
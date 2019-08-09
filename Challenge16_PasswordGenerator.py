# -*- coding: utf-8 -*-
"""
Challenge 16: Password Generator
For prompt, visit: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html

Goal: Write a password generator. Passwords should be random. 

Jess Johnson, 08/09/2019
"""
import random
import string


def getLength():
    print('Please input a desired password length and press return:')
    number = int(input())
    return number

def generateNewPassword(length):
    output = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(0, length)])
    return output

if __name__ == '__main__':    
    length = getLength()
    done = False
    while done == False:
        password = generateNewPassword(length)
        print("Your new password is: " + password)
        print('To generate again, press return, otherwise to quit, input q')
        happy = input()
        if happy == 'q':
            done = True
            



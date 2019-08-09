# -*- coding: utf-8 -*-
"""
Challenge 6: String Lists
For prompt, visit: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Goal: Ask user for a string.  Print out whether this string is a palindrome or not.
    
Jess Johnson, 08/09/2019
"""

def getWord():
    print("Please input word and we'll check to see if it's a palindrome!")
    word = input().rstrip('\n')
    return word

def isPalindrome(word):
    backward = word[::-1]
    
    if backward == word:
        print('Your word is a palindrome!')
        return True
    else:
        print('Nope, not a palindrome.')
        return False
    
        
if __name__ == '__main__':
    word = getWord()
    is_palindrome = isPalindrome(word)

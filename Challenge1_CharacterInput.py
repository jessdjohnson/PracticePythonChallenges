# -*- coding: utf-8 -*-
"""
Challenge 1: Character Input
For prompt, visit: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html\

Goal: Create a program that asks the user to enter their name and age. Print out
a message addressed to them that tells them the year that they will turn 100 years old.

Note: It bugged me that if I asked for age, the year that they turned 100 in would 
be wrong if they hadn't had their birthday yet, so I moded it to ask for birthday instead.

Jess Johnson, 08/09/2019
"""

import datetime

#Get name function
def getName():
    print('Please input your name and then press return:')
    name = input().rstrip('\n')
    return name

#Get age function
def getAge(name):
    #Get birthday info from cmdline
    print('Please input your birthday in the format MM/DD/YYYY and then press return:')
    bday = input().rstrip().split('/')
    birth_month = int(bday[0])
    birth_day = int(bday[1])
    birth_year = int(bday[2])

    #get info on today's date
    today = datetime.datetime.now()
    split_date = today.strftime("%m/%d/%Y").split('/')
    this_month = int(split_date[0])
    this_day = int(split_date[1])
    this_year = int(split_date[2])
    
    
    #calculate age 
    if (birth_month < this_month) or ((birth_month == this_month) and (birth_day < this_day)):
        #already had their birthday
        age = this_year - birth_year  
        print(age)
    elif ((birth_month == this_month) and (birth_day > this_day)):
        #birthday is this month, but still coming up
        age = this_year - birth_year - 1
        day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
        birth_day_of_year = (datetime.datetime(birth_year, birth_month, birth_day) - datetime.datetime(birth_year,1,1)).days + 1
        days_to_bday = birth_day_of_year - day_of_year
        print('You turn ' + str(age+1) + ' in ' + str(days_to_bday) + ' days. Happy Almost Birthday!')
    elif (birth_month == this_month) and (birth_day == this_day):
        #Birthday is today, sing happy birthday!
        age = this_year - birth_year
        print('\nHAPPY BIRTHDAY TO YOU.\nHAPPY BIRTHDAY TO YOU.\nHAPPY BIRTHDAY DEAR ' + name.upper() + '!\nHAPPY BIRTHDAY TO YOU!!')
    else: 
        #birthday is not this month, but later in the year.
        age = this_year - birth_year - 1
        print(age)

    return birth_year, age
    
def turnHundred(birth_year):
    turnHundredIn = birth_year + 100
    return turnHundredIn

    
if __name__ == '__main__':    
    name = getName()
    birth_year, age = getAge(name)
    year = turnHundred(birth_year)
    
    outputStr = '\nHi ' + name + '. You will turn 100 in the year ' + str(year) + '.\n'

    print(outputStr)
    
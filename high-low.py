#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:52:30 2020

@author: user
"""


'''
In this little assignment you are given a string of space separated 
numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, 
and highest number is first.
'''

def high_and_low(numbers):
    sort=[]
    x=numbers.split(' ')
    for i in x:
     sort.append(int(i))
    sort2=sorted(sort)
    
    return f'{sort2[-1]} {sort2[0]}'

print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"
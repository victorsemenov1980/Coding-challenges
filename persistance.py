#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:44:17 2020

@author: user
"""


'''
Write a function, persistence, that takes in a 
positive parameter num and returns its multiplicative 
persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.
 '''
import numpy as np
def persistence(n):
    result=0
    while len(str(n))!=1:
        digits=[int(d) for d in str(n)] 
        array=np.asarray(digits)
        n=np.prod(array)
        result+=1
        
    return result
     
print(persistence(39))
print(persistence(999))
print(persistence(4))
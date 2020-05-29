#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:07:52 2020

@author: user
"""


'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of 
digits should be considered.
'''
def increment_string(strng):
    import re
    out=''
    x=re.split('(\d+)',strng)
    
    if len(x)==1:
        out+=x[0]
        out+='1'
    else:
        out+=x[0]

        num="%%0%ii" % len(x[1]) % (int(x[1])+1)
       
        out+=str(num)
    
    return out

if increment_string("QwlgF N$5553809") == "QwlgF N$5553810":
    print('Passed')
if increment_string("foobar001")=="foobar002":
     print('Passed')
if increment_string("foobar1")=="foobar2":
     print('Passed')
if increment_string("foobar00")=="foobar01":
     print('Passed')
if increment_string("foobar99")=="foobar100":
     print('Passed')
if increment_string("foobar099")=="foobar100":
     print('Passed')
if increment_string("")=="1":
     print('Passed')
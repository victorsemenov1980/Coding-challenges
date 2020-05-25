#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:52:37 2020

@author: user
"""


'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''
import re

def order(sentence):
    result=''
    dict1={}
    res=sentence.split(' ')
    try:
        result=re.findall(r'\d',sentence)
        for i in range(len(res)):
            dict1[result[i]]=res[i]
        return ' '.join('{}'.format(val) for key, val in sorted(dict1.items()))
    except:
        return sentence
    

    

print(order("is2 Thi1s T4est 3a"))
print()
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print()
print(order(""))
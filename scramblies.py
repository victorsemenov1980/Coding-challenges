#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:01:30 2020

@author: user
"""


'''
Complete the function scramble(str1, str2) that returns true if a 
portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or 
digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.
Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''
def scramble(s1, s2):
    # your code here
    x=list(s1)
    counter=0
    
    for char in s2:
        if char in x:
            x.remove(char)
            counter+=1
    if counter==len(s2):
        return True
    else:
        return False
    
print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars') )
print(scramble('katas', 'steak'))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:38:54 2020

@author: user
"""
'''
Could be done in one-line expression, but if there is a function call, I see no point
as one-lineers still harder to read
'''

def disemvowel(string):
    vowels=['a','e','i','o','u'] #classic English vowels, 'y' not included
    dis=''
    for char in string:
        if char.lower() not in vowels: #lower to make it work with capitals
            dis=dis+char
        
    return dis

print(disemvowel("This website is for losers LOL!"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:01:43 2020

@author: user
"""


'''
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter 
words reversed (Just like the name of this Kata). Strings 
passed in will consist of only letters and spaces. Spaces 
will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(sentence):
    x=sentence.split(' ')
    result=''
    for i in x:
        if len(i)>=5:
            result+=i[::-1]
            result+=' '
        else:
            result+=i
            result+=' '
        
            
    return result.rstrip()

print(spin_words( "Hey fellow warriors" ))
print(spin_words( "This is a test"))
print(spin_words("This is another test" ))

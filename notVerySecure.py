#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:37:06 2020

@author: user
"""


'''
In this example you have to validate if a user 
input string is alphanumeric. The given string
 is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase
 latin letters and digits from 0 to 9
No whitespaces / underscore

("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
'''
def alphanumeric(password):

    return password.isalnum()



def alphanumeric(password):
    if password=='':
        return False
    else:
        import string
        x=string.ascii_lowercase
        y=string.ascii_uppercase
        z=[0,1,2,3,4,5,6,7,8,9]
        total=[]
        for i in x:
            total.append(i)
        for i in y:
            total.append(i)
        for i in z:
            total.append(str(i))
        counter=0
        for char in password:
            
            if char not in total:
                
                counter+=1
            else:
                counter+=0
        if counter!=0:
            return False
        else:
            return True
            
    
print(alphanumeric("hello world_"))
print(alphanumeric("PassW0rd"))
print(alphanumeric("     "))
print(alphanumeric(""))

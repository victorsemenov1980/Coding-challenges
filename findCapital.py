#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:36:04 2020

@author: user
"""


'''
Write a method that takes a sequence of objects  
with two keys each: country or state, and capital. 
Keys may be symbols or strings

The method should return an array of sentences 
declaring the state or country and its capital.

[{'state': 'Maine', 'capital': 'Augusta'}] 
--> ["The capital of Maine is Augusta"]

'''
def capital(capitals): 
    result=[]
    capital=''
    for i in capitals:
        try:
            state=i['state']
        except:
            state=i['country']
        city=i['capital']
        capital+=f'The capital of {state} is {city}'
        result.append(capital)
        capital=''
    return result
        

print(capital([{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}]))
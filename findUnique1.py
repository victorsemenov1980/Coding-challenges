#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:02:50 2020

@author: user
"""


'''
There is an array with some numbers. All numbers are equal except for one. 
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
'''

def find_uniq(arr):
    unique_list = [] 
    count=0
    for x in arr: 
       
        if x not in unique_list: 
            unique_list.append(x)
    for i in range(3): #we have condition about at least 3 entries in the arr
        if arr[i]==unique_list[0]:
            count+=1
    if count>1:
        return unique_list[1]
    else:
        return unique_list[0]
            
          
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print()
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))
print()
print(find_uniq([ 0, 1, 1 ]))
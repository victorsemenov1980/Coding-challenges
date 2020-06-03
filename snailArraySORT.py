#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:18:24 2020

@author: user
"""


'''
Snail Sort

Given an n x n array, return the array elements 
arranged from outermost elements to the middle 
element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow 
the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the 
lowest value to the highest; the idea is to traverse the 
2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en 
empty array inside an array [[]].
'''
#General idea is to make a recursive call and merge. ,
#get outer borders flat and call func for whatever left inside

def snail(snail_map):
    import numpy as np
    x = np.array(snail_map)
    def slicing(array):
        result=np.array
        result=x[0,:-1]
        result=np.append(result,x[:-1,-1])
        a=x[-1,:]
        # result=np.append(result,np.flip(x[-1,:]))
        result=np.append(result,a[::-1])
        b=x[:-1,0]
        # result=np.append(result,np.flip(x[:-1,0]))
        result=np.append(result,b[::-1])
        out=result[:-1]
        return out
    j=1
    z=slicing(x)
    while x[j:-j,j:-j].size>0:
        b=x[j:-j,j:-j]
        
        if b.size!=1:
            y=slicing(b)
            z=np.append(z,y)
        else:
            z=np.append(z,b)
            return z
            break
        
snail_map = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(snail_map))
snail_map = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(snail_map))

import numpy as np

def snail(array):
    m = []
    array = np.array(array)
    while len(array) > 0:
        m += array[0].tolist()
        array = np.rot90(array[1:])
    return m

snail_map = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(snail_map))
snail_map = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(snail_map))
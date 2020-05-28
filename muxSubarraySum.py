#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:41:27 2020

@author: user
"""


'''
The maximum sum subarray problem consists in finding the maximum sum 
of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive 
numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. 
Note that the empty list or array is also a valid sublist/subarray.
'''
def max_sequence(arr):
    result=[]
    test=[]
    max_val=0
    for j in range(len(arr)):
        # print(arr[j:])
        for i in arr[j:]:
            test.append(i)
            if sum(test)>max_val:
                max_val=sum(test)
                # result=test
        test=[]
    
    return max_val,test
    

arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sequence(arr))
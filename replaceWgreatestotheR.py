#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:38:31 2020

@author: user
"""


'''
Given an array arr, replace every element in that array with 
the greatest element among the elements to its right, and 
replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
'''
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result=[]
        max_val=-1
        for i in reversed(arr):
            
            
            result.append(max_val)
            if i>max_val:
                max_val=i
        result.reverse()
        return result

arr = [17,18,5,4,6,1]
y=Solution()
print(y.replaceElements(arr))












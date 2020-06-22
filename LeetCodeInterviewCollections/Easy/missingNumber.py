#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:54:10 2020

@author: user
"""


'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = 0
        sum2 = 0
        length = len(nums)
        
        for num in nums:
            sum1 += num
        for i in range (0, length + 1):
            sum2 += i
            
        return sum2 - sum1
            
     
y=Solution()
nums=[3,0,1]
print(y.missingNumber(nums))
nums=[9,6,4,2,3,5,7,0,1]
print(y.missingNumber(nums))
nums=[0]
print(y.missingNumber(nums))
nums=[0,2]
print(y.missingNumber(nums))
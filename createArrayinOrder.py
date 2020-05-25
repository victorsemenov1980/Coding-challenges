#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:32:10 2020

@author: user
"""


'''
Given two arrays of integers nums and index. 
Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at 
index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

 

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
Example 2:

Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
Example 3:

Input: nums = [1], index = [0]
Output: [1]
 

Constraints:

1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i
'''
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            result.insert(index[i],nums[i])
        return result
    
y=Solution()

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(y.createTargetArray(nums, index))
print()
nums = [1,2,3,4,0]
index = [0,1,2,3,0]
print(y.createTargetArray(nums, index))
print()
nums = [1]
index = [0]
print(y.createTargetArray(nums, index))
print()









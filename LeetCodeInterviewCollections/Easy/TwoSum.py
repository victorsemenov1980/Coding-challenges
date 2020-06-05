#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:02:49 2020

@author: user
"""


'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_dict = {}
        for i, v in enumerate(nums):
            x =  target - v  
            if x in hash_dict:
                return[hash_dict[x],i]
            else:
                hash_dict[v] = i
        
        
y=Solution()
nums = [2, 7, 11, 15]
target = 9
print(y.twoSum(nums, target))
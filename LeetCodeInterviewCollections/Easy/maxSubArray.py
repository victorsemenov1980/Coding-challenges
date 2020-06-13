#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 11:40:23 2020

@author: user
"""


'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding
 another solution using the divide and conquer approach, which is more subtle.
 '''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1] 
            max_sum = max(nums[i], max_sum)

        return max_sum

y=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(y.maxSubArray(nums))
nums=[-1]
print(y.maxSubArray(nums))
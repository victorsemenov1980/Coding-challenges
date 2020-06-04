#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:14:50 2020

@author: user
"""


'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect=[]
        import numpy as np
        x=np.intersect1d(nums1,nums2)
        for i in x:
            j = min(np.count_nonzero(nums1 == i),np.count_nonzero(nums2 == i))
            z=0
            while z<j:
                intersect.append(i)
                z+=1
            
        return intersect
y=Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(y.intersect(nums1, nums2))
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(y.intersect(nums1, nums2))
nums1 = [1,2]
nums2 = [1,1]
print(y.intersect(nums1, nums2))

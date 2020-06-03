#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:10:08 2020

@author: user
"""


'''
Given an integer array with no duplicates. A maximum tree building 
on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left 
part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right 
part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the 
root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:

The size of the given array will be in the range [1,1000].
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
root=TreeNode(10)
print(root)  
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 1:
                return TreeNode(nums[0])
        
        if(len(nums) == 0):
            return None
        
        max_ = max(nums)
        root = TreeNode(max_)
        idx = nums.index(max_)
        
        left = nums[:idx]
        right = nums[idx+1:]
        z=Solution()
        root.left = z.constructMaximumBinaryTree(left)
        root.right = z.constructMaximumBinaryTree(right)
        
        return root

y=Solution()
nums=[3,2,1,6,0,5]
print(y.constructMaximumBinaryTree(nums))
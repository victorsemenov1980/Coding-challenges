#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:51:52 2020

@author: user
"""


'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
        
    def insert(self, val):
# Compare the new value with the parent node
        if self.val:
            if val< self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    def PrintTree(self):
        print( self.val)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
# class Solution(object):
#     def isValidBST(self, root):
#        """
#         :type root: TreeNode
#         :rtype: bool\
#         """
       
#        INF = float("inf")
#        NEG_INF = float("-inf")

#        def dfs(node, lb, ub):
             
#              if not node:
#                  return True
             
#              return (lb < node.val < ub) and dfs(node.left, lb, node.val) and dfs(node.right, node.val, ub)

#        return dfs(root, NEG_INF, INF)
# y=Solution()
root=TreeNode(2)
root.insert(1)
root.insert(3)
# print(y.isValidBST(root))
root.PrintTree()






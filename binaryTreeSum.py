#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:03:11 2020

@author: user
"""


from binarytree import build 
from binarytree import tree, bst, heap
from binarytree import Node
'''
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        root=TreeNode()
        deepestSum = 0
        deepestDepth = 0
        q = [(root, deepestDepth)] #List[(TreeNode node, int depth)]
        while q:
            node, depth = q.pop(0)
            if depth > deepestDepth: #new depth attained, reset sum
                deepestDepth = depth
                deepestSum = 0
            deepestSum += node.val #add to sum of nodes at current depth
			
			# add node's children to queue
            if node.left:
                q.append((node.left,depth+1))
            if node.right:
                q.append((node.right,depth+1))
        return deepestSum
        
null=None
root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
y=Solution()
print(y.deepestLeavesSum(root))
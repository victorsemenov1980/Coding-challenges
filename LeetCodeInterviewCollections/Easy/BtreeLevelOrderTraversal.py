#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:34:38 2020

@author: user
"""


'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f'<{self.val}, {self.left}, {self.right}>' 
    
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, levels = [root] if root else [], []
        while q:
            levels.append([r.val for r in q if r])
            q = [c for r in q for c in [r.left, r.right] if c]
        return levels


from collections import deque
null=None
data = [3,9,20,null,null,15,7]
n = iter(data)
tree = TreeNode(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = TreeNode(next(n))
        fringe.append(head.left)
        head.right = TreeNode(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

# print(tree)

from binarytree import build
root=build(data)
print(root)
# print(root.values)
# print(root.levelorder)
for i in root.levelorder:
    print(i.values)
# print(root.properties)









        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:40:07 2020

@author: user
"""


'''
Write a function to delete a node (except the tail) in a singly linked 
list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the 
linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, 
the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a 
valid node of the linked list.
Do not return anything from your function.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
        

class Solution(object):
    
        
    def deleteNode(self, target_node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
    #as there is access ONLY to the taget node we need simply to copy all values of the next nodes
        #as everuy node has info only about itself and the next node
        node.val = node.next.val;
        node.next = node.next.next


head = [4,5,1,9]
y=Solution(head)
target_node = 5
print(y.deleteNode(target_node))
head = [4,5,1,9]
y=Solution(head)
target_node = 1
print(y.deleteNode(target_node))
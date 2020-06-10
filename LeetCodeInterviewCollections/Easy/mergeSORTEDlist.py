#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:04:48 2020

@author: user
"""


'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = None # Storage for first node
        prev = None  # Storage for previously selected node
        
		# While either node is not None
        while l1 or l2:
			# If both nodes not None
            if l1 and l2:
				# Select lower value node
                if l1.val < l2.val:
                    lower = l1
                    l1 = l1.next
                else:
                    lower = l2
                    l2 = l2.next
			# If only l1 is not None
            elif l1:
				# Select l1 as current node
                lower = l1
                l1 = l1.next
			# If only l2 is not None
            else:
				# Select l2 as current node
                lower = l2
                l2 = l2.next
            
			# If first hasn't been selected
            if not first:
				# Select current node as first
                first = lower
			# If previous node exists
            if prev:
				# Set current node as previous node's next
                prev.next = lower
			# Set previous to current node
            prev = lower
            
        return first # Returning first node
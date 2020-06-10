#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:01:20 2020

@author: user
"""


'''
Reverse linked list
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
    
        lst = lst[::-1]
        # construct a link list from the tail
        nxt = None
        while lst:
            val = lst.pop()
            node = ListNode(val)
            node.next = nxt
            nxt = node

        return(nxt)
        
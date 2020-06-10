#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:39:15 2020

@author: user
"""
'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''





# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        stack = []
        count = 1
        next = head
        while next.next is not None:
            count+=1
            stack.append(next.val)
            next = next.next
        if next is not None:
            stack.append(next.val)
        del stack[-n]
        if (len(stack) > 0):
            head = ListNode(stack[0])
            next = head
        else:
            head = ListNode('')
        for i in stack[1:]:
            next.next = ListNode(i)
            next = next.next
        return(head)
        
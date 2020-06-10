#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:05:26 2020

@author: user
"""


'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # convert it to a list, then figure out whether it is a palindrome
        lst = []

        current = head
        while current:
            val = current.val
            lst.append(val)
            current = current.next

        n = len(lst)
        flag = True
        for i in range(int(n/2)):
            if lst[i] != lst[n-1-i]:
                flag = False
                return(flag)

        return(True)
        
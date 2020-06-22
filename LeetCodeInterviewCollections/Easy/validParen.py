#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:09:52 2020

@author: user
"""


'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                stack.append(s[i])
            elif s[i]==')' and stack[len(stack)-1]=='(':
                stack.pop()
            elif s[i]==']' and stack[len(stack)-1]=='[':
                stack.pop()
            elif s[i]=='}' and stack[len(stack)-1]=='{':
                stack.pop()
        if stack==[]:
            return True
        return False
y=Solution()
s="()"
print(y.isValid(s))
s="()[]{}"
print(y.isValid(s))
s="(]"
print(y.isValid(s))
s="([)]"
print(y.isValid(s))
s="{[]}"
print(y.isValid(s))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:12:38 2020

@author: user
"""


'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle=='':
            return 0
        else:
            import re
            x=re.search(needle,haystack)
            if x==None:
                return -1
            else:
                return re.search(needle,haystack).start()
y=Solution()
haystack = "hello"
needle = "ll"
print(y.strStr(haystack, needle))
haystack = "aaaaa"
needle = "bba"
print(y.strStr(haystack, needle))
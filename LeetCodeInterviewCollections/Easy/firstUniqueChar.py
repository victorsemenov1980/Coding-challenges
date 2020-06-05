#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:30:55 2020

@author: user
"""


'''
Given a string, find the first non-repeating character in 
it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
 

Note: You may assume the string contain only lowercase English letters.
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
         # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
y=Solution()
s = "leetcode"
print(y.firstUniqChar(s))
s = "loveleetcode"
print(y.firstUniqChar(s))
s = "cc"
print(y.firstUniqChar(s))


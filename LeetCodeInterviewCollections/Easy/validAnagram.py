#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:57:10 2020

@author: user
"""


'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
               return False
        else:
            import collections
            count_s=collections.Counter(s)
            count_t=collections.Counter(t)
            if count_s==count_t:
                return True
            else:
                return False
            
              
y=Solution()
s = "anagram"
t = "nagaram"
print(y.isAnagram(s, t))
s = "rat"
t = "car"
print(y.isAnagram(s, t))
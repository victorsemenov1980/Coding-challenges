#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:18:46 2020

@author: user
"""


'''
Given two equal-size strings s and t. In one 
step you can choose any character of t and 
replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains 
the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, 
t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' 
from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
 

Constraints:

1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.
'''
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        freqs={}
        counter=0
        for char in s:
            if char in freqs:
                freqs[char]+=1
            else:
                freqs[char]=1
        for char in t:
            if char in freqs:
                freqs[char]-=1
                if freqs[char]<0:
                    counter+=1
            else:
                counter+=1
              
        return counter
y=Solution()
s = "bab" 
t = "aba"
print(y.minSteps(s, t))
s = "leetcode"
t = "practice"
print(y.minSteps(s, t))
s = "anagram"
t = "mangaar"
print(y.minSteps(s, t))
s = "xxyyzz"
t = "xxyyzz"
print(y.minSteps(s, t))
s= "friend"
t = "family"
print(y.minSteps(s, t))
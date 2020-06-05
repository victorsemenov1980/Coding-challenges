#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:40:38 2020

@author: user
"""


'''
Given a string, determine if it is a palindrome, c
onsidering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we
 define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        out=''
        for char in s:
            if char.isalnum():
                out+=char.lower()
        if out==out[::-1]:
            return True
        else:
            return False
y=Solution()
s="A man, a plan, a canal: Panama"
print(y.isPalindrome(s))
s="race a car"
print(y.isPalindrome(s))
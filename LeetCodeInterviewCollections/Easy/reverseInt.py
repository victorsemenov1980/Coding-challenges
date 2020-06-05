#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 17:29:16 2020

@author: user
"""
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x=x
        if x < (-1 * 2**31) or x > (2 ** 31 -1):#check for 32 bits
            return 0
       
        if x>0:
            string=str(x)[::-1]
            if int(string) < (-1 * 2**31) or int(string) > (2 ** 31 -1):
                return 0
            return int(string)
        elif x<0:
            x=(-1)*x
            string=str(x)[::-1]
            if int(string) < (-1 * 2**31) or int(string) > (2 ** 31 -1):
                return 0
            return int(string)*(-1)
        else:
            return x
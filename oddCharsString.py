#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:14:29 2020

@author: user
"""


'''
Given an integer n, return a string with n characters 
such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English 
letters. If there are multiples valid strings, return any of them.  

 

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 
'p' occurs three times and the character 'z' occurs once. 
Note that there are many other valid strings such as "ohhh" and "love".
Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 
'x' and 'y' occur once. Note that there are many other valid 
strings such as "ag" and "ur".
Example 3:

Input: n = 7
Output: "holasss"
 

Constraints:

1 <= n <= 500
'''

class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n%2==0:
            i=0
            out=''
            while i!=n-1:
                out+='a'
                i+=1
            out+='b'
        else:
            i=0
            out=''
            while i!=n:
                out+='c'
                i+=1
        return out

y= Solution()
n=4
print(y.generateTheString(n))
n=2
print(y.generateTheString(n))
n=7
print(y.generateTheString(n))
n=500
print(y.generateTheString(n))







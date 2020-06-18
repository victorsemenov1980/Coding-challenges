#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:57:46 2020

@author: user
"""


'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums=[1,3,9,27,81,243]
        
        if n==3 or n==1:
            return True
        elif n==0:
            return False
        else:
            
            while n>1:
                if n%3!=0:
                    return False
                    break
                elif n/3 in nums:
                    return True
                    break
                elif n/3<nums[-1] and n/3 not in nums:
                    
                    return False
                    break
                else:
                    n=n/3
           
y=Solution()
n=27
print(y.isPowerOfThree(n))
n=0
print(y.isPowerOfThree(n))
n=9
print(y.isPowerOfThree(n))
n=45
print(y.isPowerOfThree(n))
n=19684
print(y.isPowerOfThree(n))
n=1
print(y.isPowerOfThree(n))
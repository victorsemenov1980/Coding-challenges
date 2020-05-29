#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:02:12 2020

@author: user
"""


'''
Given an integer n, return any array containing n unique 
integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
'''
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        import random
        x=random.sample(range(0,1000),n-1)
        x.insert(-1,sum(x)*(-1))
        return x
        
y=Solution()
n=5
print(y.sumZero(n))
n=3
print(y.sumZero(n))
n=1
print(y.sumZero(n))
n=1000
print(y.sumZero(n))
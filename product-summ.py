#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:52:05 2020

@author: user
"""


'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5'''
import numpy as np #best memory efficiency, not really fast

class Solution(object):
    def subtractProductAndSum(self, n):
        '''can use string as n above zero'''
        # digits=[int(d) for d in str(n)] 
        digits=list(map(int,str(n)))
        
        array1=np.asarray(digits)
        """
        :type n: int
        :rtype: int
        """
        return np.prod(array1)-np.sum(array1)
       
        

y=Solution()
n = 234
print(y.subtractProductAndSum(n))
n = 4421  
print(y.subtractProductAndSum(n))









   
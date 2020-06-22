#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:33:19 2020

@author: user
"""


'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=numRows
        x=[]
        if n==0:
            return []
        if n==1:
            return [[1]]
        elif n==2:
            return [[1],[1,1]]
        else:
            x=[[1],[1,1]]
            coun=2
            while coun<n:
                y=x[-1]
                c=[]
                for i in range(len(y)-1):
                    c.append(y[i]+y[i+1])
                c=[1]+c+[1]
                x.append(c)
                coun+=1
        return x
y=Solution()
numRows=5
print(y.generate(numRows))
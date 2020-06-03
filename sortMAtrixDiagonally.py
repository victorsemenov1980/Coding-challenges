#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:19:56 2020

@author: user
"""


'''
Given a m * n matrix mat of integers, sort it diagonally 
in ascending order from the top-left to the bottom-right 
then return the sorted array.
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
'''
class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            row = i
            col = 0
            temp = []
            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row = i
            col = 0
            count = 0
            while row < m and col < n:
                mat[row][col] = temp[count]
                count += 1
                row += 1
                col += 1
        for i in range(1, n):
            row = 0
            col = i
            temp = []
            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row = 0
            col = i
            count = 0
            while row < m and col < n:
                mat[row][col] = temp[count]
                count += 1
                row += 1
                col += 1
        return mat

y=Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
print(y.diagonalSort(mat))


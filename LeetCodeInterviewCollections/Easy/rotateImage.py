#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:10:50 2020

@author: user
"""


'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have 
to modify the input 2D matrix directly. DO NOT allocate another 
2D matrix and do the rotation.
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # import numpy as np
        # return np.rot90(matrix, k = -1)
        for i in range(len(matrix)): 
            for j in range(i, len(matrix[0])): 
                t = matrix[i][j] 
                matrix[i][j] = matrix[j][i] 
                matrix[j][i] = t 
        print(matrix)
        for i in range(len(matrix[0])): 
            j = 0
            k = len(matrix[0])-1
            while j < k: 
                t = matrix[i][j] 
                matrix[i][j] = matrix[i][k] 
                matrix[i][k] = t 
                j += 1
                k -= 1
        return matrix

y=Solution()
matrix=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(y.rotate(matrix))
matrix=[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(y.rotate(matrix))
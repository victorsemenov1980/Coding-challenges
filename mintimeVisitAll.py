#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:51:48 2020

@author: user
"""


'''
On a plane there are n points with integer coordinates 
points[i] = [xi, yi]. Your task is to find the minimum 
time in seconds to visit all points.

You can move according to the next rules:

In one second always you can either move vertically, 
horizontally by one unit or diagonally (it means to move one 
unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is [1,1] -> 
[2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
Example 2:

Input: points = [[3,2],[-2,2]]
Output: 5
 

Constraints:

points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
'''
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time = 0
        if len(points)==1:
            return time
        startX,startY = points[0][0],points[0][1]
        for x,y in points[1:]:
            point_time = max(abs(x-startX),abs(y-startY))
            #minimum+(maximum-minimum)-->maximum between x and y
            
            time += point_time
            startX,startY = x,y
        return time
        
y=Solution()
points = [[1,1],[3,4],[-1,0]]
print(y.minTimeToVisitAllPoints(points))
print()
points = [[3,2],[-2,2]]
print(y.minTimeToVisitAllPoints(points))
print()
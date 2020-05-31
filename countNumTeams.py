#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:46:01 2020

@author: user
"""


'''
There are n soldiers standing in a line. Each soldier is 
assigned a unique rating value.

You have to form a team of 3 soldiers amongst them 
under the following rules:

Choose 3 soldiers with index (i, j, k) with rating 
(rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) 
or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. 
(soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the 
conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
'''
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        from itertools import combinations
        permuts=[]
        permuts=list(combinations(rating, 3))
        num=0
        for li in permuts:
            if list(li)== sorted(li) or list(li)==sorted(li,reverse=True):
                num+=1
        
        return num
        
        
        
        
y=Solution()
rating = [2,5,3,4,1]
print(y.numTeams(rating))
rating = [2,1,3]
print(y.numTeams(rating))
rating = [1,2,3,4]
print(y.numTeams(rating))




    

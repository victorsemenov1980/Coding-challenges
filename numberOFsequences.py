#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:57:01 2020

@author: user
"""


'''
You have a set of tiles, where each tile has one 
letter tiles[i] printed on it.  Return the number 
of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences 
are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
'''
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        import itertools
        count=0
        for r in range(1,len(tiles)+1):
            x=list(itertools.permutations(tiles, r))
            count+=len(set(x))
                    
        return count
y=Solution()
tiles='AAB'
print(y.numTilePossibilities(tiles))
tiles='AAABBC'
print(y.numTilePossibilities(tiles))
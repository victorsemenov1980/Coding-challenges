#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:20:25 2020

@author: user
"""


'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        j=1
        out=''
        prefix=''
        while len(strs[0])-j!=-1:
            
            x=0
            prefix=strs[0][:j]
            # print('pre',prefix)
            for i in strs:
               if i[:j]==prefix:
                   # print('I',i[:j])
                   x+=1
                   # print('X',x)
            if x==len(strs):
                out=prefix
                # print('out',out)
                
            else:
                return out
                break
            j+=1
            
            
        return out
        
        
                    
            
           
y=Solution()
strs=["flower","flow","flight"]
print(y.longestCommonPrefix(strs))
strs=["dog","racecar","car"]
print(y.longestCommonPrefix(strs))
strs=[]
print(y.longestCommonPrefix(strs))
strs=[" "]
print(y.longestCommonPrefix(strs))
strs=["c","c"]
print(y.longestCommonPrefix(strs))
strs=["cbc","cbd"]
print(y.longestCommonPrefix(strs))
strs=["ccc","ccc"]
print(y.longestCommonPrefix(strs))
strs=["abca","aba","aaab"]
print(y.longestCommonPrefix(strs))
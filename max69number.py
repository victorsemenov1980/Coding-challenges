#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:07:55 2020

@author: user
"""


'''
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by 
changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
'''
class Solution(object):
    def maximum69Number (self, num):
    
        """
        :type num: int
        :rtype: int
        """
        self.num=num
        max_num=[]
        temp=''
        strnum=str(num)
        for i in range(len(strnum)):
            if strnum[i]=='9':
                temp+=strnum[:i]+'6'+strnum[i+1:]
            else: 
                temp+=strnum[:i]+'9'+strnum[i+1:]
            if int(temp)>num:
                max_num.append(temp)
            temp=''
        if len(max_num)==0:
            return num
        else:
            x=sorted(max_num)
            return x[-1]
            
y=Solution()
num = 9669
print(y.maximum69Number(num))
num = 9996
print(y.maximum69Number(num))
num = 9999
print(y.maximum69Number(num))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:20:16 2020

@author: user
"""


'''
The count-and-say sequence is the sequence of integers with the first 
five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the 
count-and-say sequence. You can do so recursively, in other words from 
the previous member read off the digits, counting the number of digits 
in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups 
"2" and "1", "2" can be read as "12" which means frequency = 1 and 
value = 2, the same way "1" is read as "11", so the answer is the 
concatenation of "12" and "11" which is "1211".

1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211

To generate the nth term, just count and say the n-1th term.
'''
class Solution(object):
    def __init__(self):
        self.count = 1
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return str(n)
        else:
            retS = ''
            s= str(self.countAndSay(n - 1)) + '$'
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    self.count += 1
                else:
                    retS += str(self.count) + s[i - 1]
                    self.count = 1
                
            return retS
y=Solution()
print(y.countAndSay(1))
print(y.countAndSay(4))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:27:09 2020

@author: user
"""


'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        five=[5*n for n in range(1,n+1)]
        
        three=[3*n for n in range(1,n+1)]
        
        out=[]
        for i in range(1,n+1):
            if i in five and i not in three:
                out.append('Buzz')
            elif i in three and i not in five:
                out.append('Fizz')
            elif i in five and i in three:
                out.append('FizzBuzz')
            else:
                out.append(str(i))
        return out

y=Solution()
n=15
print(y.fizzBuzz(n))






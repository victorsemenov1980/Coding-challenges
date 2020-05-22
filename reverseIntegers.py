#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:44:41 2020

@author: user
"""
'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
'''

'''
Solution div by 10. Turned out to be very slow
'''

# class Solution(object):
#     def reverse(self, x):
#         self.x=x
#         if x < (-1 * 2**31) or x > (2 ** 31 -1):#check for 32 bits
#             return 0
#         res=[]
#         if x>0:
#             while x!=0:
#                 digit= x%10
#                 x=x//10
#                 res.append(digit)
#             str_nums = [str(x) for x in res]
#             if int(''.join(str_nums)) < (-1 * 2**31) or int(''.join(str_nums)) > (2 ** 31 -1):
#                 return 0
#             return int(''.join(str_nums))
#         elif x<0:
#             x=-1*x
#             while x!=0:
#                 digit= x%10
#                 x=x//10
#                 res.append(digit)
#             str_nums = [str(x) for x in res]
#             if int(''.join(str_nums)) < (-1 * 2**31) or int(''.join(str_nums)) > (2 ** 31 -1):
#                 return 0
#             return int(''.join(str_nums))*(-1)
#         else:
#             return x
        
        
#         """
#         :type x: int
#         :rtype: int
#         """

'''
Solution with string, turned out to be twice as fast
'''
class Solution(object):
    def reverse(self, x):
        self.x=x
        if x < (-1 * 2**31) or x > (2 ** 31 -1):#check for 32 bits
            return 0
       
        if x>0:
            string=str(x)[::-1]
            if int(string) < (-1 * 2**31) or int(string) > (2 ** 31 -1):
                return 0
            return int(string)
        elif x<0:
            x=(-1)*x
            string=str(x)[::-1]
            if int(string) < (-1 * 2**31) or int(string) > (2 ** 31 -1):
                return 0
            return int(string)*(-1)
        else:
            return x

x=Solution()
number=-123
print(x.reverse(number))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:52:22 2020

@author: user
"""


'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
'''
class Solution(object):
    def myAtoi(self, str_):
        """
        :type str: str
        :rtype: int
        """
        x=str_.strip()
        if len(x)==0:
            return 0
        else:
            min_=-2**31
            max_=2**31-1
            
            out=''
            if x[0].isnumeric() or x[0] in ['-','+']:
                out+=x[0]
                for char in x[1:]:
                    
                    if char.isalpha() or char in [' ','.','-','+']:
                        break

                    else:
                        out+=char
                try:
                    int(out)
                    if int(out)>max_:
                        return max_
                    elif int(out)<min_:
                        return min_
                    else:
                        return int(out)
                except:
                    return 0
            else:
                return 0
            
       
y=Solution()
str_="42"
print(y.myAtoi(str_))
str_="   -42"
print(y.myAtoi(str_))
str_="4193 with words"
print(y.myAtoi(str_))
str_="words and 987"
print(y.myAtoi(str_))
str_="-91283472332"
print(y.myAtoi(str_))
str_="3.14159"
print(y.myAtoi(str_))
str_=""
print(y.myAtoi(str_))
str_="+"
print(y.myAtoi(str_))
str_="  "
print(y.myAtoi(str_))
str_="-5-"
print(y.myAtoi(str_))

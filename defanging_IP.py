#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:11:08 2020

@author: user
"""


'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.
'''

class Solution(object):
    def defangIPaddr(self, address):
        
        return address.replace('.', '[.]')
        """
        :type address: str
        :rtype: str
        """

address='1.1.1.1'
y=Solution()
print(y.defangIPaddr(address))
print()
address='255.100.50.0'
y=Solution()
print(y.defangIPaddr(address))
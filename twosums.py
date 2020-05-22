#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:53:49 2020

@author: user
"""

'''
BrutForce- too slow
'''
# import itertools


# def twoSum(nums, target):
#         L=[]
#         for i in itertools.combinations(range(len(nums)), 2):
#             if nums[i[0]]+nums[i[1]] ==target:
#                 L.append(i[0])
#                 L.append(i[1])
#                 break
                
    
#         return L
        
# nums = [3,2,4]
# target = 6
# print(twoSum(nums, target))

'''
Solution with dict - much much faster
'''
def twoSum(nums, target):
    hash_dict = {}
    for i, v in enumerate(nums):
            x =  target - v  
            if x in hash_dict:
                return[hash_dict[x],i]
            else:
                hash_dict[v] = i

nums = [3,2,4]
target = 6
print(twoSum(nums, target))
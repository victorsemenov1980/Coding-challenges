#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:44:06 2020

@author: user
"""


'''
A format for expressing an ordered list of integers is 
to use a comma separated list of either

individual integers
or a range of integers denoted by the starting 
integer separated from the end integer in the range by 
a dash, '-'. The range includes all integers in the interval 
including both endpoints. It is not considered a range unless
 it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in 
increasing order and returns a correctly formatted string in the 
range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''
def solution(args):
    out=''
    if len(args)==2:
        out+=str(args[0])
        out+=','
        out+=str(args[1])
    else:
        if len(args)==3:
            if args[1]==args[0]+1 and args[2]==args[0]+2:
                out+=str(args[0])
                out+='-'
                out+=str(args[2])
            else:
                out+=str(args[0])
                out+=','
                out+=str(args[1])
                out+=','
                out+=str(args[2])
        else:    
            for i in range(len(args)):
                
                if i==len(args)-1:
                    out+=str(args[i])
                    
                else:
                    if args[i+1]!=args[i]+1:
                        out+=str(args[i])
                        out+=','
                        
                        
                        
                    elif len(out)>0 and out[-1]=='-':
                        pass
                    else:
                        if i==len(args)-2:
                            if out[-1]==',':
                                out+=str(args[i])
                                out+=','
                            elif out[-1]=='-':
                                out+=str(args[i])
                        else:
                            if args[i+2]==args[i]+2:
                                out+=str(args[i])
                                out+='-'
                               
                            else:
                                out+=str(args[i])
                                out+=','
                                
    return out
    
# if solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) == '-6,-3-1,3-5,7-11,14,15,17-20':
#     print('True')
# else: 
#     print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# if solution([-3,-2,-1,2,10,15,16,18,19,20])== '-3--1,2,10,15,16,18-20':
#     print('True')
# else:
#     print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
# if solution([97, 98, 99, 100, 101, 102, -7, -6, 14, 15, 16, 17,18, -46, -45, -44, -95, -74, 65, 66, 67, 68, 37, 38, 39, 40, 41, 42, 58, -31,-30, -29, -28, -27, -43, -42, -41, -40, -39, -38, -37, 52, 53, 54, 67, 68,69, 70, 71, 72, -48, -47, -46, -45, -44]) == "97-102,-7,-6,14-18,-46--44,-95,-74,65-68,37-42,58,-31--27,-43--37,52-54,67-72,-48--44":
#     print('True')

print(solution([-73, -72, -69, -67, -66, -63, -62, -59, -56, -53, -52]))    


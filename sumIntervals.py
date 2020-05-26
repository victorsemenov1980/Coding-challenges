#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:50:12 2020

@author: user
"""


'''
Write a function called sumIntervals/sum_intervals() 
that accepts an array of intervals, and returns the s
um of all the interval lengths. Overlapping intervals should only be counted once.

Intervals

Intervals are represented by a pair of integers 
in the form of an array. The first value of the interval 
will always be less than the second value. Interval example: 
    [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals

List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. 
Since [1, 4] and [3, 5] overlap, we can treat the interval as 
[1, 5], which has a length of 4.

Examples:

sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
'''
def no_overlapping(x):
        no_overlap=[]
        i=0
        x=sorted(x)
        
        while True:
            
            if x[i][1]<x[i+1][0]:
                
                no_overlap.append(x[i])
                del x[i]
            elif x[i+1][1]<x[i][1]>x[i+1][0]:
                no_overlap.append(x[i])
                
                del x[i]
                del x[i]
                
            elif x[i+1][1]>x[i][1]>x[i+1][0]:
                tmp=[]
                tmp.append(x[i][0])
                tmp.append(x[i+1][1])
                
                no_overlap.append(tmp)
                tmp=[]
                
                del x[i]
                del x[i]
               
            if len(x)==0:
                break
            if len(x)==1:
                
                no_overlap.append(x[0])
                break
        return no_overlap  

def check_overlap(x):
    check=0
    y=sorted(x)
    for i in range(len(y)-1):
        if y[i][1]>y[i+1][0]:
            check+=1
    if check>0:
        return True
    else:
        return False
        
    
def sum_of_intervals(intervals):
    
    while check_overlap(intervals)==True:
        
        intervals=no_overlapping(intervals)
    summ=0
    for i in intervals:   
        summ+=i[1]-i[0]
        
    return summ
    
        
    
    
    
print('Sum=',sum_of_intervals([[1,2],[6,10],[11,15]]))
print('Sum=',sum_of_intervals([[1,4],[7,10],[3,5]]))
print('Sum=',sum_of_intervals([[1,5],[10,20],[1,6],[16,19],[5,11]]))








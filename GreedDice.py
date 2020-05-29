#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:36:48 2020

@author: user
"""


'''
Greed is a dice game played with five six-sided dice. 
Your mission, should you choose to accept it, is 
to score a throw according to these rules. You will 
always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. 
For example, a "5" can only count as part of a triplet 
(contributing to the 500 points) or as a single 50 points, 
but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450
 '''
def score(dice):
    out=0
    x1=dice.count(1)
    x2=dice.count(2)
    x3=dice.count(3)
    x4=dice.count(4)
    x5=dice.count(5)
    x6=dice.count(6)
    count1=3
    count5=3
    if x1>=3:
        
        out+=1000
        for i in dice:
            if i==5:
                out+=50
            if i==1:
               count1-=1
               if count1==-1:
                   out+=100
               if count1==-2:
                   out+=100
                
    elif x6>=3:
        out+=600
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                out+=50
                
    elif x5>=3:
        out+=500
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                count5-=1
                if count5==-1:
                   out+=50
                if count5==-2:
                   out+=50
            
        
    elif x4>=3:
        out+=400
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                out+=50
    elif x3>=3:
        out+=300
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                out+=50
    elif x2>=3:
        out+=200
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                out+=50
    else:
        for i in dice:
            if i==1:
                out+=100
            if i==5:
                out+=50
    
    return out

print(score([5,1,3,4,1]))
print(score([1,1,1,3,1]))
print(score([2,4,4,5,4]))


    
 
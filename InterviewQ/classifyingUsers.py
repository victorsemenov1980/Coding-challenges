#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:08:04 2020

@author: user
"""
'''
You are given a list of XP points of all users, your 
task is to calculate how many users are there in each 
level and print them in decreasing order of those numbers. 
In case of a tie, higher level should appear first.

Levels are defined in the following way:

Recruit: 0 - 999 XP
Soldier: 1000 - 4999 XP
Warrior: 5000 - 9999 XP
Captain: 10000 - 49999 XP
Ninja: 50000+ XP
Return a list of strings where each string would represent a 
level and number of users within that level, for example:

Soldier - 15
Recruit - 13
Ninja - 1
Levels which don't have any users should not be included.

[execution time limit] 4 seconds (py3)

[input] array.integer points

An array containing list of all user XP points

[output] array.string

List of levels with the number of corresponding users sorting in 
decreasing order of those numbers
[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''

def getUserLevelBreakdown(points):
    out={}
    recruit=0
    soldier=0
    warrior=0
    captain=0
    ninja=0
    for i in points:
        if i in range(0,1000):
            recruit+=1
        if i in range(1000,5000):
            soldier+=1
        if i in range(5000,10000):
            warrior+=1
        if i in range(10000,50000):
            captain+=1
        if i >=50000:
            ninja+=1
    if ninja!=0:
        out[f'Ninja - {ninja}']=ninja
    if captain!=0:
        out[f'Captain - {captain}']=captain
    if warrior!=0:
        out[f'Warrior - {warrior}']=warrior
    if soldier!=0:
        out[f'Soldier - {soldier}']=soldier
    if recruit!=0:
        out[f'Recruit - {recruit}']=recruit
   
    return sorted(out,key=out.get)

points= [999, 4999, 9999, 49999, 50000]
print(getUserLevelBreakdown(points))







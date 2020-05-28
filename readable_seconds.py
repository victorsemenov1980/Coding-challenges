#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:18:25 2020

@author: user
"""


'''
Write a function, which takes a non-negative integer (seconds) as 
input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
'''

def make_readable(seconds):
    h=''
    m=''
    s=''
    hours=str(seconds//3600)
    if len(hours)!=2:
        h+='0'+hours
    else:
        h+=hours
        
    minutes=str((seconds%3600)//60)
    if len(minutes)!=2:
        m+='0'+minutes
    else:
        m+=minutes
    secs=str((seconds%3600)%60)
    if len(secs)!=2:
        s+='0'+secs
    else:
        s+=secs
    
    return f'{h}:{m}:{s}'
        
    
    

print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:06:49 2020

@author: user
"""



def commonChars(A):
    """
    :type A: List[str]
    :rtype: List[str]
    """
    out=[]
    out2=[]
    for i in A:
        temp=[]
        for j in i:
            temp.append(j)
        out.append(temp)
    common=set.intersection(*[set(list) for list in out])
   
    for k in common:
        
        count=1
        counts=[]
        for i in A:
            x=i.count(k)
            counts.append(x)
            
        if min(counts)>count:
            count=min(counts)
        else:
            count=1
        for j in range(count):
            out2.append(k)
            
    return out2

# A=["bella","label","roller"]
# print(commonChars(A))
# A=["cool","lock","cook"]
# print(commonChars(A))
# A=["bcaddcdd","cbcdccdd","ddccbdda","dacbbdad","dababdcb","bccbdaad","dbccbabd","accdddda"]
# print(commonChars(A))

def balancedStringSplit(s):
        """
        :type s: str
        :rtype: int
        """
        count = {'R': 0, 'L': 0}
        out=0
        for char in s:
            count[char] += 1
            if count['R'] == count['L']:
                out += 1
                count['R'] = 0
                count['L'] = 0
        return out
        
    
s = "RLRRLLRLRL"
print(balancedStringSplit(s))
s = "RLLLLRRRLR"
print(balancedStringSplit(s))

















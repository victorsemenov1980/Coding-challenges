#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:31:04 2020

@author: user
"""

'''
You have a string s that represents a chemical reaction.

The chemical reaction is a string in the following format: 
    molecule (+ molecule)* = molecule (+ molecule)*, where " * 
    " means any non-negative number of repeats. For example, 
    "A = B", "A = B + C", "A + B + C = D + E + F" are chemical 
    reactions but "X + Y = ", "X = + Z" are not.

A molecule is concatenation of a coefficient (optional) and a 
string that represents the concatenation of elements and their 
coefficents (optional). A coefficent is a positive integer 
that doesn't exceed 1000, and it represents the number of repeats.
 For example, "Cu12" means 12 repeats of "Cu" element. "3H2O" means 
 6 repeats of "H" element and 3 repeats of "O" elements: 3 is a 
 coefficient of the "H2O" molecule and 2 is a coefficient of 
 the "H" element. The coefficient of the "O" element is absent, 
 which means this element repeats once in each instance of this molecule.

An element is a string that starts with an uppercase English 
letter, while every other symbol is a lowercase English letter. 
For example, "A" and "Abc" are elements but "FF" and "hello" are not. 
"FF" actually indicates that there are 2 repeats of the "F" element.

A chemical reaction is considered to be balanced if every element 
has the same number of repeats on both sides of the chemical reaction.

Check whether the given chemical reaction is balanced.

Example

For s = "2H2 + O2 = 2H2O", the output should be
isReactionBalanced(s) = true.

Left side: 4 * "H" and "2 * O". Right side: 4 * "H" and "2 * O".

For s = "1000H2O = Au + Ag", the output should be
isReactionBalanced(s) = false.

Left side: 2000 * "H" and "1000 * O". Right side: 1 * "Ag" and "1 * Au".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that represents a chemical reaction.

Guaranteed constraints:
5 ≤ s.length ≤ 3000.

[output] boolean

Return true if s represents a balanced chemical reaction, 
otherwise return false.

'''
def isReactionBalanced(s):
    import re
    x=re.split(r'=',s)
    left=x[0].split()
    left_dict={}
    right_dict={}
    for i in left:
        if i!='+':
            splitted=re.findall(r'\d+|[A-Z][a-z]*', i)
        
            '''
            Details:

            \d+ - 1+ digits
            | - or
            [A-Z][a-z]* - an upper case letter and 
            then zero or more lowercase ones.
            '''
            if splitted[0].isdigit():
                multiplier=int(splitted[0])
                for s in range(1,len(splitted)):
                    if not splitted[s].isdigit():
                        
                        left_dict[splitted[s]]=1*multiplier
                    else:
                        left_dict[splitted[s-1]]*=int(splitted[s])
                   
            else:
                multiplier=1
                for s in range(len(splitted)):
                    if not splitted[s].isdigit():
                        left_dict[splitted[s]]=1*multiplier
                    else:
                        left_dict[splitted[s-1]]=int(splitted[s])*multiplier
            
            
    print(left_dict)   
    print('left done')
                            
    right=x[-1].split()
    for i in right:
        if i!='+':
            splitted=re.findall(r'\d+|[A-Z][a-z]*', i)
            if splitted[0].isdigit():
                multiplier=int(splitted[0])
                for s in range(1,len(splitted)):
                    if not splitted[s].isdigit():
                        right_dict[splitted[s]]=1*multiplier
                    else:
                        right_dict[splitted[s-1]]*=int(splitted[s])
            else:
                multiplier=1
                for s in range(len(splitted)):
                    if not splitted[s].isdigit():
                        right_dict[splitted[s]]=1*multiplier
                    else:
                        right_dict[splitted[s-1]]=int(splitted[s])*multiplier
    print(right_dict)
    print('right done')
    if right_dict==left_dict:
        return True
    else:
        return False
    
s = "2H2HfSs + O2 = 2H2O"
print(isReactionBalanced(s))
s = "1000H2O = Au + Ag"
print(isReactionBalanced(s))
s = "2H2 + O2 = 2H2O"
print(isReactionBalanced(s))

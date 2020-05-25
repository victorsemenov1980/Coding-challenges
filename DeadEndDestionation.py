#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:13:44 2020

@author: user
"""


'''
You are given the array paths, where paths[i] = [cityAi, cityBi] 
means there exists a direct path going from cityAi to cityBi. 
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any 
loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach 
"Sao Paulo" city which is the destination city. Your trip consist of: 
    "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 

Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.

'''
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        answer=''
        reg_dest=[]
        reg_origin=[]
        for i in paths:
             if i[0] not in reg_origin:
                reg_origin.append(i[0])
             if i[1] not in reg_dest:
                reg_dest.append(i[1])
        for i in reg_dest:
            if i not in reg_origin:
                answer+=i
            
        return answer
y=Solution()       
        
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(y.destCity(paths))
print()
paths = [["B","C"],["D","B"],["C","A"]]
print(y.destCity(paths))
print()
paths = [["A","Z"]]
print(y.destCity(paths))
print()
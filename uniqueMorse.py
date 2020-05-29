#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:42:05 2020

@author: user
"""


'''
International Morse Code defines a standard encoding where each   
letter is mapped to a series of dots and dashes, as follows: "a" 
maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the 
English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as 
a concatenation of the Morse code of each letter. For 
example, "cba" can be written as "-.-..--...", 
(which is the concatenation "-.-." + "-..." + ".-"). 
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        import string
        a=list(string.ascii_lowercase)
        code={}
        for i in range(len(morse)):
            code[a[i]]=morse[i]
        morsed=''
        morsed_L=[]
        for i in words:
            for j in i:
                morsed+=code[j]
                
            morsed_L.append(morsed)
            morsed=''
        x=set(morsed_L)
        
        return len(x)
    
y=Solution()
words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
print(y.uniqueMorseRepresentations(words))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
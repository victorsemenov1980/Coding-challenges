#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:43:28 2020

@author: user
"""


'''
What is an anagram? Well, two words are anagrams of each other if 
they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''
def anagrams(word, words):
    result=[]
    result2=[]
    counter=0
    for i in words:
        if len(i)==len(word):
            for char in word:
                if char in i:
                    counter+=1 
            if counter==len(word):
                result.append(i)   
        counter=0
    for i in result:
        for char in i:
            if char in word:
                counter+=1 
        if counter==len(word):
            result2.append(i)   
        counter=0
                
    return result2

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print()
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print()
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))


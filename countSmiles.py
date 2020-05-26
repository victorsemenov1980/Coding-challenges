#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:40:57 2020

@author: user
"""


'''
Given an array (arr) as an argument complete the 
function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. V
alid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
Invalid smiley faces:
;( :> :} :] 

Example cases:

countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

Note: In case of an empty array return 0. You will not be 
tested with invalid input (input will always be an array). 
Order of the face (eyes, nose, mouth) elements will always be the same
'''

def count_smileys(arr):
    mouth=[')','D']
    eyes=[':',';']
    noses=['-','~']
    '''
    reslly there are so few combinations, no need for coding even )))
    '''
    smiles=[':)',':D',';)',';D',':-)',':-D',';-)',';-D',':~)',':~D',';~)',';~D']
    counter=0
    for i in arr:
        if i in smiles:
            counter+=1
    return counter
print(count_smileys([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))


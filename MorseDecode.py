#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:26:44 2020

@author: user
"""


'''
Simple decoder

When the message is written in Morse code, 
a single space is used to separate the character codes
and 3 spaces are used to separate words.

In addition to letters, digits and some punctuation, 
there are some special service codes, the most notorious 
of those is the international distress signal SOS (that 
was first issued by Titanic), that is coded as ···−−−···. 
These special codes are treated as single special characters, 
and usually are transmitted as separate words.
'''

MORSE_CODE={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def decodeMorse(morse_code):
    x=morse_code.split('   ')
    decode=''
    for i in x:
        y=i.split(' ')
        for j in y:
            if j in MORSE_CODE:
                decode+=MORSE_CODE[j]
        decode+=' '
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return '-->' + decode.rstrip().lstrip() + '<--'



print(decodeMorse('.... . -.--   .--- ..- -.. .'))
print(decodeMorse('...---...'))

#should return "HEY JUDE"
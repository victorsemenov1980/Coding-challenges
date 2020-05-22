#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:49:40 2020

@author: user
"""


'''
 inserts a certain number of words "WUB" before the 
 first word of the song (the number may be zero), after the 
 last word (the number may be zero), and between words (at least one 
 between any pair of neighbouring words), and then the boy glues together 
 all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep 
remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Jonny has heard Polycarpus's new dubstep track, but since 
he isn't into modern music, he decided to find out what was the initial 
song that Polycarpus remixed. Help Jonny restore the original song.

song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
'''
import re

def song_decoder(song):
    decoded= re.sub(r'WUB', ' ',song)
    x=" ".join(decoded.split())   
    return x

print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
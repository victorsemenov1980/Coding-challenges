#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:53:50 2020

@author: user
"""


'''
TinyURL is a URL shortening service where you enter a 
URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the 
TinyURL service. There is no restriction on how your 
encode/decode algorithm should work. You just need to ensure 
that a URL can be encoded to a tiny URL and the tiny URL can 
be decoded to the original URL.
'''
class Codec:
    def __init__(self):
        self.dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import random
        len_code=6
        shortUrl=''
        coding_string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        for i in range(len_code):
            shortUrl+=random.choice(coding_string)
        self.dict[shortUrl]=longUrl
        return shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.dict:
            return self.dict[shortUrl]
        
codec=Codec()
print(codec.encode('https://leetcode.com/problems/design-tinyurl'))
print(codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl')))    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
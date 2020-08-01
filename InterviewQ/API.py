#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:30:43 2020

@author: user
"""

'''
We want to query an API endpoint to receive data about 
apartment listings on a rental website. Among the data 
fields is a column called num_bedrooms, which takes the 
value of 1 for a 1-bedroom apartment and 0 for a studio.

Upon examining the descriptions of the listings, we 
find that the provided data is ocasionally mistagged. 
For instance, sometimes a studio is described where 
num_bedrooms=1 or a 1-bedroom is described where num_bedrooms=0.

Your task is to write a function to correct this problem.

Write a function that accepts the jsonData as it comes 
from a GET request in string format. Return an array 
(from pandas Series) that contains zeros and ones, with the correct 
values for num_bedrooms.

Keep in mind that there can be cases when a studio apartment is 
incorrectly detected. For example: "description": "Beautiful 
apartment with nearby yoga studio." will be detected as a studio 
apartment and will have num_bedrooms=0, even though this is not correct. 
There can be a lot of words preceding the word "studio" that should be 
ignored, but we do need to consider three such words: "yoga", "dance", 
and "art". So, if the word "studio" is preceded by any of these three 
words, you shouldn't detect the corresponding listing as a "studio".

If the description doesn't contain the words "bedroom" or "studio", 
leave the existing value of num_bedrooms.

Note: letters case should be ignored.

Example

For
jsonData = "[{"id": "1", "agent": "Radulf Katlego", "address": 
    "123 circle dr. #3", "description" : "This luxurious studio apartment 
    is in the heart of downtown", "num_bedrooms": 1},{"id": "2", "agent": 
        "Kelemen Konrad", "address": "456 square dr.", "description": 
            "We have studios and 1-bedrooms available.", "num_bedrooms": 1},
    {"id": "3", "agent": "Ton Jett", "address": "789 rectangle ave. #12", 
    "description": "Beautiful apartment with nearby yoga studio.", 
    "num_bedrooms": 1},{"id": "4", "agent": "Fishel Salman", 
    "address": "789 rectangle ave. 13", "description": 
        "Beautiful studio with nearby yoga studio.", "num_bedrooms": 1}]",
the output should be classifyApartments(jsonData) = [0, 1, 1, 0].

The above jsonData represents the following JSON:

[
   {
      "id": "1",
      "agent": "Radulf Katlego",
      "address": "123 circle dr. #3",
      "description" : "This luxurious studio apartment is in the heart of downtown",
      "num_bedrooms": 1
   },
   {
      "id": "2",
      "agent": "Kelemen Konrad",
      "address": "456 square dr.",
      "description": "We have studios and 1-bedrooms available.",
      "num_bedrooms": 1
   },
   {
      "id": "3",
      "agent": "Ton Jett",
      "address": "789 rectangle ave. #12",
      "description": "Beautiful apartment with nearby yoga studio.",
      "num_bedrooms": 1
   },
   {
      "id": "4",
      "agent": "Fishel Salman",
      "address": "789 rectangle ave. 13",
      "description": "Beautiful studio with nearby yoga studio.",
      "num_bedrooms": 1
   }
]
Input/Output

[execution time limit] 4 seconds (py3)

[input] string jsonData

String in JSON format. It's guaranteed that each listing contains 
the fields "description" and "num_bedrooms".

Guaranteed constraints:
136 ≤ jsonData.length ≤ 95321.

[output] array.integer

Return an array that contains the correct values for num_bedrooms 
for all of the listings in jsonData.
Note for Python3 users: if you use a numpy array, casting to a 
list creates a list of numpy.int64 integers. Your returned array
 needs to be an array of standard Python int types.

[Python3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name
'''

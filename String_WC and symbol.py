# -*- coding: utf-8 -*-
"""
String Manipulation
Program to do:
    1. Word count in a sentence.
    2. Special symbol(?) count in a sentence
"""
sentence="Hi, How are you I am fine."
count=0#word count
q_count=0#'?' count
for letter in sentence:
    if letter==' ':#checking for a space 
        count+=1
    elif letter=='?':#checking for '?'
        q_count+=1
print("The number of words is:",count+1)
print("The number of occurence of ? symbol",q_count)

# -*- coding: utf-8 -*-
"""
Program to illustrate dictionary concepts:
    1. Create a dictionary
    2. Process Keys and values
"""
#dictionary --> set of items
#item --> key value pair
d={1:"akash",2:"aaron",3:"athira"}
print (d)
print(d.keys())#prints keys present in the dictionary
print(d.values())#prints values
if 2 in d.keys():
    print("Key 1 is present")
if "aaron" in d.values():
    print("Value 'aaron' is present")
del d[2]
print(d)
    


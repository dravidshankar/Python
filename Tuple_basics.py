# -*- coding: utf-8 -*-
"""
Tuple

Program to:
    1. Get elements into tuple
    2. Search for an element in tuple
"""
x=()#initialise empty tuple
n=int(input("Enter the number of elements"))
for i in range(n):
    print("Enter the element ",i+1, ": ")
    element=int(input())
    x=x+(element,)#x[i]=element
    print(x)
print("Tuple is:", x)
key=22
if 22 in x:
    print("Element present")
else:
    print("Element not present")


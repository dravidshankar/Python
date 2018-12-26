# -*- coding: utf-8 -*-
"""
List Processing

Program to do:
    1. Get elements into the list from user
    2. Find  average value of elements in the list
    3. Find the cube of each values in the list
"""
x=[]#initialise empty list
n=int(input("Enter the number of elements required:"))
for i in range(0,n):
    print("Enter the element",i+1,":")
    element=int(input())
    x.append(element)
print("The list of elements is:",x)
average=0
sum=0
for i in x:
    sum=sum+i
average=sum/n
print("The average is: ", average)
for i in x:
    print("Cube of element ",i," is:", i**3)





    



    

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:49:38 2018

@author: user
"""
f=open("test.txt","r")
text=f.read()
print("Printing the contents of file\n:")
print(text)
f.close()
f1=open("test.txt","r")
count=0
L=[]
text=""
new=""
text=f1.read()
print(text)
for i in text:
    if i =="\n" or i =="?" or i=="," or i =="." or i==":" or i=="!" or i=="\"" or i=="'":
        new=new+" "
    else:
        new=new+i
L=new.split(" ")
print(L)
for j in L:
    if len(j)==4:
            count+=1
print("The count of four letter words is:",count)    
f1.close()

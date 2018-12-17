# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:12:38 2018

@author: user
"""
source="test.txt"
f1=open(source,"a")
f1.write("\n")
f1.write("good night")
f1.close()
line_count=0
f2=open("test.txt","r")
for i in f2.readlines():
    line_count+=1
f2.close()
f2=open("test.txt","r")
text=f2.read()
print("Contents of the file:\n",text)
print("Number of lines are:",line_count)
f2.close()
f1=open("test.txt","r")
space_count=0
for text in f1.read():
    if text==" ":
        space_count+=1
print("The number of spaces in the file is:",space_count+1)
f1.close()
f1=open("test.txt","r")
text=f1.read()
print(text)
f1.close()
f1=open("test.txt","r")
f2=open("test1.txt","w")
for text in f1:
    text=text[::-1]
    f2.write(text)
f1.close()
f2.close()
f2=open("test1.txt","r")
print(f2.read())
f2.close()
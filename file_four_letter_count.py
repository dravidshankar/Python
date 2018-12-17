# -*- coding: utf-8 -*-
"""
Find the count of four letter words from a file
"""
f=open("test.txt","r")
#opening test.txt in read mode
text=f.read()
print("Printing the contents of file\n:")
print(text)
f.close()
f1=open("test.txt","r")
count=0#to store the count of 4 letter words
L=[]#list to store the words
new=""#string new initialized with null
text=f1.read()
for i in text:
#process each character 
    if i =="\n" or i =="?" or i=="," or i =="." or i==":" or i=="!" or i=="\"" or i=="'":
        #checks for newline or punctuations
        new=new+" "
        #replace space or punctuations with space
    else:
        new=new+i
        #copie the string to new
L=new.split(" ")#split returns a list
#L contains each word
#print(L)
for j in L:
#process each list element
    if len(j)==4:
        #checks for 4 letter count
            count+=1#increments count
print("The count of four letter words is:",count)    
f1.close()

# -*- coding: utf-8 -*-
"""
1. Print the number of lines in a file
2. Print the number of spaces in a file
3. Read the contents of a file in reverse order
"""
source="test.txt"
f1=open(source,"w")
#open the file test.txt in write mode
f1.write("Hai\n")
#write in new line
f1.write("Good night")
#Write the string "goog night"
f1.close()
line_count=0 # to find number of lines
f2=open("test.txt","r")
#opened the file test.txt in read mode
for i in f2.readlines():
#reads each line at a time and stores in variable i
    line_count+=1 #increment line count
f2.close()
f2=open("test.txt","r")
#Opening the file again for reading the contents
text=f2.read()
print("\nContents of the file:\n",text)
print("\nNumber of lines:",line_count)
#Prints the number of lines
f2.close()
f1=open("test.txt","r")
#Opening the file in read mode to find space count
space_count=0 #to store the space count
for text in f1.read():
    if text==" ":#checking for a space 
        space_count+=1 #incrementing the count
print("\nThe number of spaces in the file is:",space_count)
f1.close()
f1=open("test.txt","r")
#Opening the file to read contents in reverse order
text=f1.read()
#reads each line at a time and stores in variable i
text=text[::-1]#reverses the string
print("\nContents of file in reverse order: ",text)
f1.close()
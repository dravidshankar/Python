# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:10:37 2018

@author: user
"""

# -*- coding: utf-8 -*-
"""
Copying the contents of one file to another in reverse order of lines
Created on Sun Nov 25 17:49:38 2018

@author: user
"""

f=open("test.txt","r")
text=f.read()
print("Printing the contents of file:")
print(text)
f.close()
f1=open("test.txt","r")
f2=open("reverse_line.txt","w")
new_text=""
for i in f1.readlines():
    new_text= i+new_text
f2.write(new_text)
f1.close()
f2.close()
f3=open("reverse_line.txt","r")
text=f3.read()
print("\nPrinting the contents of new file:\n")
print(text)

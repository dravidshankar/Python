
"""
Copying the contents of one file to another in reverse order of lines

"""

f=open("test.txt","r")
#opening the file test.txt in read mode
text=f.read()
#reading the contents and store in 'text'
print("Printing the contents of file:")
print(text)
f.close()
f1=open("test.txt","r")
f2=open("reverse_line.txt","w")
#opening a new file reverse_line.txt
new_text=""#initialize with a null character
for i in f1.readlines():
# reads each line at a time and stores in 'i'
    new_text= i+"\n"+new_text
    #concatenating the contents in reverse order of lines
f2.write(new_text)
#written h=the contents into file reverse_line.txt
f1.close()
f2.close()
f3=open("reverse_line.txt","r")
#opening the file to read the contents
text=f3.read()
print("\nPrinting the contents of new file:\n")
print(text)
f3.close()
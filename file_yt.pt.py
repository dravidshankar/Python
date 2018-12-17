#File Operations in python
file=open("test.txt","w")#use open function. 
#Pass two arguments: filename and mode
#Type of both arguments should be string
#file : file object created 
#Modes: "r" -> read, "w"->write, "a"-append
file.write("Good morning")
#call the method write using the file object
file.close()
#close the file after performing write
f=open("test.txt","r")
#used different name for file object 'f'
#opened the file in read mode
content=f.read()
#stored contents of file in  variable content
print(content)
#printed the contents
f.close()


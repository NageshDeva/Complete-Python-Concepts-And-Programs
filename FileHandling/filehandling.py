#fileHandling
'''
2types of files
1. Text files
2. Binary files

There are operations for Text files
r--> open an existing file for read operation. The file pointer positioned at the beggining of the file
Default mode.

w--> open an existing file with write operation, if file already
contains overrides existing data. if specified file not available then this mode creates a new file.

a--> open an existing file for append operation. it wont override existing data, if 
specified file not available then this mode creates a new file.

r+--> To read and write data into the file. The previous data in the file will not be deleted
The file pointer placed at the beginning of the file.

w+-->To write and read data. it will override existing data.

a+-->To append and read data from the file. it wont override existing data.

x-->to open a file in exclusive creation mode for write operation. if the file exists then we will get fileExistsError

opening a file: f=open("filename","mode")

Modes for Binary files.
Ex: rb, wb, ab, r+b, w+b, a+b, xb

closing a file: f.close()
'''
f = open("abc.txt","w")
f.write("Nagesh\n")
f.write("Deva\n")
f.write("Hyderabad\n")
print("Data written to the file successfully")
f.close()

'''
read()--> to read total data from the file.
read(n)--> to read 'n' characters from the file.
readline()--> to read only one line.
readlines()--> to read all lines into a list.
'''
#to read only first 10 characters.
f=open("abc.txt","r")
data = f.read(10)
print(data)
f.close()

# to read data line by line.
f=open("abc.txt","r")
line1 = f.readline()
print(line1,end='')
line2 = f.readline()
print(line2,end='')
line3 = f.readline()
print(line3,end='')
f.close()



#read(n)--> we can specify till what no.of characters we need this read
f = open("abc.txt","r")
print(f.read(3))
print(f.readline())
print(f.read(4))
print("Remaining Data")
print(f.read())



#The with statement:
'''
it can be used while opening a file. we can use this to group file operation statements within a block.
The advantage of with statement is it will take care closing of of file, after completing operations automatically.
'''
with open("abc.txt", "w") as f:
    f.write("Nagesh\n")
    f.write("Deva\n")
    f.write("Hyderabad\n")
    print("is file closed:", f.closed)
print("is file closed:", f.closed)

#The seek() and tell() methods:
'''
tell()--> to return current position of the cursor from the beginning of the file.
seek()--> This method to move cursor to specified location.
f.seek(offset, fromwhere)-->offset represents no.of positions.
0-->from the begining of file (Default value)
'''
f= open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())    
print(f.read(3))
print(f.tell())


data = "Have a Happy day and start the day with a cup of coffee."
f = open("bbc.txt","w")
f.write(data)
with open("bbc.txt","r+") as f:
    text = f.read()
    print(text)
    print("The current cursor position is:", f.tell())
    f.seek(7)
    print("The current cursor position is:", f.tell())
    f.write("sad!!") 
    f.seek(0)
    text = f.read()
    print("Data after modification:")
    print(text)   


#To create Zip file:
'''
f=ZipFile("files.zip","w","ZIP_DEFLATED")   --> zip_defalted creates zip file.
once we create zipfile object, we can add files by using write method.
f.write(filename)
'''
from zipfile import*
f = ZipFile("files.zip","w",ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("files.zip file created successfully")


#To perform unzip operation:
'''f=ZipFile("files.zip", "r", ZIP_STORED)
ZIP_STORED represents unzip operation
'''

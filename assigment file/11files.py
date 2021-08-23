# 1. Write a program to read text file


f=open("sample.txt","r")
while True:
       line=f.readline()
       if line=='':break
       print (line)
f.close()

# 2. Write a program to write text to .txt file using InputStream


lines = ['sample', 'How to write text files in Python']
with open('sample.txt', 'w') as f:
    for line in lines:
        f.write("welcome in sample.txt :")
        f.write(line)
        f.write('\n')
f.close()
        
        
# 3. Write a program to read a file stream


f = open("abc.txt",'r')
data = f.read()
print(data)
f.close

# 4. Write a program to read a file stream supports random access

f = open("abc.txt",'r')
data = f.read()
data2 =f.seekable()
print(data)
print(data2)
f.close

# 5. Write a program to read a file a just to a particular index using seek()

with open("abc.txt","r+") as f:
    text=f.read()
    print(text)
    print("The Current Cursor Position: ",f.tell()) 
    f.seek(17)
    print("The Current Cursor Position: ",f.tell()) 
    f.write("KSS!!!") 
    f.seek(0) 
    text=f.read()
    print("Data After Modification:") 
    print(text) 
    
f.close()

# 6. Write a program to check whether a file is having read access and write access permissions

import os,sys
fname = input("enter file name :")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
else:
    print("file does not exist:",fname)
    sys.exit(0)
print("the content of file is:")
data=f.read()
print(data)
  
    
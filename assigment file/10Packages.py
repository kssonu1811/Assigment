
# 1. Create a program to create two class

class A:
    # 1.1. Create a constructor and a method for each class
    def __init__(self,Name,age,sal):
        self.name=Name
        self.age = age
        self.sal = sal
    def m1(self):
        print("name :",self.name)
        print("age :",self.age)
        print("sal :",self.sal)
        
# 1.3. Import the respective packages
from untitled17 import A
class B(A):
    #1.2. Create a __init__.py for adding all packages
    def __init__(self,Name,age,sal):
        A.__init__(self,Name,age,sal)
        
    def m2(self):
        self.m1()
#1.4. Call each class by creating an object to it 
obj = B("sajan",23,23000)
obj.m2()
         
"""
OUTPUT...

name : sajan
age : 23
sal : 23000
Reloaded modules: untitled17
name : sajan
age : 23
sal : 23000
name : sajan
age : 23
sal : 23000

"""
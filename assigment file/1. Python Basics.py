# 1. Write a program to print your name.
name = "sajan kumar"
print(name)

# 2. Write a program for a Single line comment and multi-line comments.
# this is single line Comment
"""
this is multi-line comment process
we can write multipul line in side in here
"""
#3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# int data type
int = 1234
print(type(int))
# Boolean datatype
bool = True
bool1 = False
print(type(bool))
print(type(bool1))
# char data type
str = "hello"
print(type(str))
# float data type
float = 1.234
print(type(float))
# double data type
"""Python does not have an inbuilt double data type, but it has a float type that designates a floating-point number. I can count double in Python as float values which are specified with a decimal point."""
data = 9.9
print(data)
print(type(data))
"""Python double star operator"""
x = 1
y = 2
c = x ** y 
print(c) 
z = 2 * (4 ** 2) + 3 * (4 ** 2 - 10) 
print(z)
"""Python double slash"""
print(3 / 2)
print(3 // 2)
# Define the local and Global variables with the same name and print both variables and understand the scope of the variables
""" Global Variable: Outside of all the functions
    Local Variable: Within a function block """
    
Global_Variable = 15
def GV (x):
    Local_Variable = 10
    print(x*Local_Variable)
GV(Global_Variable)


"""
Output
sajan kumar
<class 'int'>
<class 'bool'>
<class 'bool'>
<class 'str'>
<class 'float'>
9.9
<class 'float'>
1
50
1.5
1
150
"""
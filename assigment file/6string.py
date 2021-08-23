# 1. Different ways creating a string
""" Multipul way of creating string """
x ="hello"
y ='hello'
z=""" hello"""
s ='''hello'''
d=str("hello")
print(x,y,z,s,d)

# 2. Concatenating two strings using + operator
print(x+ "---" +y)

# 3. Finding the length of the string
asd =len(x)
print(asd)

# 4. Extract a string using Substring
""" 1. Extract Substring Using String Slicing in Python"""
# example -->
myString = "Mississippi"
print(myString[:]) # [start:stop:stap]
print(myString[4 : ])
print(myString[ : 8])
print(myString[2 : 7])
print(myString[4 : -1]) 
print(myString[-6 : -1])

""" Extract Substring Using the slice() Constructor in Python"""
# Example -->
""" use -> slice(start, stop, step) """
myString = "Mississippi"
slice1 = slice(3)
slice2 = slice(4)
slice3 = slice(0, 8)
slice4 = slice(2, 7)
slice5 = slice(4, -1)
slice6 = slice(-6, -1)
print(myString[slice1])
print(myString[slice2])
print(myString[slice3])
print(myString[slice4])
print(myString[slice5])
print(myString[slice6])

""" Extract Substring Using Regular Expression in Python"""
# Example -->
import re

string = "123AAAMississippiZZZ123"

try:
    found = re.search('AAA(.+?)ZZZ', string).group(1)
    print(found)
except AttributeError:
    pass


# 5. Searching in strings using index()
"""
x = str(input("enter string eliment :"))
y = int(input("searching index number :")) - 1
print(x[y])

"""

# 6. Matching a String Against a Regular Expression With matches()

import re
line = "pet:cat I love cats"
mat = re.match(r"pet:\w\w\w",line)
print(mat.group(0))

# 7. Comparing strings
""" multiple way of comparing
1: Using Relational Operators
2: Using is and is not 
3: Creating a user-defined function.
"""
# example -->
print("sajan" == "sajan")
print("sajan" < "sajan")
print("sajan" > "sajan")
print("sajan" != "sajan")

# 8. startsWith(), endsWith() and compareTo()
str = "sajanforsajan"
print(str.startswith("sajan"))
print(str.startswith("sajan", 3, 10))
print(str.startswith("sajan", 8, 14))

  
print(str.endswith("sajan"))
print(str.endswith("sajan", 2, 8))
print(str.endswith("for", 5, 8))

# 9. Trimming strings with strip()
"""strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
   rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
   lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.
   """
   
# Example -->
s1 = '  abc  '

print(f'String =\'{s1}\'')

print(f'After Removing Leading Whitespaces String =\'{s1.lstrip()}\'')

print(f'After Removing Trailing Whitespaces String =\'{s1.rstrip()}\'')

print(f'After Trimming Whitespaces String =\'{s1.strip()}\'')

# 10. Replacing characters in strings with replace()

string = "sajan for kss kss kss kss"
print(string.replace("kss", "sajan"))

# 11. Splitting strings with split()
""" special character or identified character removing and put in list data"""
# Example -->
word = 'sajan:for:anshu'
print(word.split(':'))
"""
# 12. Converting integer objects to Strings
y = 23
z = str(y)
print(type(z))
int_list_data  = input("Enter integer element of list data seperate with space :")
x = int_list_data.split()
data=[]
for i in range(0,len(x)):
    x[i] = str(x[i])
print(x)

"""
# 13. Converting to uppercase and lowercase
name = "SAJANKUMARSINGH"
print(name.lower())

""" OUTPUT....

hello hello  hello hello hello
hello---hello
5
Mississippi
issippi
Mississi
ssiss
issipp
ssipp
Mis
Miss
Mississi
ssiss
issipp
ssipp
Mississippi
pet:cat
True
False
False
False
True
False
True
True
False
True
String ='  abc  '
After Removing Leading Whitespaces String ='abc  '
After Removing Trailing Whitespaces String ='  abc'
After Trimming Whitespaces String ='abc'
sajan for sajan sajan sajan sajan
['sajan', 'for', 'anshu']
sajankumarsingh

"""
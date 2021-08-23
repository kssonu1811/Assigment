# 1. Write a program to generate Arithmetic Exception without exception handling

# ---> numeric calculations error known as Arithmetic Exception like  OverflowError, ZeroDivisionError, FloatingPointError

""" Example -->
y = 12/0
print(y)

OUTPUT --- ZeroDivisionError: division by zero
"""
import sys
try:
    7/0
except ArithmeticError as e:
    print(e)
    print(sys.exc_info())
    print('This is an example of catching ArithmeticError')
    
# 2. Handle the Arithmetic exception using try-catch block
try:
    x = int(input("Enter required number :"))
    y = int(input("enter required number :"))
    z = x/y
    print("the result is : ",int(z))
except ZeroDivisionError:
    print("You can not devide by Zero.")
    print("ExceptDisplay")

# 3. Write a method which throws exception, Call that method in main class without try block

class tooyoung(Exception):
    def __init__(self, args):
        self.msg = args
class tooold(Exception):
    def __init__(self, args):
        self.msg = args
age = int(input("Enter age :"))
if age>60:
    raise tooyoung("Plz wait some more time you will get best match soon!!!")
elif age<18:
    raise tooold("Your age already crossed marriage age...no chance of getting marriage")
else:
    print("You will get match details soon by email!!!") 
    
    
    
# 4. Write a program with multiple catch blocks

try :
    print("outer try block.")
    try:
        print("inner try block.")
        print(10/0)
    except ZeroDivisionError:
        print("inner exept block.")
    finally:
        print("inner finally block.")
except :
    print("output except block")
finally:
    print("outer finally block")
    
#5. Write a program to throw exception with your own message

try:
    print("inner try block.")
    print(10/0)
except ZeroDivisionError:
    print("inner exept block.")
finally:
    print("inner finally block.")

# 6. Write a program to create your own exception
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

# 7. Write a program with finally block

try:
    print("inner try block.")
    print(10/0)
except ZeroDivisionError:
    print("inner exept block.")
finally:
    print("inner finally block.")
    
# 8. Write a program to generate Arithmetic Exception

try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")
finally:
    print("exception")

# 9. Write a program to generate FileNotFoundException

try:
    file = open ("abcd.txt", 'r')
except FileNotFoundError:
    print ("File is not present, skipping the reading process...")
else:
    print (file.read())
    file.close()


# 10. Write a program to generate ClassNotFoundException
""" mostly these type exception come in java ."""










# 11. Write a program to generate IOException

file = open ("abcd.txt", 'r')
try:
	file.write("hello world")
except IOError:
	print ("Write operation: Failed")
else:
	print ("Write operation: Succeful")
finally:
	print ("Inside finally ...")
	file.close()

# 12. Write a program to generate NoSuchFieldException

""" theseone also unknown for me"""


"""
Output...

division by zero
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000001AD4189E508>)
This is an example of catching ArithmeticError

Enter required number :10

enter required number :10
the result is :  1

Enter age :54
You will get match details soon by email!!!
outer try block.
inner try block.
inner exept block.
inner finally block.
outer finally block
inner try block.
inner exept block.
inner finally block.

Enter a number: 12
This value is too large, try again!


Enter a number: 10
Congratulations! You guessed it correctly.
inner try block.
inner exept block.
inner finally block.
This statement is raising an arithmetic exception.
exception
File is not present, skipping the reading process...

"""

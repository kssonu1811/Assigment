# 1. Write a function for arithmetic operators(+,-,*,/)
x = int(input("Enter first int value :"))
y = int(input("Enter second int value :"))
def add_sub_mul_dev(t,v):
    print("addition of both :",t+v)
    print("difference between both :", t-v)
    print("multiplication of both :", t*v)
    print("division of {} and {} in flotting value :".format(t, v), t/v)
add_sub_mul_dev(x,y)

# 2. Write a method for increment and decrement operators(++, --)
z = x
x= x+1
z= z-1
print("increment value is {}".format(x),"decriment value is {}".format(z))

# 3. Write a program to find the two numbers equal or not.
s = input("Enter the first number: ")
d = input("Enter the second number: ")
if s == d:
  print("Both inputs are equal")
else:
  print("Your input is not equal.")

# 4. Program for relational operators (<,<==, >, >==)
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if a <= b:
    print("{} is less then and equal to {}".format(a,b))
    if a < b:
       print("{} is less then {}".format(a,b))
if a >= b:
    print("{} is greater then and equal to {}".format(a,b))
    if a > b :
        print("{} is greater then {}".format(a,b))
        

# 5. Print the smaller and larger number
ls =input("enter int element of list data seperate by space :")
ad = ls.split()
for i in range(0,len(ad)):
    ad[i] = int(ad[i])
print("max value is :", max(ad),"min value is :", min(ad))

"""
Output
Enter first int value :43

Enter second int value :12
addition of both : 55
difference between both : 31
multiplication of both : 516
division of 43 and 12 in flotting value : 3.5833333333333335
increment value is 44 decriment value is 42

Enter the first number: 12

Enter the second number: 13
Your input is not equal.

Enter the first number: 32

Enter the second number: 43
32 is less then and equal to 43
32 is less then 43

enter int element of list data seperate by space :12 34 5 23 54
max value is : 54 min value is : 5
"""
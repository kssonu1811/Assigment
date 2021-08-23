# 1. Write a program to print “Bright IT Career” ten times using for loop
x = "Bright IT Career"
i = 0
while i < 10:
    print(x)
    i += 1
    
# 2. Write a program to print 1 to 20 numbers using the while loop.
s = 1
while s <= 20:
    print(s)
    s += 1
    
# 3. Program to equal operator and not equal operators
a = int(input("Enter first digit :"))
b = int(input("enter second digit :"))
if a ==b :
    print("both digit is same")
if a !=b:
    print("both digit is not same")
   
# 4. Write a program to print the odd and even numbers.
s = int(input("Enter number :"))
if s % 2 == 0:
    print(s ,"is even number")
else:
    print(s,"is not even number")
    
# 5. Write a program to print largest number among three numbers.
f = int(input("Enter number :"))
g = int(input("Enter number :"))
h = int(input("Enter number :"))
if (f >= g) and (f>=h):
    largest = f
elif (g>=f) and (g>=h):
    largest = g
else:
    largest = h
print(largest, "is largest number")

# 6. Write a program to print even number between 10 and 20 using while
i = 10
while i<=20:
    if (i%2)==0:
        print(i,"is even number.")
    else:
        print(i,"is not odd number.")
    i += 1
    
# 7. Write a program to print 1 to 10 using the do-while loop statement.
i = 1
while True:
    print(i)
    i +=1
    if i==11:
        break
 
# 8. Write a program to find Armstrong number or not
num = int(input("enter number :"))
order = len(str(num))
i = 0
di = num
while di > 0 :
    d = di % 10
    i += d ** 3
    di = di // 10
    
if num == i :
    print(num, "is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
    

# 9. Write a program to find the prime or not.
num = int(input("Enter number :"))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break   
    else:
        print(num, "is a prime number")
# 10. Write a program to palindrome or not.
x = int(input("Enter number :"))
rev = 0
y = x
while y>0 :
    rev =(rev*10)+y%10
    y = y//10
if rev == x:
    print(x ,"is palindrome number")
else:
    print(x,"is not palindrome number")
# 2nd method
z =str(x)
d = (z[::-1])
if z == d:
    print(x ,"is palindrome")
else:
    print(x,"is not palindrome")
    
# 11. Program to check whether a number is EVEN or ODD using switch
print ("Enter an integer number to check Odd or Even :\n")
x = int (input ())
if (x % 2 == 0):
    print ("The input number is even.\n")
else:
    print ("The input number is odd.\n")

# 12. Print gender (Male/Female) program according to given M/F using switch




""" OUTPUT.....

Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
Bright IT Career
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

Enter first digit :12

enter second digit :13
both digit is not same

Enter number :12
12 is even number

Enter number :12

Enter number :13

Enter number :3
13 is largest number
10 is even number.
11 is not odd number.
12 is even number.
13 is not odd number.
14 is even number.
15 is not odd number.
16 is even number.
17 is not odd number.
18 is even number.
19 is not odd number.
20 is even number.
1
2
3
4
5
6
7
8
9
10

enter number :153
153 is an Armstrong number

Enter number :43
43 is prime number

Enter number :151
151 is palindrome number
151 is palindrome
Enter an integer number to check:


5
The input number is odd.

"""

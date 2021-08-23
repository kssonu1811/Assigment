# 1. Write a function to add integer values of an array
lis = input("enter int element of array data :")
x = lis.split()
su = 0
for i in range(0,len(x)):
    x[i] = int(x[i])
    su = su + x[i]
print("sum of array data is",su)
# second method
import numpy
y = numpy.array(x)
su = 0
for i in range(0,len(x)): 
    su = su + x[i]
print("sum of array data is",su)

# 2. Write a function to calculate the average value of an array of integers
lis = input("Enter int element of array data :")
x = lis.split()
su =0
for i in range(0,len(x)):
    x[i] = int(x[i])
    su = su + x[i]
average = su/(len(x)+1)
print("average value of given number is ",average)
# second method
y = x
ave = sum(x)/(len(x)+1)
print("average value of given number is ",ave)

# 3. Write a program to find the index of an array element
lis = input("Enter int element of array data :")
x = lis.split()
y = input("enter find element index :")
z = x.index(y)
print(z)


# 4. Write a function to test if array contains a specific value
arry = input("Enter int element of array data seperate by space :")
x = arry.split()
y = input("Enter special value :")
z = y in x
print(z)

# 5. Write a function to remove a specific element from an array   
arry = input("Enter int element of array data seperate by space :")
x = arry.split()
y = input("Enter removal element :")
x.remove(y)
print(x)

# 6. Write a function to copy an array to another array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()  
arr2 = [None] * len(arr1)
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i]        
print("Elements of old array: ",arr1)   
print("Elements of new array: ",arr2)

# 7. Write a function to insert an element at a specific position in the array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split() 
ele = int(input("enter intiger index where we want insert eement :"))
el = ele - 1
data = int(input("enter element :"))
print(arr1, "is old array data")
arr1.insert(el, data)
print(arr1," is new array data")

# 8. Write a function to find the minimum and maximum value of an array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0,len(arr1)):
    arr1[i] = int(arr1[i])
x = arr1
print("maximum value of array is",max(x))
print("minimum value of given array is", min(x))

# 9. Write a function to reverse an array of integer values
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0,len(arr1)):
    arr1[i] = int(arr1[i])
x = arr1[::-1]
print(x)


# 10. Write a function to find the duplicate values of an array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0, len(arr1)):
    for j in range(i+1, len(arr1)):
        if arr1[i] == arr1[j]:
            print(arr1[j])
            

# 11. Write a program to find the common values between two arrays
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
arry1 = input("Enter int element of array data seperate by space :")
arr2 = arry1.split()
for i in range(0, len(arr1)):
    for j in range (0, len(arr2)):
        if arr1[i] == arr2[j]:
            print(arr2[j]," is common value")
            break


# 12. Write a method to remove duplicate elements from an array

arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
data = []
for i in arr1:
    if i not in data:
        data.append(i)
print(data)


# 14. Write a method to find the second largest number in an array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0, len(arr1)):
    arr1[i] = int(arr1[i])
z = sorted(arr1)
print(z[-2])

# 15. Write a method to find number of even number and odd numbers in an array
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0, len(arr1)):
    arr1[i] = int(arr1[i])
for i in range(0, len(arr1)):
    if arr1[i] % 2 ==0:
        print(arr1[i]," is even number")
    else:
        print(arr1[i],"is odd number")
        

# 16. Write a function to get the difference of largest and smallest value
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0, len(arr1)):
    arr1[i] = int(arr1[i])
z = sorted(arr1)
dif = z[-1]-z[0]
print(dif," difference of largest and smallest value")


# 17. Write a method to verify if the array contains two specified elements(12,23)
arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
for i in range(0,len(arr1)):
    arr1[i] = str(arr1[i])
if "12" and "23" in arr1:
    print("inside array data having 12 and 23")
else:
    print("inside array data not having 12 and 23")

# 18. Write a program to remove the duplicate elements and return the new array

arry = input("Enter int element of array data seperate by space :")
arr1 = arry.split()
data = []
for i in arr1:
    if i not in data:
        data.append(i)
print("old array data is", arr1)
print("new array data is", data)




""" OUTPUT 



enter int element of array data : 1 2 3 4 5
 15
15

Enter int element of array data :1 2 3 4 5 6
average value of given number is  3.0
average value of given number is  3.0

Enter int element of array data :1 2 3 4 5 

enter find element index :3
2

Enter int element of array data seperate by space :1 2 3 4 5 6 6

Enter special value :6
True

Enter int element of array data seperate by space :1 2 3 4 5

Enter removal element :3
['1', '2', '4', '5']

Enter int element of array data seperate by space :1 2 3 4 5
Elements of old array:  ['1', '2', '3', '4', '5']
Elements of new array:  ['1', '2', '3', '4', '5']

Enter int element of array data seperate by space :1 2 3 4 5 6 7

enter intiger index where we want insert eement :2

enter element :19
['1', '2', '3', '4', '5', '6', '7'] is old array data
['1', 19, '2', '3', '4', '5', '6', '7']  is new array data

Enter int element of array data seperate by space :1 2 3 4 5 4 3 76
maximum value of array is 76
minimum value of given array is 1

Enter int element of array data seperate by space :1 2 3 4 5 6
[6, 5, 4, 3, 2, 1]

Enter int element of array data seperate by space :1 2 3 4 5 4 3
3
4

Enter int element of array data seperate by space : 1 2 3 4

Enter int element of array data seperate by space :3 4 5 6 78
3  is common value
4  is common value

Enter int element of array data seperate by space :1 2 3 4 5 6
['1', '2', '3', '4', '5', '6']

Enter int element of array data seperate by space :1 2 3 4 5
4

Enter int element of array data seperate by space :1 2 3 4 5 6 7 7
1 is odd number
2  is even number
3 is odd number
4  is even number
5 is odd number
6  is even number
7 is odd number
7 is odd number

Enter int element of array data seperate by space :1 2 3 4 5 6 7 8 9
8  difference of largest and smallest value

Enter int element of array data seperate by space :1 2 12 3 4 5 23
inside array data having 12 and 23

Enter int element of array data seperate by space :1 2 3 4 5 3 4 5 2 34 5 6 7 8
old array data is ['1', '2', '3', '4', '5', '3', '4', '5', '2', '34', '5', '6', '7', '8']
new array data is ['1', '2', '3', '4', '5', '34', '6', '7', '8']

"""
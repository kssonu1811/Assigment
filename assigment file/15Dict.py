# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name

di ={} # or di = dic()
di["name"] = input("Enter your name :")
di["id"] = input("Enter your id :")
di["email"] = input("Enter email id :")
di["age"] = int(input ("Enter your age intiger value aplicable :"))
di["sal"] = int(input("Enter selary intiger value aplicable :"))
di["loc"] = input("Enter job location :")
print(di)

# 1.1. Adding the values in dictionary

di["home town"] = input("enter home town :")
print(di)

# 1.2. Updating the values in dictionary
di["age"] = int(input ("Enter your current age intiger value aplicable :"))
di["sal"] = int(input("Enter your current selary intiger value aplicable :"))
print(di)

# 1.3. Accessing the value in dictionary
print(di["name"])
print(di["id"])
print(di["email"])
print(di["age"])
print(di["sal"])
print(di["loc"])

# 1.4. Create a nested loop dictionary

index_dic = {}
lis = [None]*len(di)
for i in range(0,len(di)):
    lis[i] = i
print(lis) 
for key , ele in zip(lis,di.items()):
    index_dic[key] = dict([ele])
print(index_dic)

# 1.5. Access the values of nested loop dictionary

for p_id, p_info in index_dic.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
        
# 1.6. Print the keys present in a particular dictionary

for p_id, p_info in index_dic.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print("this id's key is :", key)
        
# 1.7. Delete a value from a dictionary


index_dic.pop(6)
print(index_dic)


"""
Output --->

Enter your name :sajan kumar

Enter your id :2002

Enter email id :kss@gmail.com

Enter your age intiger value aplicable :22

Enter selary intiger value aplicable :23000

Enter job location :hyd
{'name': 'sajan kumar', 'id': '2002', 'email': 'kss@gmail.com', 'age': 22, 'sal': 23000, 'loc': 'hyd'}

enter home town :bgp
{'name': 'sajan kumar', 'id': '2002', 'email': 'kss@gmail.com', 'age': 22, 'sal': 23000, 'loc': 'hyd', 'home town': 'bgp'}

Enter your current age intiger value aplicable :23

Enter your current selary intiger value aplicable :24000
{'name': 'sajan kumar', 'id': '2002', 'email': 'kss@gmail.com', 'age': 23, 'sal': 24000, 'loc': 'hyd', 'home town': 'bgp'}
sajan kumar
2002
kss@gmail.com
23
24000
hyd
[0, 1, 2, 3, 4, 5, 6]
{0: {'name': 'sajan kumar'}, 1: {'id': '2002'}, 2: {'email': 'kss@gmail.com'}, 3: {'age': 23}, 4: {'sal': 24000}, 5: {'loc': 'hyd'}, 6: {'home town': 'bgp'}}

Person ID: 0
name: sajan kumar

Person ID: 1
id: 2002

Person ID: 2
email: kss@gmail.com

Person ID: 3
age: 23

Person ID: 4
sal: 24000

Person ID: 5
loc: hyd

Person ID: 6
home town: bgp

Person ID: 0
this id's key is : name

Person ID: 1
this id's key is : id

Person ID: 2
this id's key is : email

Person ID: 3
this id's key is : age

Person ID: 4
this id's key is : sal

Person ID: 5
this id's key is : loc

Person ID: 6
this id's key is : home town
{0: {'name': 'sajan kumar'}, 1: {'id': '2002'}, 2: {'email': 'kss@gmail.com'}, 3: {'age': 23}, 4: {'sal': 24000}, 5: {'loc': 'hyd'}}

"""
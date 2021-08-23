# 1. Define a static variable and access that through a class 
""" 
Static Variables (Class Level Variables):-
  If the value of a variable is not varied from object to object, such type of variables we have to 
declare with in the class directly but outside of methods. Such type of variables are called Static 
variables.
Example :-
"""
class add:
    class_veriable1 = 50
    class_veriable2 = 200
print(add.class_veriable1 + add.class_veriable2)


# 2. Define a static variable and access that through a instance
class Fruits(object):
       count = 3
       def __init__(self, name, count):
             self.name = name
             self.count = count
             Fruits.count = Fruits.count + count # static variable uses in instance

def main():
    apples = Fruits("apples", 12);
    pears = Fruits("pears", 8);
    print (apples.count)
    print (pears.count)
    print (Fruits.count)
    print (apples.__class__.count) 
    print (type(pears).count) 

if __name__ == '__main__':
    main()
    
# 3. Define a static variable and change within the instance
class CSStudent:
    stream = 'cse'
    def __init__(self,name,roll,branch):
        self.name = name            
        self.roll = roll
        self.branch = branch
    def m1(self):
        print(self.name,self.roll,self.branch)
x = CSStudent.stream
a = CSStudent('Geek', 1, x)
b = CSStudent('Nerd', 2, x)
a.m1()
b.m1()
print(a,b)


# 4. Define a static variable and change within the class

""" PYTHON having three types of variable
1 instance variable  (Object Level Variables)
      a. -> 1. Inside Constructor by using self variable
      
"""
# Example ->
class employee:
    def __init__(self):
        self.eno = 101
        self.ename = "Sajan"
        self.sal = 20000
e = employee()
print(e.__dict__)

"""
      b. -> 2. Inside Instance Method by using self variable
      """
# Example ->
class employee:
    def __init__(self):
        self.eno = 101
        self.ename = "Sajan"
        self.sal = 20000
    def m1(self):
        self.email = "ksajansonu@gmail.com"
e = employee()
e.m1()
print(e.__dict__)

"""
      c. -> 3. Outside of the class by using object reference variable
      """
# Example ->
class employee:
    def __init__(self):
        self.eno = 101
        self.ename = "Sajan"
        self.sal = 20000
    def m1(self):
        self.email = "ksajansonu@gmail.com"
e = employee()
e.m1()
e.phone = 9416721138
print(e.__dict__)
 

"""     
2. Static Variables (Class Level Variables)
"""
class employee:
    title = "Singh"
    def __init__(self):
        self.eno = 101
        self.ename = "Sajan"
        self.sal = 20000
    def m1(self):
        self.email = "ksajansonu@gmail.com"
x= employee()
e = employee()
e.m1()
e.phone = 9416721138
print(e.__dict__,x.title)
 
"""      
3. Local variables (Method Level Variables)
"""
# Example ->
class employee:
    def __init__(self):
        self.eno = 101
        self.ename = "Sajan"
        self.sal = 20000
    def m1(self):
        local_variable = 5000
        self.email = "ksajansonu@gmail.com"
        print("new salary is :",self.sal + local_variable)
e = employee()
e.m1()
e.phone = 9416721138
print(e.__dict__)

""" Output...
250
12
8
23
23
23
Geek 1 cse
Nerd 2 cse
<__main__.CSStudent object at 0x000001E6FCC8F648> <__main__.CSStudent object at 0x000001E6FC87B508>
{'eno': 101, 'ename': 'Sajan', 'sal': 20000}
{'eno': 101, 'ename': 'Sajan', 'sal': 20000, 'email': 'ksajansonu@gmail.com'}
{'eno': 101, 'ename': 'Sajan', 'sal': 20000, 'email': 'ksajansonu@gmail.com', 'phone': 9416721138}
{'eno': 101, 'ename': 'Sajan', 'sal': 20000, 'email': 'ksajansonu@gmail.com', 'phone': 9416721138} Singh
new salary is : 25000
{'eno': 101, 'ename': 'Sajan', 'sal': 20000, 'email': 'ksajansonu@gmail.com', 'phone': 9416721138}
"""
 

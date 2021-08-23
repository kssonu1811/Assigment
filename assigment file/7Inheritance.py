"""
A, B and C are classes

A is a super class. B is a sub class of A. C is a sub class of B. 

Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C


"""
class A():
    def m1(self):
        print("this class is grandparent class 1st method.")
    def m2(self):
        print("this class is grandparent class 2st method.")
    def m3(self):
        print("this class is grandparent class 3st method.")
class B(A):
    def m4(self):
        print("this class is parent class 1st method.")
    def m5(self):
        print("this class is parent class 2st method.")
class C(B):
    def m7(self):
        print("this class is child class 1st method.")
    def m8(self):
        print("this class is child class 2st method.")
x = C()
x.m1()
x.m2()
x.m3()
x.m4()
x.m5()
x.m7()
x.m8()


# Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.

class main_class_method(C,B,A):
    def main(self):
        x = C()
        x.m1()
        x.m2()
        x.m3()
        x.m4()
        x.m5()
        x.m7()
        x.m8()
        y = B()
        y.m1()
        y.m2()
        y.m3()
        y.m4()
        y.m5()
        z = A()
        z.m1()
        z.m2()
        z.m3()
if __name__=="__main__":
    main_class_method().main()


# Call an overridden method with super class reference to B and C class’s objects

x = C()
x.m1()
x.m2()
x.m3()
y = B()
y.m1()
y.m2()
y.m3()


# Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members

class Parent(object):
     def __init__(self):
         self.value = 4
     def get_value(self):
         return self.value
 
class Child(Parent):
     def get_value(self):
         return self.value + 1
c = Child()
print(c.get_value())


""" OUTPUT...

this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
this class is parent class 1st method.
this class is parent class 2st method.
this class is child class 1st method.
this class is child class 2st method.
this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
this class is parent class 1st method.
this class is parent class 2st method.
this class is child class 1st method.
this class is child class 2st method.
this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
this class is parent class 1st method.
this class is parent class 2st method.
this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
this class is grandparent class 1st method.
this class is grandparent class 2st method.
this class is grandparent class 3st method.
5


"""
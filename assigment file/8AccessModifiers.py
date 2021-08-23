# 1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method. Create a sub class and try to access the private fields and methods from sub class.

# class with PRIVATE fields,
class private_class():
    __name = None
    __roll = None
    __branch = None
    
    # constructor
    def __init__(self,name,roll,branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
        
    # private method function   
    def __display(self):
        # accessing private data
        print("name :", self.__name)
        print("roll :",self.__roll)
        print("branch :",self.__branch)

    # main method
    def main(self):
        self.__display()
        
obj = private_class("sajan kumar", 2002, "E.E")
if __name__=="__main__":
    obj.main()
    
#Create a sub class and try to access the private fields and methods from sub class.
"""
class sub_class(private_class):
    def main(self):
        self.__display()
        
obj1 = sub_class("sajan kumar", 2002, "E.E")
if __name__=="__main__":
    obj1.main()
    
"""


# 2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.   
class protected():
    # protected data
    _name = None
    _roll = None
    _branch = None
    
    # constructor
    def __init__(self,name,roll,branch):
        self._name = name
        self._roll = roll
        self._branch = branch
        
    # protected method
    def _display(self):
        print("Name :", self._name)
        print("Roll :",self._roll)
        
class p_r(protected):
    # constructor
    def __init__(self, name, roll, branch):
        protected.__init__(self, name, roll, branch)
        
    # public method function
    def display_detail(self):
        self._display()
        print("Branch :",self._branch)
        
obj3 = p_r("sajan kumar",2002,"E.E")
obj3.display_detail()
        
# Also, Access the PROTECTED fields and methods from child class located in a different package

from AccessModifiers import p_r
obj4 = p_r("sajan kumar",2002,"E.E")
obj4.display_detail()


# Access the PROTECTED fields and methods from any class in different package


from AccessModifiers import protected

class o_m(protected):
    def __init__(self, name, roll, branch):
        protected.__init__(self, name, roll, branch)
        
    # public method function
    def display(self):
        self._display()
        print("Branch :",self._branch)
        
obj5 = o_m("sajan kumar",2002,"E.E")
obj5.display()


# 3. Create a class with PUBLIC fields and methods.

class public():
    # constructor
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender = gender
        
    #public method
    def displayage(self):
        print("Age",self.age)
        
obj = public("sajan",23,"Male")
print("Name :",obj.name)
obj.displayage()
print("Gender :",obj.gender)

#Access the public methods and fields from any class in the same package or different package.

from AccessModifiers import public
class new_pac_cl(public):
    def __init__(self, name, age, gender):
        public.__init__(self, name, age, gender)
        
    # public method function
    def display(self):
        print("Name",self.name)
        self.displayage()
        print("Gender :",self.gender)
        
obj = new_pac_cl("sajan",23,"Male")
obj.display()
"""

OUTPUT

Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan
Age 23
Gender : Male
Name sajan
Age 23
Gender : Male
Reloaded modules: AccessModifiers
name : sajan kumar
roll : 2002
branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan
Age 23
Gender : Male
Name sajan
Age 23
Gender : Male
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan kumar
Roll : 2002
Branch : E.E
Name : sajan
Age 23
Gender : Male
Name sajan
Age 23
Gender : Male

"""


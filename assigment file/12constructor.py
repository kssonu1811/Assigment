# 1. Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class

class kss:
    first = 0
    second = 0
    def __init__(self, f, s):
        self.first = f
        self.second = s
        
    def display(self):
        print("first number = ",str(self.first))
        print("second number = ",str(self.second))
class kss1(kss):
    def main(self):
        self.display()
       
obj = kss1("sajan","kumar")
if __name__=="__main__":
    obj.main()
   
# 2. Call the constructors(both default and argument constructors) of super class from a child class

class grandchild(kss1):
    def __init__(self, f, s):
        kss1.__init__(self, f, s)
    
    def display(self):
        self.display()
obj1 = grandchild("sajan","kumar")
obj1.display()
    

# 3. Apply private, public, protected and default access modifiers to the constructor

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
    
# public

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

# protected

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



# 4. Write a program which illustrates the concept of attributes of a constructor.

class Addition:
    first = 0
    second = 0
    answer = 0
     
    def __init__(self, f, s):
        self.first = f
        self.second = s
     
    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))
 
    def calculate(self):
         self.answer = self.first + self.second

obj = Addition(5000, 2000)

obj.calculate()

obj.display()

""" 
Output..

first number =  sajan
second number =  kumar
name : sajan kumar
roll : 2002
branch : E.E
Name : sajan
Age 23
Gender : Male
Name : sajan kumar
Roll : 2002
Branch : E.E
First number = 5000
Second number = 2000
Addition of two numbers = 7000

"""
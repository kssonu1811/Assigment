# 1. Create an abstract class with abstract and non-abstract methods.
# abstract
from abc import abstractmethod

class Computer:
    @abstractmethod
    def process(self):
        print("hello")
    
class laptop(Computer):
    def process(self):
        print("it is highly useable.")
        
com=laptop()
com.process()
# non-abstract
class Computer1:

    def process(self):
        pass
    
class laptop1(Computer1):
    def process(self):
        print("it is highly useable.")
        
com=laptop1()
com.process()

# 2. Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods



class parent:      
    def kss(self):
        pass
 
class child(parent):
    def kss(self):
        print("child class")
 
print( issubclass(child, parent))

# 3. Create an instance for the child class in child class and call abstract methods

from abc import abstractmethod
class parent: 
    @abstractmethod 
    def kss(self):
        print("hello")
 
class child(parent):
    def kss(self):
        print("child class")
print( isinstance(child(), parent))

#4. Create an instance for the child class in child class and call non-abstract methods
class parent:      
    def kss(self):
        pass
 
class child(parent):
    def kss(self):
        print("child class")
        
print( isinstance(child(), parent))


"""

Output..

it is highly useable.
it is highly useable.
True
True
True

"""
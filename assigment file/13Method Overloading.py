# 1. Write two methods with the same name but different number of parameters of same type and call the methods 

class edpresso:
    name = 0
    sal = 0
    def __init__(self, name, sal):
        self.name = name
        self.sal =sal
    def hello(self):
        if self.name is not None:
            print('Hello ' + self.name)
        else:
            print('Hello ')
        if self.sal is not None:
            print('salary :' + str(self.sal))
        else:
            print('Hello ')

obj = edpresso(name ='Kadambini',sal = 20000)
obj.hello()


# 2. Write two methods with the same name but different number of parameters of different data type and call the methods 


class second:
    string = 0
    intiger = 0

    def __init__(self,string, intiger):
        self.string = string
        self.intiger = intiger
        
    def hi(self):
        if self.string is not None:
             y = type(self.string)
             print("{0} is {1} data".format(self.string,y))
        else:
            print('Hello ')
        if self.intiger is not None:
            z =type(self.intiger)
            print("{0} is {1} data".format(self.intiger,z))
        else:
            print('Hello ')
        
obj = second('Kadambini',20000)
obj.hi()


# 3. Write two methods with the same name and same number of parameters of same type 

class mytest:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def sum(self):
        if self.a != None and self.b!= None and self.c != None:
            print("The Sum of 3 Number is : ",self.a+self.b+self.c)
        elif self.a!=None and self.b!= None:
           print('The Sum of 2 Numbers:',self.a+self.b) 
        else: 
            print('Please provide 2 or 3 arguments') 
t = mytest(10,20,30)
t.sum()



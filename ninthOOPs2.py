#del keyword for object deletion
class student:
    def __init__(self,name):
        self.name=name
s1=student("Diya")
print(s1)
del s1 #here we have deleted our object
print(s1) #and here we are getting error

#delete object properties
class student:
    def __init__(self,name):
        self.name=name
s1=student("Diya")
print(s1.name)
del s1.name #here we have deleted our object property name or attribute
print(s1.name) #and here we are getting error

#creating private attribute which is only be accessible inside the class
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #adding two __ in attribute make it as private attribute which is not accessible outside the class
acc=account("mira","12345")
print(acc.acc_no) #this will print acc no
print(acc.__acc_pass) #this will throw error(AttributeError: 'account' object has no attribute '__acc_pass')
        
#but if we want to access this 

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset(self):
        print(self.__acc_pass)
acc=account("mira","12345")
print(acc.acc_no) 
print(acc.reset()) 

#creating private like method in class
class Person:
    __name="anonymous" #private attribute
     
    def __hello(self): #private method which is not directly accessible outside of class
        print("hello person!")
    
    def welcome(self): #using private method's output inside the normal method so we can call this and access the data
        self.__hello()
p1=Person()
p1.welcome()
    
# example of inheritance also (for single inheritance we can consider this program)

class Car:
    color="black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car): #inherited class 
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Prius")
print(car1.name) 
print(car2.name)
car1.start() #calling methods from parent class
car1.stop() #calling methods from parent class
print(car2.color)       

# Multi level Inheritance

class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car): #inherited class car
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar): #inherited class ToyotaCar (so toyota has inherited car class so all properties from class car we can use in this too)
    def __init__(self, type):
        self.type=type

car1=Fortuner("Petrol")
car1.start()

#Multiple Inheritance
class A:
    varA="Welcome to class A"
class B:
    varB="Welcome to class B"
class C(A,B): #inherited both class A and B 
    varC="Welcome to class C"
cls=C()
print(cls.varA)
print(cls.varB)
print(cls.varC)

#Super Method

class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car): #inherited class car
    def __init__(self,name,type):
        super().__init__(type) #accessing parent class method using super method
        self.name=name
        super().start() #accessing parent class method using super method

c1=ToyotaCar("Fortuner", "Electric")
print(c1.type)

#Accessing class with different ways

#first accessing through calling the class attribute inside the instance

class Person:
    name="anonymous"
    def changeName(self,name):
        Person.name=name #first way while accessing use class name

p1=Person()
p1.changeName("newname")
print(p1.name)

#second way we can provide class method
class Person:
    name="anonymous"
    def changeName(self,name):
        self.__class__.name=name #second way while accessing use __class__ 

p1=Person()
p1.changeName("NewName")
print(p1.name)

# Third way is to decorate as class method
class Person:
    name="anonymous"
    @classmethod
    def changeName(cls,name):
        cls.name=name #third way while accessing use __class__ 

p1=Person()
p1.changeName("NewName")
print(p1.name)


# @property decorator
#if we want to make a variable whose value or calculation depends on some variables and some change comes in that varibles and these needs to be change according to change we use @property decorator
#as we can create method where we are calculating percentage in init function but when we change marks the percentage varible taking old values
#we can solve this issue while creating new method and changing the varible byut the other way aroung in property decorator

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def Percentage(self):
        return str((self.phy+self.chem+self.math)/3) +"%"
stu1=Student(98,99,56)
print(stu1.Percentage)
stu1.phy=67
print(stu1.Percentage)

#Polymorphism
#in this code we are performing arithmatic operation on complex numbers using dunder functions

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real, "i +" ,self.img,"j")
    def __add__(self,num2): #Dunder Function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2): #Dunder Function
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

    
num1=Complex(3,6)
num1.showNumber()

num2=Complex(2,4)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num4=num1-num2
num4.showNumber()

#practice Questions

#Define a circle class to create a circle with radius r using the constructor.
#Define an area method of the class which calculates the area of the circle.
#Define a perimeter method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14 * self.r ** 2 #formula is Pi r square
    def perimeter(self):
        return 2 * 3.14 * self.r # 2 pi r

c1=Circle(3)

print(c1.area())
print(c1.perimeter())


#Define  a employee class with attribute role, department,salary This class also has showDetails() method.
#Creat an engineer class that inherits properties from employee and has addition attributes : name and age
class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showDetails(self):
        print("Role =", self.role)
        print("Department =",self.dept)
        print("Salary =",self.sal)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Devops","IT",60000)

eng1=Engineer("Elon",34)
eng1.showDetails()


#create a class called Order which stores item & its price.
#Use Dunder function __gt__() to convey that:
#order1>order2 if price of order1 > price of order 2

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price
        
ord1=Order("Chips",50)
ord2=Order("Biscuit",30)

print(ord1>ord2)


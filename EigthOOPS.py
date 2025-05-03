#Defining class
class Student:
    name="Robin"
#Calling class with object
s1=Student()
print(s1.name)

#Class with init function or constructor
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student in database")
s1=student("Rob", 88)
print(s1.name,s1.marks)
s2=student("riya", 98)
print(s2.name,s2.marks)

# class with default and parameterized constructor
class student:
    def __init__(self): #Default constuctor
        pass
    def __init__(self,name,marks): #parameterized constructor
        self.name=name
        self.marks=marks
        print("Adding new student in database")
s1=student("Rob", 88)
print(s1.name,s1.marks)
s2=student("riya", 98)
print(s2.name,s2.marks)


#Class attribute and object attribute
class student:
    college_name="Mumbai University"  #this is class attribute
    def __init__(self): #Default constuctor
        pass
    def __init__(self,name,marks): #parameterized constructor
        self.name=name  #this is object attribute (object attribute pref> class attribute i.e if same name attribute is created then object sttribute will be assigned if that is not given then class attribute will get fetched)
        self.marks=marks
        print("Adding new student in database")
s1=student("Rob", 88)
print(s1.name,s1.marks,s1.college_name)
s2=student("riya", 98)
print(s2.name,s2.marks,student.college_name)#this and above calling of attribute is same for class attribute


# Defining method in Class

class guest:
    ocassion ="party"
    def __init__(self,name,money):
        self.name=name
        self.money=money
    
    def welcome(self):
        print("welcome to our party: ",self.name)
    
    def get_money(self):
        return self.money

obj=guest("Riya",1000)
obj.welcome()
print(obj.get_money())

#-----------------------------Assignments-------------------------------------
# 1) create student class that takes name and marks of 3 subjects as argument in constructor then create a method to print the average

class subjects:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def getavg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi ",self.name, "You avg marks is ",sum/3)

sub=subjects("kajal",[87,67,55])
sub.getavg()
sub.name="Rohan" #updating attribute from object
sub.getavg()

#static method

class subjects:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod #decorator
    def hello():
        print("hello")

    def getavg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi ",self.name, "You avg marks is ",sum/3)

sub=subjects("kajal",[87,67,55])
sub.getavg()
sub.hello()
sub.name="Rohan" #updating attribute from object
sub.getavg()

#2) Crate a class account with two attributes - balance and account no.
#create method for debit,creadit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("RS. ", amount, "is debited from your account ",self.account_no)
    def credit(self,amount):
        self.balance+=amount
        print("RS. ", amount, "is credited to your account ",self.account_no)

acc=Account(10000,12345)
print(acc.account_no)
print("The remaining balance",acc.balance)
acc.credit(2000)
print("The remaining balance",acc.balance)
acc.debit(3000)
print("The remaining balance",acc.balance)

#or
class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("RS. ", amount, "is debited from your account ",self.account_no)
        print("total balance = ",self.getbalance())
    def credit(self,amount):
        self.balance+=amount
        print("RS. ", amount, "is credited to your account ",self.account_no)
        print("total balance = ",self.getbalance())
    def getbalance(self):
        return self.balance
acc=Account(10000,12345)
acc.debit(2000)
acc.credit(1300)
acc.credit(5000)
acc.debit(200)

       
        
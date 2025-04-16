num1=int(input("Enter First Numeber: "))
num2=int(input("Enter Second Number: "))
operator=int(input("Enter below no to perform the calculation :\n1-Add\n2-subtract\n3-Multiplication\n4-Division\nEnter between 1 to 4: "))

def add(num1,num2):
    print("addition of two numbers is",num1+num2)

def subtract(num1,num2):
    print("addition of two numbers is",num1-num2)
def multiplication(num1,num2):
    print("addition of two numbers is",num1*num2)
def division(num1,num2):
    print("addition of two numbers is",num1/num2)

if(operator==1):
    add(num1,num2)
elif(operator==2):
    subtract(num1,num2)
elif(operator==3):
    multiplication(num1,num2)
elif(operator==4):
    division(num1,num2)
else:
    print("Enter valid operator")



        

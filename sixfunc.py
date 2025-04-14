def func_sum(a,b):
    sum=a+b
    print(sum)
    return sum
func_sum(18,90)
func_sum(181,2)

#-------------------or
def func_sum1(a,b):
    return a+b

print(func_sum1(9,8))

#---------------------or 

def func_sum2(a,b):
    return a+b

sum=func_sum2(7,7)
print(sum)

#----function with no parameters

def func_hello():
    print("Hello guys I am function")

func_hello()
func_hello()

#create a function to calculate average of 3 numbers
def func_avg(a,b,c):
    return (a+b+c)/3
print(func_avg(2,3,5))
#--------------------------------Practice Questions------------------

#WAF to print the length  of a list (list is the parameter)
nums=[1,2,3,4,5,6,7]
list=[2,3,4,6]
def func_len(nums):
    return len(nums)

print(func_len(list))

#WAF to print the elements of a list in a single line(list is the parameter)
def func_ele(nums):
    for i in nums:
        print(i, end=" ")


func_ele(nums)
print() #this print statement is required else other existing print alse be in same line for above output

#WAF to calculate factorial of n
n=int(input("Enter a number: "))

def func_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
         
func_fact(n)

#------------------------------or---------------
n=int(input("Enter a number: "))

def func_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
         
print(func_fact(n))

#WAF to convert USD to INR
usd=int(input("Enter a $ "))
def func_inr(usd):
    return usd*88 #88 is current indian rupee

print("your",usd,"$",  "in indian rupee = ", func_inr(2))

#WAF to check the number is even or odd using user input
userinput=int(input("Enter a number to check even or odd number: "))
def func_evenorodd(userinput):
    if(userinput%2==0):
        print("Even")
    else:
        print("Odd")
func_evenorodd(userinput)

#------------recursive function(recursion)-----
#WAP to print n to 1
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(6)

#WAF to calculate factorial of number using recursive function and recursive relation
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))


#------or
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(3))

#-------practice questions for recursion in python

#WA recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)

print(sum(5))

#----- or
def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)

print(sum(5))

# Wa recursive function to print all elements in a list(use list and index as parameters)
list=[1,2,3,4,5]
def element(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    element(list,idx+1)
(element(list))



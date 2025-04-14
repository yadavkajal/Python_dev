#while loop
#printing number from 1 to 5
count=1
while count<=5:
    print(count)
    count+=1
print("Loop Ended")

#printing 5 to 1
i=5
while i>=1:
    print(i)
    i-=1
print("loop ended")

#--------------------Assignment with while loop-----------------

#---------------------------------------------
#print numbers from 1 to 100

num=1
while num <=100:
    print(num)
    num+=1
print("1 to 100 numbers are printed")

#----------------------------------------
#print numbers from 100 to 1
rev=100
while rev>=1:
    print(rev)
    rev-=1
print("100 to 1 numbers are printed")

#-------------------------------------------
#print the multiplication table for number n

var=int(input("Enter a number whose table you want to print: "))
num=1
while num<=10:
    print(var*num)
    num+=1
#------------------------------------------
#print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
#this is not requirement this is wrong requirement 1 is given below
list=[]
count=1
while count<=10:
    item=count*count
    count+=1
    list.append(item)
print(list)
i=0
while i <= len(list)-1:
    print(list[i])
    i+=1


#search for a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
num1=int(input("Enter a number to search in tuple: "))
i=0
while i<=len(tup)-1:
    if(num1==tup[i]):
        print("This number exist")
    i+=1
#--------------------------------------------------------------------
#break and continue statement
test=1
while test<=10:
    if (test==3):
        break
    print(test)
    test+=1

test2=1
while test2<=10:
    if (test2==3):
        test2+=1
        
        continue
    print(test2)   
    test2+=1
    
#-----------------------------------------------
#------------------------For loop----------------------------------------
# ----------------------------------------------- 
#print the elements of the following list using a loop
list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)

#-------------------------

#Search a number x in this tuple using for loop
tup1=(1,4,9,16,25,36,49,64,81,100,25)
userint=int(input("Eneter a number for search: "))
idx=0
isFound=False
for se in tup1:
    if(userint==se):
        isFound=True
        print("number is found",userint, "at index",idx)
    idx+=1
if(isFound==False):
    print("number not found")

#-----------------------------------or-------------------
tup1=(1,4,9,16,25,36,49,64,81,100,25)
userint=int(input("Eneter a number for search: "))
if(userint not in tup1):
    print(" not exist")
else:
    print("exist")


#-----------------------------Range()----------------------------------

#print numbers from 1 to 100 (we will provide end of range to 101 as it prints only end-1 values) 
for i in range(1,101):
    print(i)

# print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

#print the multiplication table for number n

no=int(input("enter a number for table: "))
for i in range(1,11):
    print(i*no)


#--------------------------practice Questions--------------------------
#WAP to find the sum of first n numbers
usernum=int(input("Enter a range of number to get sum of those number "))
sum=0
for i in range(1,usernum+1):
    sum=sum+i
print("total sum of number = ",sum)

#-----------------------------OR(using while loop)------------------------------

usernum=int(input("Enter a range of number to get sum of those number "))
sum=0
i=1
while i<=usernum:
    sum=sum+i
    i+=1
print("total sum of number = ",sum)

#WAP to find factorial of first n numbers 

usernum=int(input("Enter a range of number to get factorial of those number "))
fact=1
for i in range(1,usernum+1):
    fact*=i
print("total sum of number = ",fact)



#-------practice questions for recursion in python

#WA recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

print(sum(3))
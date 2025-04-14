#WAP to input user's first name & print it's length

str=str(input("enter your first name "))
print("words in your name ",len(str))


#WAP to find the occurence of "$" in a string

str2=" the company has invested 400$ in a company which has revenue of 300$"
print(str2.count("$"))
#------------------------------------------------------------------------------

#Marks and grading system using conditional statements
marks=int(input("Enter students Marks"))
if(marks>=90):
    print("Congratulations you got A grade with score: ",marks)
elif(marks>=80 and marks<90):
    print("Congratulations you got B grade with score: ",marks)
elif(marks>=70 and marks<80):
    print("Congratulations you got C grade with score: ",marks)
elif(marks<40):
    print("You are unsuccessful in this test with score: ",marks)

else:
    print("Congratulations you got D grade with score: ",marks)
#----------------------------------------------------------------------

#WAP to check if a number entered by the user is odd or even

num=int(input("enter a number "))
if (num%2==0):
    print("This is even number")
else:
    print("This number is odd number")

#WAP to find the greatest of 3 numbers entered by the user
a=int(input("enter first number "))
b=int(input("enter second number "))
c=int(input("enter third number "))
if (a>b & a>c):
    print("this number is greatest ",a)
elif(b>c):
    print("this number is greatest ",b)
else:
    print("This number is greatest ",c)

#WAP to check if a number is a multiple of 7 or not

num=int(input("Enter a number"))
if (num%7==0):
    print("number is multiple of 7")
else:
    print("not multiple of 7")
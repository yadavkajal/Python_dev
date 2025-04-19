f= open ("demo.txt", "r")
data=f.read()
print(data)
print(type(data))
f.close()

#for printing the first line of file
f = open ("demo.txt", "r")
line1=f.readline()
print(line1)
print(type(line1))
f.close()

#for printing 1st and second line

f = open ("demo.txt", "r")
line1=f.readline()
line2=f.readline()
print(line1)
print(line2)
f.close()

#write mode which will overwrite all data and add which we give as input
f = open ("demo.txt", "w")
f.write("I want to replace all text with this one")
f.close()

#Append mode which will add the line at the end which we give as input

f = open ("demo.txt", "a")
f.write("I want to append the second line without overwriting the file")
f.close()

f = open ("demo.txt", "a")
f.write("\nI want to append the third line in next line without overwriting the file")
f.close()

#ToCreate an empty file in python we just need below code
f=open("createdbywritemode.txt","w")
f.close()

#or

f=open("createdbywritemode.txt","a")
f.close()

#r+ mode where a file with data will be override by text from beginning which we provide
f=open("createdbywritemode.txt","r+")
f.write("abcd")
print(f.read())
f.close()

# w+
f=open("createdbywritemode.txt","w+")
f.write("abcd")
print(f.read())
f.close()

#r+
f=open("createdbywritemode.txt","a+")
f.write("abcd")
print(f.read())
f.close()


#with syntax

with open("demo.txt","r") as f:
    print(f.read())

with open("demo.txt","w") as f:
    f.write("This is new data")


#to delete file we need to import os
import os
os.remove("demo.txt")

#Practice Questions

#create a file "practice.txt" using python add the following data in it
#Hi everyone 
#we are learnig file IO.
# using java
# I like programming in java.

with open("practice.txt","w+") as f:
    f.write("Hi everyone \n We are learning file IO\n using java\n I like programming in java")

#------------------------------------------------------------------------------------
#Write a function that replace all occurences of "java" with python in above file.

with open("practice.txt","r") as f:
    read=f.read()
new_data=read.replace("java","python")
print(new_data)
with open("practice.txt","w") as f:
    f.write(new_data)

#or (in function)
def replace():
    with open("practice.txt","r") as f:
        read=f.read()
    new_data=read.replace("java","python")
    print(new_data)
    with open("practice.txt","w") as f:
        f.write(new_data)
replace()
#Search if the word "learning" exist in the file or not

with open("practice.txt","r") as f:
    data=f.read()
count=data.count("learning")
if(count>=1):
    print("Learning exist in this file")
else:
    print("learning does not exist")

#or

with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("found")
    else:
        print("not found")

#WAF to find in which line of the file does the word "learning" occurs first. print -1 if word not found
def readline():
    word="python"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
readline()

#From a file containing numbers separated by comma, print the count of even numbers
count=0
with open("numbers.txt","r") as f:
    data=f.read()
    val= data.split(",")
    for i in val:
        if(int(i)%2==0):
            count+=1
print(count)
    

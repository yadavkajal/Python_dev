#---------------------------------------
#Nested Dictionary
#---------------------------------------
student={
    "name":"kajal",
    "Marks":{
        "Phy":90,
        "maths":80
    }
}
print(student)
print(student["Marks"]["Phy"])

#---------------------------------------
#Dictonary Method
#---------------------------------------
#to get all keys
print(student.keys())
print(list(student.keys())) #typecasting to get keys in list format

#find lenth of key value there are two ways below
print(len(student.keys()))
print(len(list(student.keys())))

#to get all the values
print(student.values())
print(list(student.values()))

#to get all key value-pairs
print(student.items())
print(list(student.items()))

#to get value according to key

print(student.get("name")) #---if we provide non existing key name it will print none as output (this will print none but the program will continue)
print(student["name"]) #this line will print key-error for non existing key.(this will stop running the entire program)

#to update the dictionary
student.update({"age":27})
print(student)
#---other way if we have more data
mydict={"age":67,"city":"mumbai"} #age will be updated in previous age as duplicate keys are not allowed in dictionary
student.update(mydict)
print(student)


#collection

set1={1,2,5,6,7,8,8,9,0,0}
print(set1)
print(type(set1))
print(len(set1))

#Store following word meaning in python dictionary
dict1={
    'table':['A piece of furniture','list of fact & figures'],
    'cat' : 'a small animal'
}
print(dict1)

#you are given a list of subjects.Assume one classroom is required for 1 subject. How many classrooms are needed by students

set2={"python","java","c++","python","javascript","java","python","java","c++","c"}
#as here only 1 class is unique for each subject
print("total classes required for each subject",len(set2))

# WAP to enter three subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one .use subject name as key and marks as 

result={}
subject1=str(input("enter subject1"))
marks1=int(input("enter Marks1 here"))
subject2=str(input("enter subject2"))
marks2=int(input("enter Marks2 here"))
subject3=str(input("enter subject3"))
marks3=int(input("enter Marks3 here"))
result[subject1]=int(marks1)
result[subject2]=int(marks2)
result[subject3]=int(marks3)
print(result)

##2nd way

marks={}
x=int(input("Enter marks for hindi: "))
marks.update({"hindi":x})
x=int(input("Enter marks for english: "))
marks.update({"english":x})
x=int(input("Enter marks for math: "))
marks.update({"math":x})
print(marks)

##3rd way


try:
    no_subject=int(input("Enter how many subjects you want to enter: "))
    dictofsub={}
    for i in range(1,no_subject+1):
        subject=str(input("Enter subject name: "))
        marks=int(input("Enter marks:  "))
        dictofsub[subject]=int(marks)
    print(dictofsub)
except:
    print("please Enter valid number")


#with try catch and print subjects in a format
try:
    no_subject=int(input("Enter how many subjects you want to enter: "))
    dictofsub={}
    for i in range(1,no_subject+1):
        subject=str(input("Enter subject name: "))
        marks=int(input("Enter marks:  "))
        dictofsub[subject]=int(marks)
    print(dictofsub)
    for key in dictofsub:
        print(key,"=", dictofsub[key])
except(ValueError) as e:
    print("please Enter valid number",e)


#figure out a way to store 9 and 9.0 as a seprate value in the set.(take help fo in-built fuction)

values={9,"9.0"} #make anything string
print(values)

#or
values1={("float",9.0),("int",9)}
print(values1)

values2={9,9.2}
print(values2)
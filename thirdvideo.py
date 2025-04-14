list=[1,2,3,4,5,6]
print(list[1:4])
print(list[-6:])
list.append(7)
print(list)

list1=["a","m","j","h","t","u"]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1) 
list1.reverse()
print(list1)
list1.insert(4,"k")
print(list1)
list1.remove('h')
print(list1)
list1.pop(2)
print(list1)

tup=(2,4,6,8,9,0,8,8)
print(tup)
print(type(tup))
print(tup[0:3])
print(tup.index(6))
print(tup.count(8))

#practice Questions-----------------

#WAP to ask the user to enter names of their three favourite movies and store them in a list
list=[]
p1=str(input("enter first movie name: "))
p2=str(input("enter second movie name: "))
p3=str(input("enter third movie name: "))
list.append(p1)
list.append(p2)
list.append(p3)
print(list)

#or

list1=[]
list1.append(input("enter first movie name: "))
list1.append(input("enter first movie name: "))
list1.append(input("enter first movie name: "))
print(list1)

#or

list2=[]
p1=str(input("enter first movie name: "))
list2.append(p1)
p1=str(input("enter second movie name: "))
list2.append(p1)
p1=str(input("enter third movie name: "))
list2.append(p1)
print(list2)


#WAP to check if a list contains a palindroms of elements
list3=[1,2,3,2,1]
list4=list3.copy()
list4.reverse()

if(list3 == list4):
    print("it is palindrom")
else:
    print("it is not palindrom")

#WAP to count the number of students with "A" grade in the following tuple.("c","D","a","a","b","a")

tup=("C","D","A","A","B","B","A")
print("Number of student with A grade",tup.count("A"))


#Store the above values in a list and sort them from A to D
Grade=["C","D","A","A","B","B","A"]
Grade.sort()
print("Grades from A to D",Grade)

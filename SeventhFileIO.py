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


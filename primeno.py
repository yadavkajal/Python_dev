num=int(input("Enter no between 1 to 100: "))
counter=0
for i in range(1,100):
    if(num%i==0):
        counter+=1
    #print(counter)
if(counter==2):
    print("The number is a prime number")
else:
    print("The number is not a prime number")
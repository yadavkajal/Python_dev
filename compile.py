count=0
with open("numbers.txt","r") as f:
    data=f.read()
    val= data.split(",")
    for i in val:
        if(int(i)%2==0):
            count+=1
print(count)
    
    

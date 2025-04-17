def occur():
    with open("practice.txt","r") as f:
        for i in f:
            data=f.readline()
            if(data.find("learning")!=-1):
                print("found")
            else:
                print("-1 not found")
occur()
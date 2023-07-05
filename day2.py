def getAge(age):
    cat="baby"
    if(age<=5):
        cat="baby"
    elif(age>5 and age<=13):
        cat="kids"
    else:
        cat="big people"
    return cat
#myage=input("enter your age as a interger (ex.18): ")
#mycat=getAge(int(myage))
#print(mycat)

friends=["aaa","bbb","ccc"]
friends.append("ddd")
friends.remove("ccc")
friends.sort()

for f in friends: #sequential search algorithm
    if (f=="bbb"):
     print(f+" is cool")
    else:
        print(f+" is ok")

for i in range(3):
    print(friends[i])

keepgoing=True
while (keepgoing==True):
    key=input("press q to quit: ")
    if(key=="q"):
        keepgoing=False
        print("bye")

        

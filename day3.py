def exData(blist,num):
    for r in range(1,num):
        line=blist[r]
        temp=line.split(",")
        print(temp[3]+" survived? "+temp[1]+" m/f "+temp[5])




#file input
fi=open("titanic.csv","r")#read-only,write
biglist=fi.readlines()
fi.close()

print(len(biglist))
print(biglist[0])
exData(biglist,10)

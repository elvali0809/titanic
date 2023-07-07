def kidz(data):
    numkidz=0
    kidzlive=0
    for r in data:
        temp=r.split(",")
        if(float(temp[6])<16.0):
            numkidz=numkidz+1
            if(temp[1]=="1"):
             kidzlive=kidzlive+1
            return round(kidzlive/numkidz*100,1)
        file=open("titanic.csv","r")
        cols=file.readline()
        data=file.readlines()
        file.close()
        print(cols)
        print(data[0])
        print(str(kidz(data))+"%survived")

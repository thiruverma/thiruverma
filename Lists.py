myUniqueList=[]
LeftOvers=[]
print(myUniqueList)
def Add(num):
    if num in myUniqueList:
        LeftOvers.append(num)
        return False
    else:
        myUniqueList.append(num)
        return True
                
intfe = Add(1)
sd= Add(2)
cd= Add(2)
df= Add(5)
print(myUniqueList)
print(LeftOvers)




    






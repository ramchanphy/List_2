list=[1,1,2,3,4,5,2,3]
i=0
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i+=1
print(a)
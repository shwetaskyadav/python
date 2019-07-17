list1=[9,10,16,1,4,96]
a=len(list1)
t=0
for i in range(a):
    for j in range(a-1):
        if list1[j]>list1[j+1]:
            t=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=t
            print(list1)
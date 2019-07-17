x=int(input("enter number of element in list"))
lst1=[]
for i in range(x):
    lst1.append(int(input()))
min=lst1[0]
for i in range(x):
    if(lst1[i]<min):
        min=lst1[i]
print(min)

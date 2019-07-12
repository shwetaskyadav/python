#n=int(input())
words=['abc','bcd','efg','abc','k','n','k']
rep={}
#for i in range(0,n):
#    words.append(input())
for i in words:
    if i not in rep.keys():
        rep[i]=1
    else:
        rep[i]+=1
print(len(rep))
list2=[]
for i in rep.values():
    list2.append(i)
print(list2)
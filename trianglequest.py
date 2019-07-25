def trianglequest(n):
    num=0
    for i in range(0,n):
        for j in range(0,i):
            print(num,end="")
            
        print('\r')
        num=num+1
        
trianglequest(5)
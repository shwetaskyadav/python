def fibo(n):
    a=0
    print(a)
    b=1
    print(b)
    for i in range(n-2):
        c=a+b
        print(c)
        a=b
        b=c

fibo(5)
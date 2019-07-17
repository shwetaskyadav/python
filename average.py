def fun(*args):
    sum=0
    avg=0
    for i in args:
        sum+=i
    avg=sum/len(args)
    print(avg)

fun(10,20,30,40,50)
def leap(y):
    if (y%4==0 and y%100==0 and y%400==0):
        print("leap year")
    else:
        print("no")


y=int(input())
leap(y)

        




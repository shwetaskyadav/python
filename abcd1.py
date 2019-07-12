import re
credit=input("Enter your credit card number")
match=re.search(r'[4-6]{1}[0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',credit)
if(match):
    if(credit[4]=='-'):
        credit=credit.replace('-','')
    l=len(credit)
    for i in range(0,l-3,1):
        flag=0
        for j in range(i+1,i+3,1):
            if credit[i]==credit[j]:
                flag+=1
        if flag>=4:
           print("Invalid")
           exit()
    print("valid")    
else:
    print("Invalid")

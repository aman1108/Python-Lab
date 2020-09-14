amount=0
while (True):
    a=input("").split()
    if (len(l)==0):
            break
    else:
        if (a[0]=='D'):
            amount=amount+int(a[1])
        elif (a[0]=='W'):
            if((amount-a[1])<0):
                print("Not enough amount")
            else:
                amount=amount-int(a[1])
print(amount)

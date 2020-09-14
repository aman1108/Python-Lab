mystr=input("Enter String: ")
dcount=0
acount=0
for a in mystr:
    if (a.isdigit()):
        dcount=dcount+1
    elif(a.isalpha()):
        acount=acount+1
print("Number of Digit :",dcount)
print("number of Alpha :",acount)

temp=input("Enter Temperature in C or F: ")
a=len(temp)
if (temp[a-1]=='F'):
    print("Value in C: ",(5/9)*(float(temp[0:a-1])-32))
elif (temp[a-1]=='C'):
    print("Value in F: ",((9/5)*(float(temp[0:a-1]))+32))

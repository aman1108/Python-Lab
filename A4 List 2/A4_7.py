mylist=input("Enter your list: ").split()
mylist1=[]
for i in mylist:
    if(i not in mylist1):
        mylist1.append(i)
print(mylist1)

mylist=input("Enter your list: ").split()
myset=set(mylist)
mylist=list(myset)
mylist.sort()
print(mylist[len(mylist)-2])
mylist=input("Enter your Elements").split()
a,b =input("Enter range").split()
mylist.sort()
print([i for i in mylist if (i>a and i<b)])

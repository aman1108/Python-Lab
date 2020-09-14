mylist=[int(i) for i in input("Enter List Elements").split(" ")] 
a=int(input("Enter specified Number"))
print([i for i in mylist if i>a])

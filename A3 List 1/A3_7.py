l=[1,2,3,4]
mystr="emp"
print(l)
for i in range(len(l)):
    l[i]=mystr+str(l[i])
print(l)

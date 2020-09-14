n=input("Enter your Number").split()
fact=1
l=[ ]
for  i in n:
    fact=1;
    for j in range(1,int(i)+1):
        fact=fact*j
    l.append(fact)
print(l)

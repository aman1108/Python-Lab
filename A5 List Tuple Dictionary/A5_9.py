a=input("").split()
b=set(a)
c=list(b)
c.sort()
for i in c:
    print(i+":", a.count(i))

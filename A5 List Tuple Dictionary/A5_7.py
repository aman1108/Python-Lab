a=[ ]
while True:
    l=tuple(input("").split())
    if (len(l)==0):
        break;
    a.append(l)
a.sort()
print(a)


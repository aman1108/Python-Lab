a=0
b=1
print(a)
print(b)
for i in range(1,250):
    c=a+b
    print(c%10,end='\t')
    a=b
    b=c

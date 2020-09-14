def gen(n):
    for i in range(n):
        if(i%7==0):
            yield i
for i in gen(25):
    print(i)

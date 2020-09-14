def gen(s):
    for i in range(len(s)-1,-1,-1):
        yield s[i]

for i in gen("abcd"):
    print(i)

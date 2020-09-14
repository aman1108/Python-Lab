def fun():
    a=5
    b=a
    c=8
    print("a,b,c are local variable")

print(fun.__code__.co_nlocals)

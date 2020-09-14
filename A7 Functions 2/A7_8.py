def incr(x):
    return x+1
def decr(x):
    return x-1
def operate(fun,x):
    result=fun(x)
    return result
print(operate(incr,3))
print(operate(decr,2))

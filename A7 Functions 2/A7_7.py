def sumfun(*args):
    sumval=0
    for i in args:
        sumval=sumval+int(i)
    return sumval

print(sumfun(6,8,9,8,5,4))
print(sumfun(5,6,'7'))

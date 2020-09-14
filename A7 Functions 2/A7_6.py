def num(a):
    def incr(val):
        val=val+1
        return(val)
    def decr(val):
        val=val-1
        return(val)
    print("Value increment wil be: ",incr(a))
    print("Value decrement wil be: ",decr(a))

num(5)
    

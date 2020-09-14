i=int(input("Enter input: "))
mystr=" "
print("*"*i)
for j in range (i-1):
    mystr=" "*(i-j-1)+"*"
    print(mystr)
print("*"*i)
    
    

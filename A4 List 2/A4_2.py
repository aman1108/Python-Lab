mystr=input("Enter your String").split()
n=int(input("Enter Number:"))
print([i for i in mystr if len(i)>n])

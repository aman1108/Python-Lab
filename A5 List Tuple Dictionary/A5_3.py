D=input("Enter values of D in comma seprated: ").split(",")
C=50
H=30
Q=[int(((2*C*int(i))/H)**(1/2))  for i in D]
print(Q)

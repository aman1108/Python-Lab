a=input("Enter 4-digit binary number: ").split(",")
b=['0000','0101','1010','1111']
print([i for i in a if(i in b)])

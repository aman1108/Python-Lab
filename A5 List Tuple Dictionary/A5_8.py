a=[0,0,0,0]
while(True):
    up=input("").split()
    if (up[0]=="UP"):
        a[0]=a[0]+int(up[1])
    elif(up[0]=="DOWN"):
        a[1]=a[1]+int(up[1])
    elif(up[0]=="LEFT "):
        a[2]=a[2]+int(up[1])
    elif(up[0]=="RIGHT "):
        a[3]=a[3]+int(up[1])
    elif(len(up)==0):
        break
print(a)
print(int((((a[0]-a[1])**2)+(a[2]-a[3])**2)**(1/2)))

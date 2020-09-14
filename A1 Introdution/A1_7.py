str=input("Enter a string")
a=len(str)
if(a>2):
    if(str[a-3:]=="ing"):
        str1=str+"ly"
        print(str1)
    else:
        str1=str+"ing"
        print(str1)
else:
    print(str)

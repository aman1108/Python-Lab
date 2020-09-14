def checkpass(a):
    spchar="$@#"
    lower = 0
    upper = 0
    digits = 0
    special = 0
    for char in a:
        if (char.islower()):
            lower += 1
        elif (char.isupper()):
            upper += 1
        elif (char.isdigit()):
            digits += 1
        elif (spchar.find(char) != -1):
            special += 1
    if (lower >= 1 and upper >= 1 and digits >= 1 and special >= 1 and len(a) in range(6,13)):
        print(a, end=",")

A=["ABd1234@1","a","F1#","2w3E*","2We3345"]
for i in A:
    checkpass(i)

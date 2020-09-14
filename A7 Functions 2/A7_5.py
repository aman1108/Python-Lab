def palin(s):
    b=s[::-1]
    if(b==s):
        print("Palindrome")
    else:
        print("Not Palindrome")

palin("abcd")
palin("abba")

s = input("enter car registration plate: ")

if len(s) == 7:
    if s[0].isdigit() and s[1].isdigit() and s[2].isdigit() and s[3].isdigit():
        if s[4].isupper() and s[5].isupper() and s[6].isupper():
            print("Valid new registration plate")
    else:
        print("Not valid plate")
elif len(s) == 6:
    if s[0].isupper() and s[1].isupper() and s[2].isupper():
        if s[3].isdigit() and s[4].isdigit() and s[5].isdigit():
            print("Old registration plate")
    else:
        print("Not valid plate")
else:
   print("Not valid plate")
        
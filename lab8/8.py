s = """3
word
localization
internationalization"""

a = s.split("\n")

def abbreviate(s: str):
    if len(s) <= 10:
        return s
    else:
        abbreviation = s[0] + str(len(s)-2) + s[-1]
        return abbreviation

for i in range(1,len(a)):
    print(abbreviate(a[i]))
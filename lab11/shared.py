def modifyString(s: str):
    s = s.upper()
    for char in "AEILNORSTU":
        s = s.replace(char, "1")

    for char in "DG":
        s = s.replace(char, "2")

    for char in "BCMP":
        s = s.replace(char, "3")

    for char in "FHVWY":
        s = s.replace(char, "4")

    s = s.replace("K", "5")

    for char in "JX":
        s = s.replace(char, "8")

    for char in "QZ":
        s = s.replace(char, "9")

    return s

points = {"1":1, "2":2, "3":3, "4":4, "5":5, "8":8, "9":10 }

def countPoints(s: str):
    count = 0
    for char in s:
        count += points[char]

    return count
s = """5
Jack captain
Alice woman
Charlie man
Bob child
Julia woman"""

lines = s.split("\n")[1:]
womenAndChildren = []
men = []
captain = ""


for line in lines:
    name, category = line.split()
    if category == "woman" or category == "child":
        womenAndChildren.append(name)
    elif category == "man":
        men.append(name)
    else:
        captain = name

for name in womenAndChildren:
    print(name)

for name in men:
    print(name)
    
print(captain)
    

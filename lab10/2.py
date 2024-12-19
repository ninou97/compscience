
with open("file5.txt", "r") as file:
    file5 = file.read()

with open("file6.txt", "r") as file:
    file6 = file.read()

if "Academy" in file5:
    print("Academy is in file5")

if "Academy" in file6:
    print("Academy is in file6")


# print(file5)
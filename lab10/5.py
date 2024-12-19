
with open("fileFor5.txt", "r") as file:
    lines = [line.strip() for line in file]

inp = input("Type a line: ")

lines.insert(len(lines)//2, inp)

# print(lines)

with open("fileFor5.txt", "w") as file:
    for word in lines:
        file.write(word + "\n")

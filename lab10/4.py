
n = int(input())
sex = input()

if sex == "м":
    with open("file8.txt", "r") as file:
        lines = file.readlines()
    
    for i in range(n):
        print(lines[i].split()[0])
elif sex == "ж":
    with open("file8.txt", "r") as file:
        lines = file.readlines()
    
    for i in range(n):
        print(lines[i].split()[0])



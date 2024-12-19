
with open("file4.txt", "r") as file:
    lines = [line.strip().split() for line in file]

max = -1
max_index = -1

# print(lines)
# print(lines[-1])

for i, line in enumerate(lines):
    if max < int(line[2]):
        max_index = i
        max = int(line[2])

print(f"{lines[max_index][0]} {lines[max_index][1]} (Набранное количество баллов: {lines[max_index][2]})")
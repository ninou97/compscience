
# shacnidw
cypher = input()

if cypher[-1] != "#":
    print("Ошибка! Отсутствует символ #")
else:
    cypher = cypher[:-1]
    a1 = []
    a2 = []

    for i in range(len(cypher)):
        if i % 2 == 0:
            a1.append(cypher[i])

    for i in range(len(cypher)-1, 0,-1):
        if i % 2 != 0:
            a2.append(cypher[i])

    a1.extend(a2)

    print("".join(a1))
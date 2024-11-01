
people = []

while 1:
    height = int(input())
    if height == 0:
        break
    if height > 0:
        people.append(height)

if len(people) > 1:
    print("Самый высокий человек с ростом: ", max(people))
    print("Самый низкий человек с ростом: ", min(people))
else:
    print("Некого сравнивать")




data = [1,"a",3,4,"b",6]

letters = []
numbers = []

for x in data:
    if isinstance(x, (int, float)):
        numbers.append(x)
    else:
        letters.append(x)

data.clear()

print(numbers)
print(letters)
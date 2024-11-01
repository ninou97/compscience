
inputs = []

while True:
    user_input = input()

    if user_input == "":
        break

    inputs.append(int(user_input))

mean = sum(inputs) / len(inputs)
print("arithmetic mean: ", mean)
print("numbers less than the mean: ", end="")
for x in inputs:
    if x < mean:
        print(x, end=" ")

print()

print("numbers greater than the mean: ", end="")
for x in inputs:
    if x > mean:
        print(x, end=" ")
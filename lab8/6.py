import random

count_o = 0
count_p = 0
tries = 0

while True:
    coin = random.choice(["O", "P"])
    print(coin, end=" ")

    if coin == "O":
        count_o += 1
        count_p = 0
    else:
        count_o = 0
        count_p += 1

    tries += 1

    if count_o == 3:
        print("(попыток: ", tries, ")")
        break

    if count_p == 3:
        print("(попыток: ", tries, ")")
        break
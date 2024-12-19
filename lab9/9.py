import random

field = [[0]*4 for _ in range(4)]

cnt = 0

while True:
    x = random.randint(0,3)
    y = random.randint(0,3)

    if field[y][x] == 0:
        field[y][x] = 1
        cnt += 1
        if cnt == 4:
            break

while True:
    x = random.randint(0,3)
    y = random.randint(0,3)

    if field[y][x] == 0:
        field[y][x] = "B"
        break


print(field)

win_cond = 0

while True:
    for y in range(len(field)):
        for x in range(len(field)):
            if field[y][x] == "X":
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

    
    y, x = map(int, input("Type Y X: ").split())
    y -= 1
    x -= 1    
    if field[y][x] == "B":
        print("You've lost")
        break
    elif field[y][x] == 1:
        field[y][x] = "X"
        win_cond += 1
        if win_cond == 4:
            print("You've won")
            break


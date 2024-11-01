
import random

secret = random.randint(1, 10)

print("Хорошо, я загадал число. Попробуй его отгадать")

counter = 1
while 1:
    num = int(input(f"{counter}> "))

    if num == secret:
        print("Поздравляю! Вы угадали!")
        play_again = bool(input("play again? (empty space to exit)"))
        if play_again:
            secret = random.randint(1,10)
            counter = 1
            continue
        else:
            break
    elif num < secret:
        print("Больше")
    elif num > secret:
        print("Меньше")
    
    counter += 1

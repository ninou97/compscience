import random

with open("fileFor7.txt", "r") as file:
    words = file.read().split()

while True:
    first = words[random.randint(0,len(words)-1)]
    second = words[random.randint(0,len(words)-1)]

    while len(first) < 3:
        first = words[random.randint(0,len(words)-1)]
    while second == first or len(second) < 3:
        second = words[random.randint(0,len(words)-1)]

    password = first[0].upper() + first[1:] + second[0].upper() + second[1:]
    if 8 <= len(password) <= 10:
        print(password) 
        break

        

        

        

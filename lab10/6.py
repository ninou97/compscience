
choice = input("Decypher or cypher, type d or c: ")

if choice == "d":
    with open("fileFor6.txt", "r") as file:
        words = file.read().split()

    for word in words:
        for i in range(len(word)-1,-1, -1):
            print(word[i], end="")
        print(" ", end="")

elif choice == "c":
    inp = input("Type text to cypher: ")
    words = inp.split()

    with open("cypheredTextFrom6.txt", "w") as file:
        for word in words:
            rev_word = word[::-1]
            file.write(rev_word + " ")


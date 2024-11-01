
phrase = input()

words = phrase.strip().split()

if len(words) != 2:
    print("Ошибка! Некорректное количество слов")
else:
    print(words[1], words[0])


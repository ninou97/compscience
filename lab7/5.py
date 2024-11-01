
sentence = """Вечер за окном.
Еще один день .
Жизнь скоротечна..."""


print(sentence)
lines = sentence.splitlines()

def count_vowels(s):
    vowels = "аеиоуыэюёя"
    s = s.lower()
    sum = 0
    for char in s:
        if char in vowels:
            sum += 1
    return sum

if len(lines) != 3:
    print("Не хайку. Должно быть 3 строки.")
else:
    if count_vowels(lines[0]) == 5 and count_vowels(lines[1]) == 7 and count_vowels(lines[2]) == 5:
        print("Хайку")
    else:
        print("Не хайку")
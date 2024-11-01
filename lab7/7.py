import random


pass_len = int(input("Желаемая длина пароля (целое число) "))
pass_cap_letters = input("Нужны ли заглавные буквы (да/нет) ")
pass_lowercase_letters = input("Нужны ли строчные буквы (да/нет) ")
pass_digits = input("нужны ли цифры (да/нет) ")
pass_special_symbols = input("нужны ли специальные символы (да/нет) ")

cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special_symbols = "@#&*!?%^$"

a = []

if pass_cap_letters == "да":
    a.append(cap_letters)

if pass_lowercase_letters == "да":
    a.append(lowercase_letters)

if pass_digits == "да":
    a.append(digits)

if pass_special_symbols == "да":
    a.append(special_symbols)

password = ""

if len(a) > 0:
    for i in range(pass_len):
        r = random.choice(a)
        char = random.choice(r)
        password += char

    print(password)



sentence = """Довольно распространённая ошибка ошибка
ошибка это лишний повтор повтор
слова слова Смешно не не правда ли
Не нужно портить хор хоровод хоровод"""

sent = sentence.split()
newword = []

for i in range(len(sent)-1):
    if sent[i] == sent[i+1]:
        continue
    newword.append(sent[i])

newword.append(sent[-1])

for word in newword:
    print(word, end=" ")

with open("file6.txt", "r") as file:
    text = file.read()

words = text.split()

count = 0

for word in words:
    if 'e' in word:
        count += 1
    else:
        continue

percentage = (count/len(words))*100

print(f"{percentage:.2f}...")
    
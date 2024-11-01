
bin = input()
num = 0

for i in range(len(bin)):
    # print(i, bin[i], (len(bin)-i))
    num += int(bin[i])*2**(len(bin)-1-i)

print(num)

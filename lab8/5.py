
a = [215,207,196,176,168,166]
a2 = [215,210,207]

x = int(input())

for i in range(len(a)):
    if x >= a[i] or i == len(a):
        print(i+2)
        break

for i in range(len(a2)):
    if x >= a2[i] or i == len(a2)-1:
        print(i+2)
        break


a = [1,5,2,4,3]

for i in range(1,len(a)):
    if a[i] > a[i-1]:
        print(a[i], end=" ")
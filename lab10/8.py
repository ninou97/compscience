
n, m = map(int, input().split())

if 3 <= n <= 50 and 3 <= m <= 50:
    for i in range(n):
        if i % 2 == 0:
            print("#"*m)
        else:
            if i % 4 == 1:
                print("."*(m-1) + "#")
            else:
                print("#" + "."*(m-1))



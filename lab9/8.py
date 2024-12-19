
n, m = map(int, input("n m: ").split())

matrix = []

for i in range(n):
    matrix.append([0]*m)

for j in range(m):
    matrix[0][j] = 1

for i in range(n):
    matrix[i][0] = 1

    for i in range(1,n):
        for j in range(1,m):
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

for row in matrix:
    print(" ".join(f"{y:6d}" for y in row))


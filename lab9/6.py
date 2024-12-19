
def create_matrix():
    n = int(input("Square matrix dimensions: "))

    matrix = []

    for i in range(n):
        row = list(map(int, input(f"Enter {n} elements: ", ).split()))

        if len(row) != n:
            print(f"Need {n} elements in a row")
            return []

        matrix.append(row)

    matrix[0][0], matrix[-1][0] = matrix[-1][0], matrix[0][0]
    matrix[0][-1], matrix[-1][-1] = matrix[-1][-1], matrix[0][-1]

    return matrix


matrix = create_matrix()

for row in matrix:
    print(" ".join(list(map(str, row))))




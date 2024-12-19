
def create_matrix():
    rows, cols = map(int, input("Rows and columns (space separated): ").split())

    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: enter {cols} elements (space separated): ").split()))
        
        if len(row) != cols:
            print(f"Need {cols} elements in a row")
            return []
        
        matrix.append(row)
    
    return matrix

matrix = create_matrix()
# matrix = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

def transpose_matrix(matrix):
    # "*" unpacks the matrix - passes each element (row) of the array (matrix) as a separate argument into zip function
    # zip function returns tuple of elements from input lists that correspond to the same index
    return [list(row) for row in zip(*matrix)]

transp = transpose_matrix(matrix)

print()

print("Original matrix: ")
for row in matrix:
    print(" ".join(list(map(str, row))))

print("\nTrasnposed: ")
for row in transp:
    print(" ".join(list(map(str, row))))

import random

def main():
    n, m, k = map(int, input("n m k: ").split())

    if k <= m:
        matrix = []

        for i in range(n):
            row = [random.randint(0,1) for _ in range(m)]
            matrix.append(row)


        print(matrix)

        for i in range(len(matrix)):
            arr = matrix[i]
            cnt = 0
            
            for j in range(len(arr)):
                if arr[j] == 0:
                    cnt += 1
                    if cnt == k:
                        print(i+1)
                        return
                else:
                    cnt = 0
        else:
            print(0)

main()





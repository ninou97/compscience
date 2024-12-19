import random

n = 3
m_square = [0] * n
for i in range(n):
    m_square[i] = [0] * n

m_square[1][1] = 5
first_corner = 0
second_corner = 0
used_numbers = set()

# Corners
while True:
    n = random.randint(1,9)
    if n % 2 == 0:
        first_corner = n
        used_numbers.add(n)
        break

m_square[0][0] = first_corner
fourth_corner = 10 - first_corner
used_numbers.add(fourth_corner)
m_square[2][2] = fourth_corner

while True:
    n = random.randint(1,9)
    if n % 2 == 0 and n not in used_numbers:
        second_corner = n
        break

m_square[0][2] = second_corner
third_corner = 10 - second_corner
m_square[2][0] = third_corner

# intermediate_numbers

m_square[0][1] = 15 - (first_corner + second_corner)
m_square[1][0] = 15 - (first_corner + third_corner)
m_square[1][2] = 15 - (second_corner + fourth_corner)
m_square[2][1] = 15 - (third_corner + fourth_corner)

for i in range(3):
    for j in range(3):
        print(f"{m_square[i][j]}", end=" ")
    print()








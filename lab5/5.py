first_side = input("First side: ")
second_side = input("Second side: ")
third_side = input("Third side: ")

if (first_side == second_side and first_side == third_side):
    print("Равносторонний треугольник")
elif (first_side == second_side or first_side == third_side or second_side == third_side):
    print("равнобедренный")
else:
    print("Разностороннего")


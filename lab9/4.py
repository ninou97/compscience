
menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

def main():

    choice = int(input("""Choose the option number:\n
    1. Отобразить меню ресторана
    2. Найти блюдо по названию и отобразить его ингредиенты и цену.
    3. Добавить новое блюдо в меню.
    4. Изменить цену блюда.
    5. Выйти\n"""))

    print()

    if choice == 1:
        for a in menu:
            print(a[0])
    if choice == 2:
        dish = input("Введите название блюда: ")
        for a in menu:
            if a[0] == dish:
                print("Ingredients: ", ", ".join(a[1]), "; Price: ", a[2])
                
                # print(a[1], a[2])
                break
        else:
            print("Такого блюда нет")
    if choice == 3:
        dish = []

        name = input("Имя блюда: ")
        if name == "":
            print("Не введено имя")
            return

        dish.append(name)

        ingredients = input("Введите ингридиенты через пробел: ").split()
        if len(ingredients) == 0:
            print("Не введены ингридиенты: ")
            return
        
        dish.append(ingredients)

        price = int(input("Введите цену: "))
        dish.append(price)

        menu.append(dish)
    if choice == 4:
        dish = input("Блюдо: ")
        for i in range(len(menu)):
            if menu[i][0] == dish:
                newPrice = int(input("Новая цена: "))
                menu[i][2] = newPrice
                break
        else:
            print("Такого блюда нет")
    if choice == 5:
        return 1
    
    print()

while True:
    choice = main()
    if choice == 1:
        break
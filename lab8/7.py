
def check_number(number: str):
    digits = [int(x) for x in number]

    sum = 0

    for i in range(len(digits)):
        if i % 2 != 0:
            sum += digits[i]
        
    for i in range(len(digits)):
        if i % 2 == 0:
            product = digits[i]*2
            if product > 9:
                product -= 9
            sum += product

    if sum % 10 == 0:
        print("Корректный номер")
    else:
        print("Некорректный номер")

check_number("4276440013361511")
check_number("4276440013361512")
check_number("42761336512")

ticket = input()
if len(ticket) != 6:
    print("Некорректный билет")
else:
    ticket_n = []
    for x in ticket:
        ticket_n.append(int(x))
    sum1 = (ticket_n[0] + ticket_n[1] + ticket_n[2])
    sum2 = (ticket_n[3] + ticket_n[4] + ticket_n[5])
    if sum1 == sum2:
        print("Поздравляю! Ваш билет - счастливый")
    else:
        print("Обычный билет")
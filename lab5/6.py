month = int(input("Месяц: "))

if month == 2:
    print("Either 28 or 29 days")
else:
    if month % 2 == 1:
        print("31 days")
    else:
        print("30 days")



test = "Еда не плоха, но могла бы быть лучше"
test2 = "Фильм не плохой"
test3 = "Книга плохая!"

test = test.replace("не плохой", "хороший")
test = test.replace("не плоха", "хороша")
test = test.replace("не плохо", "хорошо")

test2 = test2.replace("не плохой", "хороший")
test2 = test2.replace("не плоха", "хороша")
test2 = test2.replace("не плохо", "хорошо")


print(test)
print(test2)
print(test3)
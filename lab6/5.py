
age = int(input())
age_2 = 0

if age > 1:
    age_2 = 10.5*2 
    b = age-2
    age_2 += 4*b
elif age == 1:
    age_2 = 10.5
else:
    print("Ошибка")
    

print(age_2)

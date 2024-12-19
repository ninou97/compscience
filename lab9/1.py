
ns = [10,100,1000]

def func(x):
    return x**2 / (10 + x**3)

for n in ns:
    a = -2
    b = 5
    # n = 100000
    h = (b - a) / n

    # Initial sum with first and last terms (for trapezoidal rule)
    sum = (func(a) + func(b)) / 2

    # Add the middle terms
    i = a + h
    while i < b:
        sum += func(i)
        i += h

    # Multiply by step size h to get the final area approximation
    sum *= h

    print(f"{sum:.2f}")
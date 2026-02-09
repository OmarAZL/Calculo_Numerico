import math

def func(x):
    return x**2 * math.sin(3 * x**3 + 1)

def func2(x):
    return 3 * x * math.sqrt(x**2+1)

def Riemann(func, a, b, n):
    h = (b - a) / n
    x = a
    area = 0
    for i in range(n):
        area = area + (h * func(x))
        x = x + h
    return area

print(Riemann(func2, 0, 1, 1000))
import math

def derivada(f, x, h=1e-6):
    return (f(x+h) - f(x-h)) / (2*h)

def segunda_derivada(f, x, h=1e-6):
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)

def newton_rapson(func, a, b, error, maxI = 5):
    x0 = (a+b)/2
    condicion = abs( (func(x0) * segunda_derivada(func, x0)) / math.pow(derivada(func, x0), 2) ) < 1
    
    ints = 0
    xi = x0
    while maxI > ints:
        diff = derivada(func, xi)
        xis = xi - func(xi) / diff
        errorActual = abs((xis - xi) / xis)
        print(f"[{ints}] {xi} {xis} {errorActual}")
        if( errorActual <= error):
            return xis, errorActual, ints 
        xi = xis
        ints += 1
    return "No converge"

def func(x):
   return ( (x * math.log(x)) - 2 )

def fun(x):
    return math.sin(x) - math.pow(math.e, -x)

newton_rapson(func, 0, 1, 0.03, 10)
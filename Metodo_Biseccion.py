import math

def func(x):
   return ( (x * math.log(x)) - 2 )

def biseccion(func, a, b, error, maxI = 30):
    if( func(a) * func(b) >= 0 ):
        return "No converge"
   
    i = 0
    m = 0
    errorRelativo = 100
    lm = []
    while i < maxI and errorRelativo > error:
        m = (a + b) / 2
        lm.append(m)
        print(f"[{i}] {a}, {m}, {b}", end=" ")
        if(i > 0):
            errorRelativo = abs((lm[i] - lm[i-1]) / lm[i])
            print(f"Error: {round(errorRelativo, 4)}")
        else:
            print("nil")
        
        if(func(a) * func(m) < 0):
            b = m
        elif(func(b) * func(m) < 0):
            a = m
        i += 1
        if(errorRelativo < error):
            return m, errorRelativo, i

m, error, i = biseccion(func, 2, 3, 0.03)
print(f"\nIntentos: {i}, m = {m}, Error = {error}, f({round(m,4)} = {func(m)})\n")

def sn(x):
    return math.sin(x) - math.pow(math.e, -x)

m, error, i = biseccion(sn, 0, 1, 0.04)
print(f"\nIntentos: {i}, m = {m}, Error = {error}, f({round(m,4)}) = {round(sn(m),4)}\n")
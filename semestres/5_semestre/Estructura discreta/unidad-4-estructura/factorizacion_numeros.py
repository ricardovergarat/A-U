from primos import *
def factorizacion_numero(n):
    primos = generar_primos(1,int(n / 2))
    factorizacion = []
    while n != 1:
        for i in range(len(primos)):
            if n % primos[i] == 0:
                factorizacion.append(primos[i])
                n = n / primos[i]
    factorizacion.sort()
    return factorizacion
import math

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

def poisson(lam,x):
    numerador = (lam ** x) * math.exp(- lam)
    denominador = factorial(x)
    return numerador / denominador

def obtener_esperanza_poisson(lam,x):
    return lam

def obtener_varianza_poisson(lam,x):
    return lam

def obtener_desviacion_poisson(lam,x):
    varianza = obtener_desviacion_poisson(lam,x)
    resultado = math.sqrt(varianza)
    return resultado
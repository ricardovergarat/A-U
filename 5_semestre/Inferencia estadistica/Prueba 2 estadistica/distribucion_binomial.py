import math

def distribucion_binomial(n,x):
    parte_1 = p ** x
    parte_2 = (1 - p) ** (n - x)
    resultado = parte_1 * parte_2
    return resultado

def obtener_esperanza_binomial(n,p):
    return n * p

def obtener_varianza_binomial(n,p):
    esperanza = obtener_esperanza_binomial(n,p)
    return esperanza * (1 - p)

def obtener_desviacion_binomial(n,p):
    varianza = obtener_varianza_binomial(n,p)
    resultado = math.sqrt(varianza)
    return resultado

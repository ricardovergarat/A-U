import math

def obtener_esperanza_bernoulli(p):
    return p

def obtener_varianza_bernolli(p):
    restante = 1 - p
    varianza = p * restante
    return varianza

def obtener_desviacion_bernolli(p):
    varianza = obtener_varianza_bernolli(p)
    desviacion = math.sqrt(varianza)
    return desviacion

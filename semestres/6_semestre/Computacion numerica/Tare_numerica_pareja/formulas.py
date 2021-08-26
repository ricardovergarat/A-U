import numpy as np

# ambos parametros son float de 64 bits
def obtener_error_absoluto(valor_real,valor_representativo):
    resultado = valor_real - valor_representativo
    resultado = abs(resultado)
    return resultado

# ambos parametros son float de 64 bits
def obtener_error_relativo(valor_real,valor_representativo):
    error_absoluto = obtener_error_absoluto(valor_real,valor_representativo)
    resultado = error_absoluto / valor_real
    return resultado

# ambos parametros son float de 64 bits
def obtener_error_cuadratico(valor_real,valor_representativo):
    resultado = valor_real - valor_representativo
    resultado = resultado * resultado
    return resultado
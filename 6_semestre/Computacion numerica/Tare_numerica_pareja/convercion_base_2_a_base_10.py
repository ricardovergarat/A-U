import numpy as np

# binario es un string positivo
def cambio_binario_a_base_10_entero(binario):
    sumatoria = np.int64(0)
    dos = np.int64(2)
    for i in range(len(binario)):
        sumatoria = sumatoria + ( np.int64(int(binario[i])) * ( dos ** ( np.int64(len(binario) - 1 - i) ) ) )
    return sumatoria

# base es un int de 64 bits, exponente es un int de 32 bits positivo
def potencia_negativa(base,exponente):
    if exponente == 0:
        return 1
    else:
        exponente = np.int64(exponente)
        decimal = np.float64(1.0)
        for i in range(exponente):
            decimal = decimal / base
        return decimal

# binario es un string positivo
def cambio_binario_a_base_10_decimal(binario):
    sumatoria = np.float64(0)
    dos = np.int64(2)
    for i in range(len(binario)):
        sumatoria = sumatoria + ( np.int64(int(binario[i])) * potencia_negativa(dos,i + 1) )
    return sumatoria

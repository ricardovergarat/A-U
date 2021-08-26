def obtener_polinomio(lista,x):
    sumatoria = 0
    for i in range(len(lista)):
        x_elevado = obtener_potencia(x,len(lista) - 1 - i)
        sumatoria = sumatoria + ( lista[i] * x_elevado )
    return sumatoria

def obtener_potencia(base,potencia):
    if potencia == 0:
        return 1
    for i in range(potencia - 1):
        base = base * base
    return base


def generar_primos(a,b):
    primos = obtener_primos(b)
    primos_finales = []
    for i in range(len(primos)):
        if a <= primos[i] <= b:
            primos_finales.append(primos[i])
    return primos_finales

def obtener_primos(n):
    primos = []
    for i in range(n):
        valido = es_primo(i + 1, primos)
        print(i)
        if valido == True:
            primos.append(i + 1)
    return primos

def es_primo(n,lista_de_primos):
    if n == 2:
        return True
    elif n == 1:
        return False
    else:
        for i in range(len(lista_de_primos)):
            if n % lista_de_primos[i] == 0:
                return False
        return True




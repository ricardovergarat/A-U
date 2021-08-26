from primos import *
from minimo_comun_multiplo import *

def obtener_m_c_d(lista):
    maximo = obtener_maximo(lista)
    primos = obtener_primos(maximo)
    divisores = []
    while True:
        for i in range(len(primos)):
            validez = obtener_respuesta_AND_elementos(primos[i],lista)
            if validez == True:
                for j in range(len(lista)):
                    lista[j] = lista[j] / primos[i]
                divisores.append(primos[i])
                break
        if i == len(primos) - 1:
            break
    divisores = multiplicar_elementos(divisores)
    return divisores

def obtener_respuesta_AND_elementos(n,lista):
    p = True
    for i in range(len(lista)):
        q = division_entera(n,lista[i])
        p = p and q
    return p
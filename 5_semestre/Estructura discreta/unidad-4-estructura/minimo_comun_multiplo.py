from primos import *

def obtener_m_c_m(lista):
    maximo = obtener_maximo(lista)
    primos = obtener_primos(maximo)
    multiplos = []
    while True:
        son_uno = todos_son_1(lista)
        if son_uno == True:
            break
        else:
            for i in range(len(primos)):
                validez = obtener_respuesta_OR_elementos(primos[i],lista)
                if validez == True:
                    for j in range(len(lista)):
                        una_division_entera = division_entera(primos[i],lista[j])
                        if una_division_entera == True:
                            lista[j] = lista[j] / primos[i]
                    multiplos.append(primos[i])
                    break
    multiplos = multiplicar_elementos(multiplos)
    return multiplos

def obtener_respuesta_OR_elementos(n,lista):
    p = False
    for i in range(len(lista)):
        q = division_entera(n,lista[i])
        p = p or q
    return p


def division_entera(a,b):
    if b % a == 0:
        return True
    return False

def obtener_maximo(lista):
    maximo = max(lista)
    return maximo

def todos_son_1(lista):
    for i in range(len(lista)):
        if lista[i] != 1:
            return False
    return True

def multiplicar_elementos(lista):
    multiplicacion = 1
    for i in range(len(lista)):
        multiplicacion = multiplicacion * lista[i]
    return multiplicacion
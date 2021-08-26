import math

def obtener_esperanza(lista_cuantitativa,lista_datos):
    sumatoria = 0
    for i in range(len(lista_cuantitativa)):
        suma = lista_cuantitativa[i] * lista_datos[i]
        sumatoria = sumatoria + suma
    return sumatoria

def obtener_varianza(lista_cuantitativa,lista_datos):
    media = obtener_esperanza(lista_cuantitativa,lista_datos)
    sumatoria = 0
    for i in range(len(lista_cuantitativa)):
        suma = (lista_cuantitativa[i] * lista_cuantitativa[i]) * lista_datos[i]
        sumatoria = sumatoria + suma
    varianza = sumatoria - (media * media)
    return varianza

def obtener_desviacion_estandar(lista_cuantitativa,lista_datos):
    varianza = obtener_varianza(lista_cuantitativa,lista_datos)
    desviacion = math.sqrt(varianza)
    return desviacion
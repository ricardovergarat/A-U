from cociente_y_residuo import *

def algoritmo_euclidiano(a,b,lista=[]):
    solucion = obtener_cociente_residuo(a,b)
    lista.append(solucion)
    if solucion[6] == 0:
        return lista
    else:
        return algoritmo_euclidiano(b,solucion[6],lista)
from el_algoritmo_euclidiano import *

def obtener_mcd_metodo_clase(a,b):
    lista = algoritmo_euclidiano(a,b)
    return lista[len(lista) - 2][6]
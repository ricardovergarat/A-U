from el_algoritmo_euclidiano import *

def despejar_resto(lista):
    solucion = [ lista[6],"=",lista[0],"-",lista[2],"X",lista[4] ]
    return solucion

def obtener_despejes_cocientes_residuo(lista,largo):
    despejes = []
    for i in range(largo - 1):
        despeje_n = despejar_resto(lista[i])
        despejes.append(despeje_n)
    return despejes
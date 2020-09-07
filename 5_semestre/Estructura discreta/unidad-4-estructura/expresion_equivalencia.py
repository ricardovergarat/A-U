
def obtener_su_equivalencia(lista):
    return lista[2:7]

def expresar_en_string(lista):
    linea = "("
    for i in range(len(lista)):
        linea = linea + str(lista[i])
    linea = linea + ")"
    return linea

def obtener_expresion_equivalencia(lista_restos):
    expresion = lista_restos[len(lista_restos) - 1]
    print(expresion)

import numpy as np

# Entero es un int de 64 bits positivo
def cambio_base_10_a_binario_entero(entero):
    dos = np.int64(2)
    convercion = ""
    while entero >= dos:
        # iremos agrupando la parte entera a la derecha la primera vez, los siguientes digitos se pondran a la izquirda del anterior en vez de agregar siempre por la derecha y luego invertir el string al final
        convercion = str(entero % dos) + convercion
        entero = np.int64(entero / dos)
    convercion = str(entero) + convercion
    return convercion

# numero es un float de 64 bits
def obtener_parte_decimal(numero):
    numero = numero - np.int64(numero)
    return numero

# numero es la parte decimal de un float de 64 bits (ejemplo: 0.80 - 0.34 - 0.6456), el numero siempre sera positivo
def cambio_base_10_a_binario_decimal(numero):
    convercion = ""
    # Esto es para cortar el proceso si el producto del numero por la base es un numero que ya conseguimos, de no ser asi sacara numero de ya en la convercion y lo hara infinitamente
    numero_repetidos = []
    dos = np.int64(2)
    continuar = True
    while continuar != False:
        # Como ayuda descomentar las siguientes dos lineas
        #print("repetidos: ",numero_repetidos)
        #print(numero," X ",dos," = ",np.float64(numero * dos))
        numero = np.float64(numero * dos)
        convercion = convercion + str(int(numero))
        if ((numero == np.float64(1.0)) or (np.float32(numero) in numero_repetidos)): # el float 32 es para conservar las numeros a 64 cumpliendo la condicion del programa e ignorar unos decimales al final del float de 64 bits
            continuar = False
        else:
            numero_repetidos.append(np.float32(numero))
            numero = obtener_parte_decimal(numero)
    return convercion

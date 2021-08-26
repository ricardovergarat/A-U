# integrantes
# isidora varela
# ricardo vergara

import numpy as np
import random
import os
from convercion_base_10_a_base_2 import *
from convercion_base_2_a_base_10 import *
from resta_binaria_programa import *
import matplotlib.pyplot as plt
from formulas import *

# maximo es un int que debe ser mayor o igual a 80 y es el rango de los numeros aleatorios
def crear_lista(maximo=100):
    if maximo < 80:
        maximo = 80
    lista = []
    for i in range(maximo):
        numero_aleatorio = random.uniform(-maximo,maximo) # numero float de 32 bits
        numero_aleatorio = np.float64(numero_aleatorio)
        lista.append(numero_aleatorio)
    return lista

# numero es un float de 64
def determinar_signo(numero):
    if numero < 0:
        return "negativo"
    return "positivo"

# numero es un float de 64 bits
def convertir_a_binario(numero):
    signo = determinar_signo(numero)
    if signo == "negativo":
        numero = numero * np.int64(-1)
    # ahora numero siempre es positivo, el signo lo agregaremos en la salida
    entero = np.int64(numero)
    decimal = obtener_parte_decimal(numero)
    entero_binario = cambio_base_10_a_binario_entero(entero)
    decimal_binario = cambio_base_10_a_binario_decimal(decimal)
    if signo == "negativo":
        return "-" + entero_binario + "." + decimal_binario
    return entero_binario + "." + decimal_binario

# Aqui cada elemento de la lista(solo floats de 64 bits) sera pasado a binario
def convertir_elementos_a_binario(lista):
    lista_resultado = []
    for i in range(len(lista)):
        binario = convertir_a_binario(lista[i])
        lista_resultado.append(binario)
    return lista_resultado

# binario es un string positivo, lado es un caracter, puede ser el caracter "i" o "d" de izquierda y derecha, largo deseado es un int positivo
# Esto esta para agregar numeros si el no cummple con la cantidad de cifras significativas
def complementar_numero(binario,lado,largo_deseado):
    if lado == "i":
        while len(binario) != largo_deseado:
            binario = "0" + binario
    else:
        # implica que lado es "d"
        while len(binario) != largo_deseado:
            binario = binario + "0"
    return binario

# binario es un string con parte entera y decimal
# cantidad de cifras es un int entre 36 y 50, ambos incluidos
def recuperar_sifras_significativas(binario,cantidad_cifras):
    cantidad_negativos = binario.count("-")
    binario = binario.replace("-","")
    if len(binario) >= (cantidad_cifras + 2):
        binario = binario[0:cantidad_cifras + 2]
    else:
        while len(binario) != (cantidad_cifras + 2):
            binario = binario + "0"
    if cantidad_negativos == 1:
        return "-" + binario
    return binario

# Cada binario de la lista sera modificado para solo tener "n" digitos en la parte decimal, este "n" es el parametro "cantidad_cifras"
def recuperar_cifras_significativas_en_la_lista(lista,cantidad_cifras):
    lista_resultado = []
    for i in range(len(lista)):
        binario_recortado = recuperar_sifras_significativas(lista[i],cantidad_cifras)
        lista_resultado.append(binario_recortado)
    return lista_resultado

# a y b son float de 64 bits (pueden ser positivos o negativos)
def suma_real(a,b):
    c = a + b
    # el float64 de abajo es solo porseacaso
    return np.float64(c)

# obtendremos la suma de los elementos sub i de cada lista, cada elemento de las listas son floats de 64 bits
def obtener_suma_real_lista(lista_1,lista_2):
    lista_resultado = []
    for i in range(len(lista_1)):
        suma = suma_real(lista_1[i],lista_2[i])
        lista_resultado.append(suma)
    return lista_resultado

# Los parametros "digitos" son caracteres, estos caracteres solo pueden ser 0 o 1
# reserva es int que sera siempre 0 o 1
def declarar_suma_binaria(digito_1,digito_2,reserva):
    # aqui no es nesesario usar el int64 por que es solo un digito y este puede ser 0 o 1
    digito_1 = int(digito_1)
    digito_2 = int(digito_2)
    suma = digito_1 + digito_2 + reserva
    if suma == 0:
        return "0",0
    if suma == 1:
        return "1",0
    if suma == 2:
        return "0",1
    else:
        return "1",1

# a y b son binarios en formato string, reserva es un int que puede ser 0 o 1
# Esto puede sumar dos binarios (eso no mas) (deje de leer los comentarios) (ustede no aprende verdad)
# lado es un caracter que puede ser "i" o "d", esto es por que debemos agregar 0 a izquieda o derecha dependiendo si sumamos la parte decimal o entera
def suma_entera_binaria(a,b,reserva,lado):
    if len(a) > len(b):
        b = complementar_numero(b,lado,len(a))
    if len(b) > len(a):
        a = complementar_numero(a,lado,len(b))
    # aqui tienen la misma cantidad de digitos
    resultado = ""
    for i in range(len(a)):
        suma,reserva = declarar_suma_binaria(a[len(a) - 1 - i],b[len(b) - 1 - i],reserva)
        resultado = suma + resultado
    return resultado,reserva

# a y b son binarios decimales, ejemplo: -1010110110.10101010101010 o 10101.101010010010010 (pueden ser positivos o negativos)
def suma_binaria(a,b):
    cantidad_negativos_a = a.count("-")
    cantidad_negativos_b = b.count("-")
    if cantidad_negativos_a == cantidad_negativos_b:
        # implica que a y b tienen signos iguales, es decir ambos son positivos o negativos
        # si ambos son negativos daremos los numero como positivos a la suma y luego agregaremos el signo negativo
        # si ambos son positivos solo debemos retornar la suma
        a = a.replace("-","")
        b = b.replace("-","")
        entero_a,decimal_a = a.split(".")
        entero_b,decimal_b = b.split(".")
        reserva = 0
        suma_decimal,reserva = suma_entera_binaria(decimal_a,decimal_b,reserva,"d")
        suma_entera,reserva = suma_entera_binaria(entero_a,entero_b,reserva,"i")
        if reserva == 1:
            suma_entera = "1" + suma_entera
        resultado = suma_entera + "." + suma_decimal
        if cantidad_negativos_a == 1:
            resultado = "-" + resultado
        return resultado
    else:
        return resta_binaria(a,b)

# Esta funcion sumara los binarios sub i de cada lista
def obtener_suma_binaria_en_la_lista(lista_1,lista_2):
    lista_resultado = []
    for i in range(len(lista_1)):
        suma = suma_binaria(lista_1[i],lista_2[i])
        #print("i: ",i,"   b1: ",lista_1[i],"   b2: ",lista_2[i]," :   ",suma)
        lista_resultado.append(suma)
    return lista_resultado

# Esta funcion convertir un binario con parte entera y decimal a un numero
# lista es una lista, donde cada elemento es un string binario con parte entera y deciaml (puden ser positivos o negativos)
def obtener_trasformacion_base_10_lista(lista):
    lista_resultado = []
    for i in range(len(lista)):
        cantidad_negativo = lista[i].count("-")
        lista[i] = lista[i].replace("-","")
        entero_binario,decimal_binario = lista[i].split(".")
        decimal_base_10 = cambio_binario_a_base_10_decimal(decimal_binario)
        entero_base_10 = cambio_binario_a_base_10_entero(entero_binario)
        numero = entero_base_10 + decimal_base_10
        if cantidad_negativo == 1:
            numero = numero * np.int64(-1)
        lista_resultado.append(numero)
    return lista_resultado

# Esta funcion calcula todos los errores relativos de los elementos sub i de las listas
# ambos parametros son listas, donde cada elemnto son float de 64 bits
def obtener_error_relativo_en_la_lista(lista_1,lista_2):
    lista_resultado = []
    for i in range(len(lista_1)):
        erro_relativo = obtener_error_relativo(lista_1[i],lista_2[i])
        lista_resultado.append(erro_relativo)
    return lista_resultado

# Esta funcion calcula todos los errores absolutos de los elementos sub i de las listas
# ambos parametros son listas, donde cada elemnto son float de 64 bits
def obtener_error_absoluto_en_la_lista(lista_1,lista_2):
    lista_resultado = []
    for i in range(len(lista_1)):
        error_absoluto = obtener_error_absoluto(lista_1[i],lista_2[i])
        lista_resultado.append(error_absoluto)
    return lista_resultado

# Esta funcion esta para graficar la suma_real y la suma_real_binaria ya habiendola transformada en floats de 64 bits
def grafico_comparacion(lista_1,lista_2):
    plt.plot(lista_1,label="suma real",color="b",linestyle="-")
    plt.plot(lista_2,label="suma real binaria",color="g",linestyle="--")
    plt.legend()
    plt.show()

# Esta funcion grafica los datos que recibe
# lista es una lista, los elementos solo nesesitan ser numero, no estan restringidos por algunto tipo de numero
# contenido label es un string, esta para ser proyectado en el grafico y saber que representa los datos del grafico
def grafico_proyecion(lista,contenido_label):
    plt.plot(lista,label=contenido_label,color="g",linestyle="-")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    # Algoritmo generico
    # 1 - crear lista
    # 2 - convertir lista a 64 bits
    # 3 - convertir a binario (parte int) (parte decimal)
    # 4 - recuperar binarios con cifras significativas
    # 5 - crear lista de sumas
    # 6 - crear lista de sumas binarias
    # 7 - convertir binarios a float64
    # 8 - evaluar numeros en las formulas (formulas 1) (formula 2) (formula 3)
    # 9 - proyectar resultados
    os.system("cls")
    # 1 - crear lista
    # 2 - convertir lista a 64 bits
    operandos_1 = crear_lista()
    operandos_1 = [-62.12911417845515, 3.3516837333462632, 32.87041144170527, 84.64767762832582, -57.48136969688924, -2.443862914822276, 29.64434176828044, 39.17181818301887, 29.752982268710696, -9.576735465866975, 76.01141791432116, -6.501226730638692, -10.222641532050275, 24.460695734315934, 15.085751450839439, 73.90411359303539, -36.19880091333052, -10.17772973730007, 16.981651844782107, -59.07705608803442, -49.30014011866859, 45.92169313827469, 17.9818646860966, -95.12101720855289, -29.951864623046532, 52.54337680939969, 67.01290015140586, -77.60887585655063, 52.81428780589931, 98.70579375772161, -1.6435487828325677, 10.608753535863215, 71.72707379172792, -16.81485754736198, -37.60508774219866, -35.07600471403434, -41.990243844520215, 82.81462871214393, -14.252896583563484, 74.46642667052018, 57.10825833662591, 92.3182205005794, -60.536552401349965, 77.25662049173118, -85.31002344163852, 26.49559222154072, 6.056684819864159, 0.37656557542192104, -89.7150777612115, 18.289763969964042, -4.889733029196151, 85.95288970816335, 53.29331605005626, -68.98567826836467, 59.95563564754096, 7.8850983290142125, -32.98220010735801, -4.48353793700818, 61.38424642315803, -42.59313134572695, -68.50532447652947, -90.36259467677381, -78.73092187613918, 69.34580911083472, -1.8083423068136852, 39.63583847621359, -76.31517750408278, 1.994468486153039, 44.044917591808115, -84.26424005442463, -28.923415738929663, -79.11988637526895, 31.894443574062223, -76.85980566294883, -7.910448529378812, -6.399950863553158, 63.26361048353786, -69.67483890737594, -86.00590008452463, -45.052787984077526, -75.20713572261542, 30.480250580638113, -11.237474007669718, 56.57825000864767, -69.37013285472855, 45.60764155941038, 12.547499087678531, -71.52472033729231, 55.31572421133336, -93.17241988621947, -6.918767524026961, -34.830965105745776, 39.10898683764921, 34.45828713961453, -80.37446896857492,24.741765445858903, 6.367280959676691, 6.62974970751165, 5.914576382165549, 77.41559496564975]
    operandos_2 = crear_lista()
    operandos_2 = [45.05539253653521, -46.783845769738775, -19.41043678195868, 40.87822028613141, 12.943193460419408, -51.01301182633811, 65.47240282414313, -27.91019027750137, -88.95065521544723, -78.49788794244164, 20.016178350907126, 52.02177473428122, 44.76645920552295, 55.90677321158668, -2.918212482607615, 33.44082078311453, -17.867397717591544, -7.431585303073348, -29.802230159496744, -27.993707121819924, -65.4800481047092, 82.95937041303637, -91.03069367061039, 56.641544854005815, -18.60611868803204, 92.79572571518872, 28.934594403620792, -21.89387078820984, -78.1592915552479, 82.370214298517, -74.16130913516722, -8.052608249115963, 33.06626899802288, -70.63888856680929, 64.03495384890573, -6.970058209270306, -11.876157559298946, 92.03531620270434, 74.67136536337503, 26.777919502689613, -8.229000615584738, -32.17570065050444, 81.6562250949211, 66.88041527845752, 73.28244377070021, -38.66205137566601, 80.5672771761815, 75.71475669374988, -87.96427358349821, -36.30319900068826, 44.53070765780353, 62.271890357725226, 51.14153904463237, 89.92275156597486, 79.45138146386336, -23.324276106342225, 83.91934794273214, -73.50224792692666, -39.27394628206484, 25.703195564442154, -58.582492628781566, -6.371597951711166, -50.146380716975614, -20.31459141990733, 43.96190451918335, 90.40787661577252, -11.242416739014544, 10.302741898012286, -9.40778827968849, 26.19253264598727, 53.927560919420415, -26.147012706937872, 87.7120205282213, 75.58308577706512, 87.89626211303155, -84.75661377147996, 10.417569797614007, 83.93855833728477, -5.137997237080441, -90.22386854289456, -18.340807595149485, 73.95828523093212, -91.89514098246892, 73.96097198953493, -27.428248341132246, 72.66868300381014, 56.77451632976425, 1.7848379283508677, -41.91561779273283, 94.07570979945382, 73.18167286929676, 52.554736952521665, 86.41055199899566, -23.041022185317743, 79.76499395832008, 74.34747794728455, 50.57129578219656, -52.388500721844466, -94.99604278067369, -65.01910045365838]
    print(operandos_1)
    print("\n")
    print(operandos_2)
    # 3 - convertir a binario (parte int) (parte decimal)
    operandos_1_binario = convertir_elementos_a_binario(operandos_1)
    operandos_2_binario = convertir_elementos_a_binario(operandos_2)
    # 4 - recuperar binarios con cifras significativas
    operandos_1_binario = recuperar_cifras_significativas_en_la_lista(operandos_1_binario, 36)
    operandos_2_binario = recuperar_cifras_significativas_en_la_lista(operandos_2_binario, 36)
    print("\n")
    print(operandos_1_binario)
    print("\n")
    print(operandos_2_binario)
    # 5 - crear lista de sumas
    suma_real = obtener_suma_real_lista(operandos_1,operandos_2)
    # 6 - crear lista de sumas binarias
    suma_binaria = obtener_suma_binaria_en_la_lista(operandos_1_binario, operandos_2_binario)
    # 7 - convertir binarios a float64
    suma_binaria_transformada = obtener_trasformacion_base_10_lista(suma_binaria)
    print("\n")
    print(suma_real)
    print("\n")
    print(suma_binaria_transformada)
    # 8 - evaluar numeros en las formulas (formulas 1) (formula 2) (formula 3)
    errores_absolutos = obtener_error_absoluto_en_la_lista(suma_real,suma_binaria_transformada)
    errores_relativos = obtener_error_relativo_en_la_lista(suma_real,suma_binaria_transformada)
    # 9 - proyectar resultados
    grafico_comparacion(suma_real,suma_binaria_transformada)
    grafico_proyecion(errores_absolutos,"error absoluto")
    grafico_proyecion(errores_relativos,"error relativo")

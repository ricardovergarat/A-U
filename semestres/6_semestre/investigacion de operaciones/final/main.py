import csv
import os
from arbol import *

def recuperar_datos(nombre):
    with open(nombre,encoding = "utf-8") as archivo:
        lineas = csv.reader(archivo)
        datos = []
        for row in lineas:
            datos.append(row)
    return datos

def convertir_a_numeros(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            lista[i][j] = int(lista[i][j])
    return lista

def es_entero(numero):
    numero = numero - int(numero)
    if numero == 0:
        return True
    return False

def obtener_P0(lista,cantidad_sifras_significativas):
    for i in range(len(lista[0])):
        lista[0][i] = lista[0][i] * (-1)
    restriciones = []
    resultado_restricion = []
    for i in range(1,len(lista)):
        restriciones.append(lista[i][0:len(lista[i]) - 1])
        resultado_restricion.append(lista[i][len(lista[i]) - 1])
    P0 = proceso("P0",lista[0],restriciones,resultado_restricion,cantidad_sifras_significativas)
    return P0

def algoritmo(P0,cantidad_sifras_significativas):
    i = 1
    P0.mostrar_proceso()
    raiz = nodo(P0)
    extremos = raiz.obtener_extremos()
    cota = max(extremos)
    z_es_entero = es_entero(cota)
    while z_es_entero != True:
        raiz.crear_ramificacion("P" + str(i),"P" + str(i + 1),cota,cantidad_sifras_significativas)
        extremos = raiz.obtener_extremos()
        cota = max(extremos)
        z_es_entero = es_entero(cota)
        P_n_solucion_temporal = raiz.obtener_solucion(cota)
        X_n_es_entero = P_n_solucion_temporal.son_soluciones_enteras(cantidad_sifras_significativas)
        print(X_n_es_entero)
        z_es_entero = z_es_entero and X_n_es_entero
        print("los extremos son: ",extremos," la cota es: ",cota," es entero: ",z_es_entero)
        i = i + 2
    print("---------")
    P_n_solucion = raiz.obtener_solucion(cota)
    P_n_solucion.mostrar_proceso()
    return P_n_solucion








if __name__ == '__main__':
    os.system("cls")
    datos = recuperar_datos("ecuacion.csv")
    datos = convertir_a_numeros(datos)
    cifras_significativas = datos[len(datos) - 1][0] # quitaremos la cantidad de sifras significativas de los datos
    datos = datos[0:len(datos) - 1]
    P0 = obtener_P0(datos,cifras_significativas)
    print("------------")
    P_n_solucion = algoritmo(P0,cifras_significativas)
    for i in range(len(P_n_solucion.soluciones)):
        print(round(P_n_solucion.soluciones[i],cifras_significativas))





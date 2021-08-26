from main import complementar_numero
from convercion_base_2_a_base_10 import *
from convercion_base_10_a_base_2 import *
import numpy as np

# a y b son caracteres, esto caracteres solo pueden ser 0 o 1
def declarar_resta_binaria(a,b):
    if a == "0" and b == "0":
        return "0","0"
    if a == "0" and b == "1":
        return "1","1"
    if a == "1" and b == "0":
        return "1","0"
    if a == "1" and b == "1":
        return "0","0"

# Adiferencia de la suma la resta binaria es mas complicada, debido a que restar solo dos digitos tiene un proceso largo, esta funcion hace eso (conclusion: esta funcion resta dos digitos)
# Los parametros son caracteres, estos caracteres solo pueden ser 0 o 1
def resta_digitos_binarios(a,b,retroceso):
    if retroceso == "0":
        resta,retroceso = declarar_resta_binaria(a,b)
        return resta,retroceso
    else:
        resta,retroceso_1 = declarar_resta_binaria(a,retroceso)
        resta,retroceso_2 = declarar_resta_binaria(resta,b)
        if retroceso_1 == "1" or retroceso_2 == "1":
            return resta,"1"
        return resta,"0"

# Esta funcion dice que parametro es mayor, regresaremos "a" en caso de que el primero sea el mayor,"b" si es el mayor y en caso de ser iguales "c"
# El motivo de esta funcion es para sumar binarios con distinto signo, cuando pasemos los binarios a restar a la funcion haremos que siempre su primer parametro sea mayor y esto funciona conocer el mayor
# a y b son string binarios
# lado es un caracter, puede ser el caracter "i" o "d", de izquierda y derecha, esto esta por si tenemos que comparar numerod y no tienen la misma cantida digitos rellenaremos con ceros, pero lo ceros se agrean dependiendo de si es numero entero o decimal
def comparar_string(a,b,lado):
    if len(a) > len(b):
        b = complementar_numero(b,lado,len(a))
    if len(b) > len(a):
        a = complementar_numero(a,lado,len(b))
    # aqui tienen la misma cantidad de digitos
    for i in range(len(a)):
        if a[i] > b[i]:
            return "a"
        if a[i] < b[i]:
            return "b"
    return "c"

# a y b son binarios en formato string (siempre son positivos)
# esta funcion tiene como restricion que "a" debe ser mayor o igual a "b", de no ser asi llamaremos a esta misma funcion en el orden correcto ya cumpliendo la restricion
def resta_entera_binaria(a,b,lado):
    mayor = comparar_string(a,b,lado)
    if mayor == "a" or mayor == "c": # esto implica que "a" en efecto es mayor o "a" y "b" son iguales
        if len(a) > len(b):
            b = complementar_numero(b,lado,len(a))
        if len(b) > len(a):
            a = complementar_numero(a,lado,len(b))
        # aqui tiene la misma cantidad de digitos
        resultado = ""
        retrocesos = "0"
        for i in range(len(a)):
            resta,retrocesos = resta_digitos_binarios(a[len(a) - 1 - i], b[len(b) - 1 - i],retrocesos)
            resultado = resta + resultado
        return resultado,"0" # este cero significa que debemos restar cero a la parte entera cuando recibe la parte decimalo de un binario
        # como aclaracion siempre llegara a este punto cuando recibe un binario que representa la parte entera, ya que en otra funcion obligaremos a que restemos al numero mayor
        # como aclaracion 2 un "numero" se compone de parte entera y parte decimal, es decir llamaremos dos veces a esta funcion para restar la parte decimal y luego la parte entera
        # cuando llamamosa a la funcion con la parte decimal existe el caso de que primer numero sea menor, entonces ahi ira el else de esta funcion, pero tendremos que restar uno en la parte entera, y para eso el uno en el return del else
        # cuando llamamos a esta funcion con la parte entera deberemos restar el 0 o 1 con esta misma funcion
        # ahora solo consiste en restar las partes enteras sin problema y ya que en esta parte entera "SIEMPRE" el primer numero sera mayor no tendremos que quitar uno a otro numero, por eso este siempre sera el final
    else:
        # b es mayor que "a"
        resultado,retrocesos = resta_entera_binaria(b,a,lado)
        retrocesos = "1" # este uno significa que deberemos restar uno a la parte entera cuando recibe la parte decimal de un binario,cunado recibe la parte entera nunca llegara aqui
        return resultado,retrocesos

# La resta binaria en la parte decimal tiene un proceso distinto
# Por el motivo si el primer parametro es menor que el segundo
# De ser asi tendremos que hacer el proceso del "else" para tener el resultado correcto en la parte decimal
# a y b son string binarios positivos
def resta_decimal_binaria(a,b):
    mayor = comparar_string(a,b,"d")
    if mayor == "a" or mayor == "c":
        resultado,retroceso = resta_entera_binaria(a,b,"d")
        return resultado,retroceso
    else:
        # implica que b es mayor, y es un proceso mas complicado
        resultado,inutil = resta_entera_binaria(b,a,"d")
        b_base_10 = cambio_binario_a_base_10_decimal(b)
        string_numero_base_10 = str(b_base_10)
        string_numero_base_10 = string_numero_base_10[2:len(string_numero_base_10)]
        n = "1"
        for i in range(len(string_numero_base_10)):
            n = n + "0"
        #print("debo restar: ",n," - ",string_numero_base_10)
        n_binario = cambio_base_10_a_binario_entero(np.int64(n))
        resultado,retroceso = resta_entera_binaria(n_binario,resultado,"i")
        retroceso = "1"
        return resultado,retroceso

# a y b son binarios decimales, es decir tiene parte entera y decimal
# a y b tiene signo distintos siempre
def resta_binaria(a,b):
    cantidad_negativo_a = a.count("-")
    cantidad_negativo_b = b.count("-")
    a = a.replace("-","")
    b = b.replace("-","")
    entero_a,decimal_a = a.split(".")
    entero_b,decimal_b = b.split(".")
    mayor = comparar_string(entero_a,entero_b,"i")
    if mayor == "c":
        # tienen el mismo numero entero,entonces compararemos la parte decimal para saber cual es mayor
        mayor = comparar_string(decimal_a,decimal_b,"d")
        if mayor == "a" or mayor == "c":
            # implica que el "a" es mayor o son el mismo numeroo en la parte entera y decimal asi que da los mismo el orden, pero pondremos "a" primero por que si
            resta_decimal,retroceso = resta_decimal_binaria(decimal_a,decimal_b)
            entero_a,inutil = resta_entera_binaria(entero_a,retroceso,"i")
            resta_entera,inutil = resta_entera_binaria(entero_a,entero_b,"i")
            if mayor == "c":
                return resta_entera + "." + resta_decimal
            if cantidad_negativo_a == 1:
                return "-" + resta_entera + "." + resta_decimal
            return resta_entera + "." + resta_decimal
        else:
            # imlica que el numero mayor es b
            resta_decimal,retroceso = resta_decimal_binaria(decimal_b,decimal_a)
            entero_b,inutil = resta_entera_binaria(entero_b,retroceso,"i")
            resta_entera,inutil = resta_entera_binaria(entero_b,entero_a,"i")
            if cantidad_negativo_b == 1:
                return "-" + resta_entera + "." + resta_decimal
            return resta_entera + "." + resta_decimal
    else:
        # implica que son distintos
        if mayor == "a":
            resta_decimal,retroceso = resta_decimal_binaria(decimal_a,decimal_b)
            entero_a,inutil = resta_entera_binaria(entero_a,retroceso,"i")
            resta_entera,inutil = resta_entera_binaria(entero_a,entero_b,"i")
            if cantidad_negativo_a == 1:
                return "-" + resta_entera + "." + resta_decimal
            return resta_entera + "." + resta_decimal
        else:
            # implica que b es mayor
            resta_decimal,retroceso = resta_decimal_binaria(decimal_b,decimal_a)
            entero_b,inutil = resta_entera_binaria(entero_b,retroceso,"i")
            resta_entera,inutil = resta_entera_binaria(entero_b,entero_a,"i")
            if cantidad_negativo_b == 1:
                return "-" + resta_entera + "." + resta_decimal
            return resta_entera + "." + resta_decimal

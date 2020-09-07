from tablas import *
from Bernoulli import *
from distribucion_binomial import *
from poisson import *

def sumar(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    return sumatoria

def estandarizacion(x,media,desviacion):
    numerador = x - media
    return numerador / desviacion

if __name__ == "__main__":
    print("hola mundo")
    x = [0,1,2,3,4,5,6,7,8,9,10]
    y = [0.038,0.057,0.056,0.091,0.152,0.189,0.150,0.103,0.072,0.051,0.042]
    s = sumar(y)
    print(s)
    esperanza = obtener_esperanza(x,y)
    print(esperanza)
    var = obtener_varianza(x,y)
    print(var)
    des = obtener_desviacion_estandar(x,y)
    print(des)
    raro = estandarizacion(549,495,40)
    print(raro)
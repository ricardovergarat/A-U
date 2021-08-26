def obtener_promedio(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    return sumatoria / len(lista)

def esta_de_menor_a_mayor(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def ordenar_numeros_menor_a_mayor(lista):
    ordenado = esta_de_menor_a_mayor(lista)
    while ordenado != True:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                respaldo = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = respaldo
        ordenado = esta_de_menor_a_mayor(lista)
    return lista

def contar_elemento(lista,elemento):
    cantidad = lista.count(elemento)
    return cantidad

def redondear(numero,cantidad_de_decimales):
    numero = round(numero, cantidad_de_decimales)
    return numero

def obtener_desviacion_estandar(lista,n):
    promedio = obtener_promedio(lista)
    promedio = redondear(promedio, 2)
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + (lista[i] - promedio)**2
    if n == 1:
        resultado = (sumatoria / len(lista))** (1/2)
    else:
        resultado = (sumatoria / ( len(lista) - 1) )** (1/2)
    resultado = redondear(resultado,2)
    return resultado

def obtener_mediana(lista):
    lista = ordenar_numeros_menor_a_mayor(lista)
    n = ( len(lista) + 1 ) / 2
    print(len(lista))
    print(lista)
    print(n)
    #print(n % int(n))
    if n % int(n) == 0:
        print(lista)
        print("mediana: ",lista[int(n) - 1])
        return lista[int(n)]
    else:
        print(lista)
        print("medianas: ",lista[int(n) - 1],"---",lista[int(n)])
        promedio = obtener_promedio([ lista[int(n) - 1],lista[int(n)] ])
        print("media final: ",promedio)
        return promedio

def obtener_cuartiles(lista):
    lista = ordenar_numeros_menor_a_mayor(lista)

def abrir_archivo(nombre):
    archivo = open(nombre)
    datos = archivo.readlines()
    datos = quitar_enter(datos)
    archivo.close()
    return datos

def quitar_enter(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].replace("\n","")
    return lista

def convertir_a_numero(lista):
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    return lista

def obtener_rango(lista):
    lista = ordenar_numeros_menor_a_mayor(lista)
    min = lista[0]
    max = lista[len(lista) - 1]
    print(lista)
    return max - min

if __name__ == "__main__":
    print("hola mundo")
    edad = abrir_archivo("edad.txt")
    edad = convertir_a_numero(edad)
    nivel = abrir_archivo("educacion.txt")
    zona = abrir_archivo("zona.txt")
    sexo = abrir_archivo("sexo.txt")
    net = abrir_archivo("net.txt")
    trabajo = abrir_archivo("trabajo.txt")
    estatura = abrir_archivo("metros.txt")
    estatura = convertir_a_numero(estatura)
    #estatura = ordenar_numeros_menor_a_mayor(estatura)
    print(edad)
    print(nivel)
    print(zona)
    print(sexo)
    print(net)
    print(trabajo)
    print(estatura)
    print("------------------------")
    respuesta = obtener_mediana(estatura)
    print(respuesta)

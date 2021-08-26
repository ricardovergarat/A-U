import math

def abrir_archivo():
	nombre = "10.txt" #--------------------------------------------> esto es lo unico que cambia ejemplo "2.txt","3.txt","4.txt",.......,"10.txt"
	print(nombre)
	archivo = open(nombre) 
	lineas = archivo.readlines()
	lineas = quitar_enter(lineas)
	return lineas

def quitar_enter(lista):
	x = 0
	while x != len(lista):
		lista[x] = lista[x].replace("\n","")
		x = x + 1
	return lista

def separar_tiempo(lista):
	x = 0
	los_timepos = []
	while x != len(lista):
		tiempo_y_matrix = lista[x].split(":")
		tiempo = tiempo_y_matrix[2].split(" ")
		los_timepos.append(tiempo[1])
		x = x + 1
	return los_timepos

def convertir_a_numero(lista):
	x = 0
	while x != len(lista):
		lista[x] = float(lista[x])
		x = x + 1
	return lista

def obtener_tiempo_promedio(lista):
	x = 0
	sumatoria = 0
	while x != len(lista):
		sumatoria = sumatoria + lista[x]
		x = x + 1
	print("timepo promedio es: ",sumatoria/len(lista))
	return (sumatoria/len(lista))

def desviacion_estandar(lista,promedio):
	x = 0
	sumatoria = 0
	while x != len(lista):
		sumatoria = sumatoria + (lista[x] - promedio)**2
		x =  x + 1
	numero_de_la_raiz = sumatoria / ( len(lista) - 1 )
	desviacion = math.sqrt(numero_de_la_raiz)
	print("desviacion estandar: ",desviacion)


if __name__ == "__main__":
 	texto = abrir_archivo()
 	tiempo = separar_tiempo(texto)
 	tiempo_numeros = convertir_a_numero(tiempo)
 	promedio = obtener_tiempo_promedio(tiempo_numeros)
 	desviacion_estandar(tiempo_numeros,promedio)



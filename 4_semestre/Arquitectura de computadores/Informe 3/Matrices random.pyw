from tkinter import *
import os
import random

def obtener_ruta():
	return os.getcwd()

def determinar_resolucion():
	pantalla = Tk()
	ancho = pantalla.winfo_screenwidth()
	alto = pantalla.winfo_screenheight()
	pantalla.destroy()
	return ancho,alto

def centrar_ejes(x,y,tamano):
	x = (x / 2) - (tamano / 2)
	y = (y / 2) - (tamano / 2)
	return x,y

def GUI(x,y,tamano):
	ventana = Tk()
	ventana.title("Matrices random") 
	ventana.resizable(0,0)
	ventana.geometry("%dx%d+%d+%d" % (tamano,tamano,x,y))

	Label(text="Ruta de salida").place(x=10,y=10)
	Label(text="Orden de matriz").place(x=10,y=30)
	Label(text="Rango minimo").place(x=10,y=50)
	Label(text="Rango maximo").place(x=10,y=70)
	Label(text="Cantidad de matrices").place(x=10,y=90)

	Button(ventana,text="Generar",command=lambda:recuperar(entry_ruta.get(),entry_orden.get(),entry_minimo.get(),entry_maximo.get(),entry_cantidad.get())).place(x=200,y=130)

	entry_ruta = StringVar()
	entry_ruta.set(ruta)
	Entry(ventana,textvariable=entry_ruta,width=30).place(x=140,y=10)
	entry_orden = StringVar()
	Entry(ventana,textvariable=entry_orden,width=5).place(x=140,y=30)
	entry_minimo = StringVar()
	Entry(ventana,textvariable=entry_minimo,width=5).place(x=140,y=50)
	entry_maximo = StringVar()
	Entry(ventana,textvariable=entry_maximo,width=5).place(x=140,y=70)
	entry_cantidad = StringVar()
	Entry(ventana,textvariable=entry_cantidad,width=5).place(x=140,y=90)

	ventana.mainloop()

def recuperar(ruta,orden,minimo,maximo,cantidad):
	n = son_numeros(orden,minimo,maximo,cantidad)
	if n == True:
		error = detectar_error(int(orden),int(minimo),int(maximo),int(cantidad))
		if error == True:
			escribir(["error"],ruta)
		else:
			i = 0
			Lista_de_matrices = []
			for i in range(int(cantidad)):
				matriz = crear_matriz(int(orden),int(minimo),int(maximo))
				matriz = matriz_a_string(matriz)
				Lista_de_matrices.append(matriz)
			try:
				escribir(Lista_de_matrices,ruta)
			except:
				escribir(["error",ruta])
	else:
		escribir(["error"],ruta)

def son_numeros(orden,minimo,maximo,cantidad):
	a = orden.isdigit()
	b = minimo.isdigit()
	c = maximo.isdigit()
	d = cantidad.isdigit()
	if a and b and c and d:
		return True
	return False
		
def detectar_error(orden,minimo,maximo,cantidad):
	if orden  <= 0:
		return True
	if minimo < 0:
		return True
	if maximo < 0:
		return True
	if  cantidad <= 0:
		return True
	return False
	
def crear_matriz(orden,minimo,maximo):
	i = 0
	M = ["["]
	for i in range(orden):
		j = 0
		for j in range(orden):
			n = aleatorio(minimo,maximo)
			M.append(n)
			if j == orden - 1:
				pass
			else:
				M.append(",")
		if i == orden - 1:
			pass
		else:
			M.append(";")
	M.append("]")
	return M

def aleatorio(minimo,maximo):
	numero = random.randint(minimo,maximo)
	return str(numero)

def matriz_a_string(lista):
	i = 0
	string = ""
	for i in range(len(lista)):
		string = string + lista[i]
	return string

def escribir(lista,ruta):
	string = "\\muerte a omar.txt"
	ruta = ruta + string
	agregar = open(ruta,"w")
	contador = 0
	while contador < len(lista):
		agregar.write(lista[contador] + "\n" )
		contador = contador + 1
	agregar.close()


if __name__ == "__main__":
	ruta = obtener_ruta()
	x,y = determinar_resolucion()
	x,y = centrar_ejes(x,y,500)
	GUI(x,y,500)
	
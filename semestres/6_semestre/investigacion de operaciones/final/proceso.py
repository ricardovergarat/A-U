from scipy.optimize import linprog

class proceso:
    nombre = None
    funcion_objetivo = None
    restriciones = None
    valores_restriciones = None
    soluciones = None
    z = None

    def __init__(self,_nombre,_funcion_objetivo,_restriciones,_valores_restriciones,cantidad_sifras_significativas):
        self.nombre = _nombre
        self.funcion_objetivo = _funcion_objetivo
        self.restriciones = _restriciones
        self.valores_restriciones = _valores_restriciones
        resultado = linprog(self.funcion_objetivo,self.restriciones,self.valores_restriciones,bounds=(0,None))
        self.soluciones = resultado.x
        self.z = round(resultado.fun * (-1),cantidad_sifras_significativas) # valor redondeado con signo positivo

    def obtener_valor_ramificacion(self,cantidad_sifras_significativas):
        for i in range(len(self.soluciones)):
            solucion_aprox = round(self.soluciones[i],cantidad_sifras_significativas)
            numero = solucion_aprox - int(solucion_aprox)
            #print("numero es:", numero)
            #numero = round(numero,cantidad_sifras_significativas)
            #print("numero es:",numero)
            if numero != 0.0: # regresaremos el primer numero decimal
                print("ramificaremos: ",round(self.soluciones[i],cantidad_sifras_significativas)," como: ",int(self.soluciones[i])," y ",int(self.soluciones[i]) + 1," soluciones: ",self.soluciones," con indice: ",i)
                return int(self.soluciones[i]),i

    def mostrar_proceso(self):
        print("nombre: ",self.nombre," restriciones: ",self.restriciones," valores: ",self.valores_restriciones," soluciones: ",self.soluciones," z: ",self.z)

    def comprobar_factibilidad(self,cota):
        #print(cota," > ",self.z)
        if cota < self.z:
            self.z = None

    def son_soluciones_enteras(self,cantidad_sifras_significativas):
        for i in range(len(self.soluciones)):
            solucion_aprox = round(self.soluciones[i], cantidad_sifras_significativas)
            numero = solucion_aprox - int(solucion_aprox)
            if numero != 0.0:
                return False
        return True
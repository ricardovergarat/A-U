class nodo:
    izquierda = None
    centro = None
    derecha = None

    def __init__(self,dato):
        self.centro = dato

    def agregar_dato(self,dato):
        if dato < self.centro:
            if self.izquierda == None:
                nuevo_nodo = nodo(dato)
                self.izquierda = nuevo_nodo
            else:
                self.izquierda.agregar_dato(dato)
        else:
            if self.derecha == None:
                nuevo_nodo = nodo(dato)
                self.derecha = nuevo_nodo
            else:
                self.derecha.agregar_dato(dato)

    def obtener_lista(self):
        salida = []
        if self.izquierda == None:
            salida.append("_")
        else:
            salida.append(self.izquierda.obtener_lista())
        salida.append(self.centro)
        if self.derecha == None:
            salida.append("_")
        else:
            salida.append(self.derecha.obtener_lista())
        return salida

    def mostrar_arbol(self):
        if self.izquierda != None:
            self.izquierda.mostrar_arbol()
        print(self.centro)
        if self.derecha != None:
            self.derecha.mostrar_arbol()

    def obtener_lista_ordenada(self):
        lado_izquierdo = []
        lado_derecho = []
        if self.izquierda != None:
            lado_izquierdo = self.izquierda.obtener_lista_ordenada()
        if self.derecha != None:
            lado_derecho = self.derecha.obtener_lista_ordenada()
        return lado_izquierdo + [self.centro] + lado_derecho




if __name__ == "__main__":
    raiz = nodo(45)
    print(raiz.izquierda)
    print(raiz.centro)
    print(raiz.derecha)
    a = raiz.obtener_lista()
    print(a)
    raiz.agregar_dato(33)
    raiz.agregar_dato(50)
    raiz.agregar_dato(30)
    a = raiz.obtener_lista()
    print(a)
    raiz.mostrar_arbol()
    b = raiz.obtener_lista_ordenada()
    print(b)
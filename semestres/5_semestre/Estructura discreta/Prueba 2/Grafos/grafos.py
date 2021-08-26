class grafo:
    vertices = []
    aristas = []
    matriz_adyacente = []

    def __init__(self,_vertices,_aristas,_largo = 0):
        #G(V,A)
        self.vertices = _vertices
        self.aristas = _aristas
        self.largo = _largo

    def mostrar_vertices(self):
        print(self.vertices)

    def mostrar_aristas(self):
        print(self.aristas)

    def obtner_matriz_adyacente(self):
        matriz = []
        for i in range(len(self.vertices)):
            fila_n = []
            for j in range(len(self.vertices)):
                if (self.vertices[i],j + 1) in self.aristas: # j + 1 por que suelen poner vertices 1 o mayor y no 0 o mayor
                    fila_n.append(1)
                else:
                    fila_n.append(0)
            matriz.append(fila_n)
        self.matriz_adyacente = matriz

    def mostrar_matriz_adyacente(self):
        for i in range(len(self.matriz_adyacente)):
            fila = ""
            for j in range(len(self.matriz_adyacente[i])):
                fila = fila + str(self.matriz_adyacente[i][j]) + " "
            print(fila)



if __name__ == "__main__":
    print("hola")
    G = grafo([1,2,3,4],[(1,4),(1,2),(2,3),(4,3),(2,4)]) # (1,4),(4,1),(1,2),(2,1),(2,3),(3,2),(4,3),(3,4),(2,4)
    G.mostrar_vertices()
    G.mostrar_aristas()
    G.obtner_matriz_adyacente()
    G.mostrar_matriz_adyacente()

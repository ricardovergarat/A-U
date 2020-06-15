class grafo:
    vertices = []
    aristas = []
    def __init__(self,_vertices,_aristas):
        self.vertices = _vertices
        self.aristas = _aristas

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
        for i in range(len(self.vertices)):
            fila = ""
            for j in range(len(self.vertices)):
                fila = fila + str(matriz[i][j]) + " "
            print(fila)
            #print(matriz[i])


if __name__ == "__main__":
    print("hola")
    G = grafo([1,2,3,4],[(1,4),(1,2),(2,3),(4,3),(2,4)]) # (1,4),(4,1),(1,2),(2,1),(2,3),(3,2),(4,3),(3,4),(2,4)
    G.mostrar_vertices()
    G.mostrar_aristas()
    G.obtner_matriz_adyacente()
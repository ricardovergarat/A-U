from proceso import *

class nodo:
    izquierda = None
    centro = None
    derecha = None

    def __init__(self,proceso_n):
        self.centro = proceso_n

    def crear_ramificacion(self,P_i,P_i_mas_1,cota,cantidad_sifras_significativas):
        if self.izquierda == None and self.derecha == None:
            n,indice = self.centro.obtener_valor_ramificacion(cantidad_sifras_significativas)
            nueva_restricion_izquierda = []
            nueva_restricion_derecha = []
            for i in range(len(self.centro.funcion_objetivo)):
                if i == indice:
                    nueva_restricion_izquierda.append(1)
                    nueva_restricion_derecha.append(-1)
                else:
                    nueva_restricion_izquierda.append(0)
                    nueva_restricion_derecha.append(0)
            ramificacion_izquierda = proceso(P_i,self.centro.funcion_objetivo,self.centro.restriciones + [nueva_restricion_izquierda],self.centro.valores_restriciones + [n],cantidad_sifras_significativas)
            ramificacion_izquierda.comprobar_factibilidad(self.centro.z)
            ramificacion_izquierda.mostrar_proceso()
            ramificacion_derecha = proceso(P_i_mas_1,self.centro.funcion_objetivo,self.centro.restriciones + [nueva_restricion_derecha],self.centro.valores_restriciones + [-(n + 1)],cantidad_sifras_significativas)
            ramificacion_derecha.comprobar_factibilidad(self.centro.z)
            ramificacion_derecha.mostrar_proceso()
            nuevo_nodo_izquierdo = nodo(ramificacion_izquierda)
            nuevo_nodo_derecho = nodo(ramificacion_derecha)
            self.izquierda = nuevo_nodo_izquierdo
            self.derecha = nuevo_nodo_derecho
        else:
            if cota <= self.izquierda.centro.z:
                self.izquierda.crear_ramificacion(P_i,P_i_mas_1,cota,cantidad_sifras_significativas)
            else:
                # cota <= self.derecha.centro.z
                self.derecha.crear_ramificacion(P_i,P_i_mas_1, cota,cantidad_sifras_significativas)

    def obtener_extremos(self):
        if self.izquierda == None and self.derecha == None:
            if self.centro.z == None:
                return []
            return [self.centro.z]
        else:
            return self.izquierda.obtener_extremos() + self.derecha.obtener_extremos()

    def obtener_solucion(self,cota):
        if cota == self.centro.z:
            return self.centro
        else:
            if self.izquierda.centro.z != None and self.derecha.centro.z != None:
                distancias = [abs(self.izquierda.centro.z - cota),abs(self.derecha.centro.z - cota )]
                menor = min(distancias)
                if distancias[0] == menor:
                    return self.izquierda.obtener_solucion(cota)
                else:
                    return self.derecha.obtener_solucion(cota)
            else:
                # alguno es null
                if self.izquierda.centro.z == None:
                    return self.derecha.obtener_solucion(cota)
                else:
                    return self.izquierda.obtener_solucion(cota)

from scipy.optimize import linprog



if __name__ == "__main__":
    print(True )
    funcion_objetivo = [-4,-7,-6,-5,-4]
    restriciones = [[5, 8, 3, 2, 7], [1, 8, 6, 5, 4], [1, 0, 0, 0, 0], [0, 0, -1, 0, 0],[-1,0,0,0,0],[0,0,0,1,0],[0,0,-1,0,0]]
    resultados_restriciones =  [23, 22, 3, -1,-3,2,-2]
    resultado = linprog(funcion_objetivo,restriciones,resultados_restriciones,bounds=(0,None))
    print(resultado.x)
    print(round(resultado.fun * (-1),3))
    print("---------")
    for i in range(len(resultado.x)):
        print(round(resultado.x[i],3))

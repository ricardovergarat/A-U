
def combinacion(lista,n):
    combinacion = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] + lista[j] == n:
                combinacion.append([ lista[i],lista[j] ])
    print(combinacion)
    return combinacion


if __name__ == "__main__":
    dado = [1,2,3,4,5,6]
    x_5 = {(1,4),(2,3),(3,2),(4,1)}
    x_7 = {(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)}
    x_9 = {(3,6),(4,5),(5,4),(6,3)}
    x_5 & x_7
    print(set())
    print(len(x_5))
    print(len(x_7))
    print(len(x_9))
    print(len(x_5 | x_7 | x_9))
    x_5 = combinacion(dado,5)
    x_7 = combinacion(dado,7)
    x_9 = combinacion(dado,9)
    print(len(x_5))
    print(len(x_7))
    print(len(x_9))
    print(len(x_5) + len(x_7) + len(x_9))

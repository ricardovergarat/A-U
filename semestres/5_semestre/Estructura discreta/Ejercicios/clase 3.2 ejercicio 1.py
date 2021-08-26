import random

def combinaciones(lista):
    combinaciones = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            combinaciones.append([lista[i],lista[j]])
    return combinaciones

def palomar(lista,n):
    cajas = []
    for i in range(n):
        cajas.append([])
    print("k = ", int(len(lista)/n))
    for i in range(len(lista)):
        cajas[random.randint(0, len(cajas) - 1 )].append(lista[i])
    print(cajas)
    for i in range(len(cajas)):
        print("El numero de elementos en la caja, ", i + 1, " son ", len(cajas[i]))



if __name__ == "__main__":
    alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    palomar(alf,9)

    # n = 9
    # m = 27
    # k = m / n

        # implica que encontraremos ALOMENOS K cajas con cardinalidad K
    #com = combinaciones(alf)
    #print(com)
    #palomar(com,4)
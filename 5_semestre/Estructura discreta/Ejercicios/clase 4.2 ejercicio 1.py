from itertools import permutations

def promefe_malo(lista):
    n = len(lista)
    j = n - 2
    while lista[j] > lista[j + 1]:
        j = j + 1
    k = n - 1
    while lista[j] > lista[k]:
        k = k - 1
    temp = lista[j]
    lista[j] = lista[k]
    lista[k] = temp
    r = n - 1
    s = j + 1
    while r > s:
        temp = lista[r]
        lista[r] = lista[s]
        lista[s] = temp
        r = r - 1
        s = s + 1
    return lista

def malisimo(lista):
    print("malisimo")
    c = 0
    lista.sort()
    n = len(lista)
    while c < factorial(n):
        print("entro al while")
        if c == 0:
            yield lista
        else:
            yield promefe_malo(lista)
        c = c + 1

def factorial(n):
    if n == 1:
        return 0
    else:
        return n * factorial(n-1)



        

if __name__ == "__main__":
    for i,p in enumerate(permutations(list("hola"))):
        print(i,p)
    print("-------------------")
    for i,p in enumerate(malisimo(list("hola"))):
        print(i,p)
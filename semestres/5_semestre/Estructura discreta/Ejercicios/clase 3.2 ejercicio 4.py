import random

def examen(lista,n):
    examen = []
    for i in range(n):  # por que N estudiantes aprobaron este examen (asi lo dice el enunciado)
        examen.append(random.randint(0, len(lista) - 1))
    examen = set(examen)
    return examen


if __name__ == "__main__":
    total = 150
    final  = total - ( 60 + 70 + 50 - 80 - 80 - 80 )
    A = range(150)
    A = list(A)
    A = set(A) # los comvierte a llaves
    examen_1 = examen(A,60)
    examen_2 = examen(A, 70)
    examen_3 = examen(A, 50)
    print(A)
    print("------")
    print(examen_1)
    print("------")
    print(examen_2)
    print("------")
    print(examen_3)
    universo_examen = len(examen_1) + len(examen_2) + len(examen_3) - len(examen_1 & examen_2) - len(examen_1 & examen_3) - len(examen_2 & examen_3) + len(examen_1 & examen_2 & examen_3)
    print(universo_examen)
    reprobados = total - universo_examen
    print(reprobados)
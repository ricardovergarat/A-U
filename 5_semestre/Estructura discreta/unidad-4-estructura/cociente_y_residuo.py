def obtener_cociente_residuo(a,b):
    if a < 0:
        if b > 0:
            division = obtener_division(-a,b)
            resto = obtener_resto(-a,b)
            expresion = [a,"=",b,"X",(-division) - 1,"+",b - resto]
        else:
            division = obtener_division(-a, -b)
            resto = obtener_resto(-a, -b)
            expresion = [a, "=", b, "X", (division) + 1, "+", (-b) - resto]
    else:
        if b > 0:
            division = obtener_division(a,b)
            resto = obtener_resto(a, b)
            expresion = [a, "=", b, "X", division, "+", resto]
        else:
            division = obtener_division(a,-b)
            resto = obtener_resto(a,-b)
            expresion = [a, "=",b, "X", -division, "+", resto]
    return expresion

def obtener_division(a,b):
    c = a / b
    return int(c)

def obtener_resto(a,b):
    c = a % b
    return c

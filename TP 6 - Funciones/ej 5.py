""" Desarrollar la funcion singo(n), que reciba un número entero y devuelva 1, -1 o 0 según
el valor recibido sea positivo, negativo o nulo """

def signo():
    n = int(input("Ingrese un valor"))
    if n > 0:
        a = 1
    elif n < 0:
        a = -1
    else:
        a = 0
    return a

resultado = signo()
print(resultado) 
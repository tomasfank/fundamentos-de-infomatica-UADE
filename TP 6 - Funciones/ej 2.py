""" Dados dos parámetros enteros A y B, obtener A elevado a la B mediante multiplicaciones
sucesivas, utilizando la funcion del ejercicio anterior para multiplicar.
Por ejemplo 4 elevado a la 3 = 4 * 4 * 4. """

num1 = int(input("Ingrese un número"))
num2 = int(input("¿Por qué valor desea elevarlo?"))

def potencia(a, b):
    contador = 0
    acumulador = 1
    while contador < b:
        contador = contador + 1
        operacion = a * acumulador
        acumulador = operacion
    return acumulador

resultado = potencia(num1, num2)
print("El resultado es =", resultado)
        
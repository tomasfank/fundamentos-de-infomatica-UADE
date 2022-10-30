""" Escribir una función que reciba como parámetros dos números enteros.
Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamente
sumas. Por ejemplo 4 * 3 = 4 + 4 + 4. """

num1 = int(input("Ingrese un número "))
num2 = int(input("¿Por que valor le gustaría multiplicarlo? "))

def multiplicacion (a, b):
    contador = 0
    acumulador = 0
    while contador < b:
        contador = contador + 1
        operacion = a + acumulador
        acumulador = operacion
    return acumulador

resultado = multiplicacion(num1, num2)
print("El resultado es = ", resultado)
        
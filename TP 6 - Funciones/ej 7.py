""" Calcular y devolver el máximo común divisor de dos enteros no negativos, basándose
en las siguientes formulas matemáticas:
    - MCD(x,x) = x
    - MCD(x, y) = MCD(y, x)
    - Si x > y => MCD(x, y) = MCD(x-y, y)
Ejemplo: MCD(40, 15) devuelve 5 """

num1 = int(input("Ingrese el primer número "))
num2 = int(input("Ingrese el segundo número "))

def mcd(a, b):
    while a % b != 0: #Utilicé el algoritmo de Euclides.
        c = a % b
        a = b
        b = c
    return c

resultado = mcd(num1, num2)
print(resultado)
    
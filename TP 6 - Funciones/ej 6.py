""" Escribir la funcion comparar(a, b) que reciba como parámetro dos números enteros y devuelva
1 si el primero es mayor que el segundo, 0 si son iguales y -1 si el primero es menor que el
segundo """

def comparar(a, b):
    if a > b:
        res = 1
    elif a < b:
        res = -1
    else:
        res = 0
    return res

num1 = int(input("ingrese A = "))
num2 = int(input("ingrese B = "))
programa = comparar(num1, num2)
print(programa) 
""" Utilizando el ejercicio 1: calcular la suma de los números de la lista"""

#vector
lista = []

#función
def entrada(a, b):
    num = int(input("Ingrese un valor"))
    suma = 0
    while num != -1:
        if (num >= a) and (num <= b):
            lista.append(num)
        elif (num >= b) and (num <= a):
            lista.append(num)
        elif (num == a) and (num == b):
            lista.append(num)
        else:
            print("Ingrese valores dentro del parámetro")
        suma = suma + num 
        num = int(input("Ingrese otro valor"))
    return suma
   
   
#parámetros
A = int(input("Ingrese el primer parámetro"))
B = int(input("Ingrese el segundo parámetro"))

#programa
inicio = entrada(A, B)
print(lista)
print("La suma de los números de la lista es =", inicio) 

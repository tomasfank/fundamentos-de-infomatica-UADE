""" Escribir una función para ingresar desde el teclado una serie de números entre A y B, y guardarlos
en una lista. En casno de ingresar un valor fuera de rango la función mostrará un mensaje de error
y solicitará un nuevo número. Para finalizar la carga se debera ingresar -1. La función recibe como
parámetros los valores de A y B, y devuelve la lista cargada (o vacía, si el usuario no ingresa nada)
como valor de retorno. Tener en cuenta que A puese ser mayor, menor o igual a B. """

#vector
lista = []

#función
def entrada(a, b):
    num = int(input("Ingresa un valor"))
    while num != -1:
        if (num >= a) and (num <= b):
            lista.append(num)
        elif (num >= b) and (num <= a):
            lista.append(num)
        elif (num == a) and (num == b):
            lista.append(num)
        else:
            print("Valores fuera de rango")
        num = int(input("Ingresa otro valor"))
        
#parámetros
min = int(input("Ingrese el parámetro A "))
max = int(input("Ingrese el parámetro B ")) 

#programa 
inicio = entrada(min, max) 
print(lista)
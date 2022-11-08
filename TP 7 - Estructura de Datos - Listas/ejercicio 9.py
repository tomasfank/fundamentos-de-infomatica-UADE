"""
Crear una lista de N números generados al azar entre 0 y 100 pero sin
elementos repetidos. El valor de N se ingresa por teclado. Resolver este
problema utilizando dos estrategias distintas:
    -Impidiendo el agregado de elementos repetidos
    -Eliminando duplicados luego de generar la lista. Asegurarse que
    la cantidad final de elementos sea la solicitada.
"""

#modulo random
import random

#creamos la lista
def crear_lista():
    N = int(input("Cuantos elementos desea cargar?"))
    i = 0 #contador 
    lista = [] 
    lista.append(random.randint(0,100)) #agregamos un primer valor a la lista
    while i <= N:
        num = random.randint(0,100) #generamos un segundo número y a continuacion lo comparamos con el primero
        if num not in lista: #si "num" no esta en la lista entonces será agregado a la misma 
            lista.append(num)
        i = i + 1 #sumamos al contador para no entrar en bucle    
    return lista #retornamos la lista

#ordenamos la lista para comprobar de manera más fácil que efectivamente ningun valor esta repetido
def ordenar(a):
    largo = len(a) 
    for i in range(largo-1):
        for j in range(i+1, largo):
            if a[i] > a[j]:
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
    return a

a = crear_lista()
print(a)
b = ordenar(a)
print(b) 
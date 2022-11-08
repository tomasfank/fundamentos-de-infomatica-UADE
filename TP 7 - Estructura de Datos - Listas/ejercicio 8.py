""" Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar
e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el
mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las
posiciones que ocupe. La carga de datos termina cuando se obtenga un 0
como número al azar, el que no deberá cargarse a la lista """

import random

def cargar_lista():
    lista = []
    i = 0
    lista.append(random.randint(0,100))
    while lista[i] > 0:
        i = i + 1
        lista.append(random.randint(0,100))
    del lista[len(lista)-1]
    return lista

def buscar_min(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo

def buscar(lista):
    minimo = lista[0]
    pos = []
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            pos.append(minimo)
    return pos

def borrar_min(lista, dato):
    i = 0
    minimo = dato
    while i < len(lista):
        if lista[i] == minimo:
            del lista[i]
            i = i-1
        i = i+1
    return lista
        
            
a = cargar_lista()
print(a)
b = buscar_min(a)
print("el minimo es", b)
d = buscar(a)
print("esta en las pos", d)
c = borrar_min(a, b)
print(c) 
    
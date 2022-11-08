""" Práctica de métodos de ordenamiento:
    1) Método de selección
    2) Método de inserción
    3) Método de burbujeo
"""

#importamos modulo random
import random

#creamos lista
def crear_lista():
    n = int(input("cantidad de numeros a cargar "))
    lista = []
    for i in range(n):
        lista.append(random.randint(0, 100))
    return lista

#ordenamos usando método de selección
def ordenar_seleccion(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

#ordenamos usando método de inserción
def ordenar_insercion(lista):
    for i in range(1, len(lista)): #range(1, len(lista)) quiere decir que empezamos a ordenar desde el segundo elemento
        aux = lista[i]
        j = i
        while j>0 and lista[j-1] > aux:
            lista[j] = lista[j-1]
            j = j-1
        lista[j] = aux
    return lista

#ordenamos usando método de burbujeo
def ordenar_burbujeo(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenado = True
    return lista

#programa
a = crear_lista()
print("La lista es")
print(a)
b = ordenar_seleccion(a)
print("La lista ordenada por selección")
print(b)
c = ordenar_insercion(a)
print("La lista ordenada por insercion")
print(c)
d = ordenar_burbujeo(a)
print("La lista ordenada por burbujeo")
print(d)
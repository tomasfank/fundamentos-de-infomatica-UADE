""" Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar
e imprimir el valor mínimo y el lugar que ocupa. Tener en cuenta que el
mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las
posiciones que ocupe. La carga de datos termina cuando se obtenga un 0
como número al azar, el que no deberá cargarse a la lista """

#módulo random
import random

#generamos la lista al azar hasta que se genere el valor 0
def cargar_lista():
    lista = []
    i = 0
    lista.append(random.randint(0,100))
    while lista[i] > 0: #mientras el valor generado no sea 0 seguimos acumulando valores
        i = i + 1
        lista.append(random.randint(0,100))
    del lista[len(lista)-1]
    return lista

#buscamos el valor mínimo en la lista
def buscar_min(lista):
    minimo = lista[0]
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo #retornamos el valor mínimo

#buscamos todas las posiciones en las que se encuentra el valor mínimo 
def buscar(lista):
    minimo = lista[0]
    pos = []
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            pos.append(minimo)
    return pos #retornamos las posiciones del valor mínimo 

#eliminamos el valor mínimo de todas las posiciones 
def borrar_min(lista, dato):
    i = 0
    minimo = dato
    while i < len(lista):
        if lista[i] == minimo:
            del lista[i]
            i = i-1
        i = i+1
    return lista
        
#programa principal            
a = cargar_lista()
print(a)
b = buscar_min(a)
print("el minimo es", b)
d = buscar(a)
print("esta en las pos", d)
c = borrar_min(a, b)
print(c) 
    
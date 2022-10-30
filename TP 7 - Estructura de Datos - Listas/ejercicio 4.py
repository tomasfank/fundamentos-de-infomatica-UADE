""" Escribir una función para devolver la primera posición que ocupa un valor pasado como
parámetro, utilizando busqueda secuencial en una lista desordenada. La funcion debe devolver
-1 si el elemento no se encuentra en la lista """

import random

#funciones
def cargarLista(cant):
    lista = []
    for i in range(cant):
        lista.append(random.randint(0, 100))
    return lista

def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
#programa principal
cantidad = int(input("¿Cuántos elementos desea cargar?"))
parametro = int(input("Ingrese el valor parámetro que desea encontrar"))
miLista = cargarLista(cantidad)
imprimirLista(miLista) 
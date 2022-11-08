""" Escribir una función para devolver una lista con todas las posiciones que ocupa un valor
pasado como parámetro, utilizando búsqueda secuencial en una lista desordenada. La función debe
devolver una lista vacía si el elemento no se encuentra en la lista original. """

#modulo random 
import random

def cargarLista(cant):
    lista = []
    for i in range(cant):
        lista.append(random.randint(0, 100))
    return lista

def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i],end=" ")
    print()
    
def busquedaSecuencial(lista, dato):
    i = 0
    pos = []
    while i < len(lista):
        if lista[i] == dato:
            pos.append(i)
        i = i + 1
    return pos

cantidad = int(input("¿Cuántos elementos desea cargar? "))
miLista = cargarLista(cantidad)
imprimirLista(miLista)
parametro = int(input("Ingrese el valor parámetro que desea encontrar "))
posicion = busquedaSecuencial(miLista, parametro)
print("El elemento", parametro, "se encontró en la posición", posicion) 

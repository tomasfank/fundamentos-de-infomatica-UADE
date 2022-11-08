"""Ejercicio 1
Escribir un programa que utilice funciones para:
Cargar una lista de N elementos con números enteros entre 50 y 780 obtenidos al azar.
El valor de N se ingresa por teclado.
Ordenar la lista en forma ascendente utilizando cualquier método de ordenamiento estudiado.
Pedir un dato al usuario y buscarlo con búsqueda binaria e informar su posición o -1 sino se encuentra.
Luego eliminar de la lista, el valor minimo en todas sus posiciones.
Imprimir por pantalla la lista luego de realizar cada tarea."""

#importar modulo random
import random

#funciones

#cargamos la lista
def cargar_lista():
    cantidad = int(input("¿Cúantos números desea cargar?"))
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(50, 780))
    return lista

#ordenamos la lista utilizando el método de inserción
def ordenar_lista(miLista):
    for i in range(1, len(miLista)):
        aux = miLista[i]
        j = i
        while j > 0 and miLista[j-1] > aux:
            miLista[j] = miLista[j-1]
            j = j-1
            miLista[j] = aux
    return miLista
    
#búsqueda binaria
def busqueda_binaria(v):
    izq = 0
    der = len(v) - 1
    pos = -1
    dato = int(input("Ingrese el número que desea buscar"))
    while izq <= der and pos == -1:
        centro = (izq + der) //2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izq = centro +1 
        else:
            der = centro - 1
    return pos

#obtener mínimo de la lista desordenada 
def obtener_min(v):
    min = v[0]
    for i in range(len(v) - 1):
        if v[i] < min:
            min = v[i]
    return min

#eliminar mínimo de la lista desordenada
def eliminar_min(desordenada, minimo):
    min = minimo
    i = 0
    while i < len(desordenada):
        if desordenada[i] == min:
            del desordenada[i]
            i = i - 1
        i = i + 1
    return desordenada

#programa principal
inicio = cargar_lista()
print("La lista es:")
print(inicio)
print("Lista ordenada:")
ordenar = ordenar_lista(inicio)
print(ordenar)
buscar = busqueda_binaria(ordenar)
#evaluamos si el dato buscado está en la lista
if buscar == -1:
    print("No se encontro el número que buscas")
else:
    print("El número que buscas esta en la posición", buscar)
obtenerMin = obtener_min(inicio)
eliminarMin = eliminar_min(inicio, obtenerMin)
print("El mímino de la lista es", obtenerMin, "la lista queda:")
print(eliminarMin)
    
    
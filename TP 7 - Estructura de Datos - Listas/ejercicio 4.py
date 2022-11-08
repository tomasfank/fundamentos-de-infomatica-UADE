""" Escribir una función para devolver la primera posición que ocupa un valor pasado como
parámetro, utilizando busqueda secuencial en una lista desordenada. La funcion debe devolver
-1 si el elemento no se encuentra en la lista """

#El modulo "random" es una función que se agrega al programa a través de la instrucción "import".
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
    
def busquedaSecuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1
    
#programa principal
cantidad = int(input("¿Cuántos elementos desea cargar? "))
miLista = cargarLista(cantidad)
imprimirLista(miLista)
parametro = int(input("Ingrese el valor parámetro que desea encontrar "))
posicion = busquedaSecuencial(miLista, parametro)
if posicion >= 0:
    print("El elemento", parametro, "se encontró en la posición", posicion + 1) #sumo 1 para que la primera posición se 1 y no 0
else:
    print("El elemento", parametro, "no se encuentra en la lista")
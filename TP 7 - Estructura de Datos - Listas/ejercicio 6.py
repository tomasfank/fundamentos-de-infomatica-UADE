""" Ídem anterior, utilizando busqueda binaria sobre una lista ordenada """

#modulo random
import random

#FUNCIONES
#Cargamos la lista
def cargarLista(cant):
    lista = []
    for i in range(cant):
        lista.append(random.randint(0, 100))
    return lista

#Ordenamos utilizando método de selección
def ordenarLista(v):
    largo = len(v)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux 
    return v 

#Realizamos busqueda binaria 
def busquedaBinaria(lista, dato):
    izq = 0 
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro +1 
        else:
            der = centro -1
    return pos 

#Imprimimos la lista
def imprimirLista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

#PROGRAMA PRINCIPAL
cantidad_Elementos  = int(input("¿Cúantos elementos desea cargar?"))
lista_Desordenada = cargarLista(cantidad_Elementos)
imprimir_Desordenada = imprimirLista(lista_Desordenada)
lista_Ordenada = ordenarLista(lista_Desordenada)
imprimir_Ordenada = imprimirLista(lista_Ordenada)
dato_Buscado = int(input("¿Qué dato desea encontrar?"))
busqueda = busquedaBinaria(lista_Ordenada, dato_Buscado)
print(busqueda)
if  busqueda == -1:                                      
    print("El dato que buscas no se encuentra en la lista")
else:
    print("El dato que buscas se encuentra en la posición/es", busqueda)

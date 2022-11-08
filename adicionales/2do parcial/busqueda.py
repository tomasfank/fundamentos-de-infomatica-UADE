""" Metodos de busqueda """

#módulo random
import random

#cargamos una lista
def cargar_lista():
    N = int(input("cantidad de elementos en la lista"))
    lista = []
    for i in range(N):
        lista.append(random.randint(0,100))
    return lista

#la ordenamos con cualquier metodo 
def ordenar_lista(a):
    largo = len(a)
    for i in range(largo - 1):
        for j in range(i+1, largo):
            if a[i] > a[j]:
                aux = a[i]
                a[i] = a[j]
                a[j] = aux
    return a

#busqueda binaria
def binaria(lista):
    dato = int(input("que dato desea encontrar con busqueda binaria"))
    izq = 0
    der = len(lista) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if lista[centro] == dato:
            pos = centro
        elif lista[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

#busqueda secuencial
def secuencial(lista):
    dato = int(input("que dato desea encontrar con busqueda secuencial"))
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i + 1
    if i < len(lista):
        return i
    else:
        return -1

a = cargar_lista()
print("La lista desordenada es")
print(a)
b = ordenar_lista(a)
print("La lista ordenada es")
print(b)
c = binaria(b)
if c == -1:
    print("El dato no esta en la lista")
else:
    print("El dato esta en la posicion", c)
d1 = secuencial(a) #secuencial desordenada
if d1 == -1:
    print("El dato no esta en la lista")
else:
    print("El dato esta en la posicion", d1)
d2 = secuencial(b) #secuencial ordenada
if d2 == -1:
    print("El dato no esta en la lista")
else:
    print("El dato esta en la posicion", d2)


import random

def lista_1(n):
    lista1 = []
    for i in range(n):
        lista1.append(random.randint(0,50))
    return lista1

def lista_2(n):
    lista2 = []
    for i in range(n):
        lista2.append(random.randint(0,50))
    return lista2

N = int(input("Cuantos valores tendra cada lista"))
a1 = lista_1(N)
a2 = lista_2(N)
print(a1)
print(a2)


""" Utilizando el ejercicio 1: determinar si la lista es capicúa """

#vector
lista = []

#funcion
def entrada(a, b):
    num = int(input("Ingrese un valor = "))
    while num != -1:
        if (num >= a) and (num <= b):
            lista.append(num)
        elif (num >= b) and (num <= a):
            lista.append(num)
        elif (num == a) and (num == b):
            lista.append(num)
        else:
            print("Ingrese un valor dentro del rango")
        num = int(input("Ingrese otro valor = "))

def capicua(a):
    listaInvertida = a[::-1]
    print("La lista invertida es =", listaInvertida)
    if a == listaInvertida:
        print("La lista es capicúa")
    else:
        print("La lista no es capicúa")
    
#programa
parametro_1 = int(input("Ingrese un parámetro = "))
parametro_2 = int(input("Ingrese el otro parámetro = "))
armarLista = entrada(parametro_1, parametro_2)
print("La lista ingresada es = ", lista)
verificaCapicua = capicua(lista)


'''Ejercicio 2
Cargar una lista con números ingresados por un usuario hasta que se ingresa un -1
(fin de a carga de los datos) y reemplazar un valor en una posición determinada por el usuario.
Imprimir la lista antes y después del reemplazo.'''


#cargamos una lista creada con datos ingresados por el usuario
def cargar_lista():
    ingresa = int(input("Ingrese un valor o -1 para terminar "))
    lista = []
    if ingresa != -1:
        while ingresa != -1:
            lista.append(ingresa)
            ingresa = int(input("Ingrese otro valor o -1 para terminar "))
    else:
        lista = print("El usuario no ingreso ningun valor")
    return lista

#reemplazar elemento
def reemplazar_el(lista):
    pos = int(input("¿Que posición desea reemplazar? "))
    largo = len(lista) - 1
    while pos < 0 or pos > largo:
        pos = int(input("Ingrese una valor válido "))
    print("el valor que será reemplazado es ", lista[pos])
    valor = int(input("Ingrese el valor que desea reemplazar en dicha posición "))
    lista[pos] = valor
    return lista
    
    
#programa principal
a = cargar_lista()
print("La lista generada es:")
print(a)
b = reemplazar_el(a)
print("La nueva lista es:")
print(b)
        
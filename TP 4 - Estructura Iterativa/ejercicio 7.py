contador = 0
suma = 0
mayor = 0
posicion = 0

while contador < 10:
    entero = int(input("ingrese un numero"))  
    if entero > mayor:
        mayor = entero
        posicion = contador + 1
    suma = entero + suma
    promedio = suma / 10
    contador = contador +1
     
print("promedio = ", promedio, "mayor = ", mayor, "posicion = ", posicion)
  
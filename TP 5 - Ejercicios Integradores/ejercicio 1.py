edad = int(input("Ingrese la edad de la persona"))
contadorMayores = 0
contadorMenores = 0
edadMayores = 0
edadMenores = 0

while edad != -1:
    if edad >= 0 and edad < 18:
        contadorMenores = contadorMenores + 1
        edadMenores = edad + edadMenores
        edad = int(input("Ingrese la edad de la persona"))
    else:
        if edad >= 18 and edad <= 100:
            contadorMayores = contadorMayores + 1
            edadMayores = edad + edadMayores
            edad = int(input("Ingrese la edad de la persona"))
        else:
            print("Has ingresado una edad inválida")
            edad = int(input("Ingrese la edad correcta"))
            
promedioMayores = edadMayores // contadorMayores
promedioMenores = edadMenores // contadorMenores

print("Menores de 18 =", contadorMenores, "Mayores de 18 =", contadorMayores, "Promedio de edad de menores =", promedioMenores,
      "Promedio de edad de mayores =", promedioMayores)
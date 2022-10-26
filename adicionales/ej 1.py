edad1 = int(input("Ingrese la edad del primer hermano"))
edad2 = int(input("Ingrese la edad del segundo hermano"))

if edad1 >= 0 and edad2 >= 0:
    if edad1 > edad2:
        print("El primer hermano es mayor que el segundo")
    elif edad1 < edad2:
        print("El segundo hermano es mayor que el primero")
    elif edad1 == edad2:
        print("Los hermanos son mellizos")
else:
    print("Algo salio mal")
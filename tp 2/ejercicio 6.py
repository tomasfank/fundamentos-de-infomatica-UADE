viajeMin = float(50)
km = float(input("cuantos km hizo el taxi? = "))

if km > 0 and km <= 10:
    print("El viaje cuesta = $", (viajeMin + (20 * km)))
else:
    if km > 10:
        print("El viaje cuesta = $", (viajeMin + (15 * km)))
           
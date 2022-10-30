""" Una remiseria requiere un programa que calcule el precio de un viaje a partir de la cantidad
de kilometros que desea recorrer el usuario. Para eso cuenta con la siguiente tarifa:
    - Viaje mínimo = $150
    - Si recorre entre 0km y 10km = $20 por km
    - Si recorre 10km o más = $15 por km
"""

viajeMin = float(150)
km = float(input("cuantos km hizo el taxi? = "))

if km > 0 and km <= 10:
    print("El viaje cuesta = $", (viajeMin + (20 * km)))
else:
    if km > 10:
        print("El viaje cuesta = $", (viajeMin + (15 * km)))
           
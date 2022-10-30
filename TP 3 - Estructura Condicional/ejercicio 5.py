""" Una editorial determina el precio de un libro según la cantidad de páginas que contiene.
El costo básico del libro es de $500, más $3,20 por página con encuadernación rústica. Si el
número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo
en $200. Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento
especial de encuadernación que incrementa el costo en otros $336. Desarrollar un programa que
calcule el costo de un libro dado el número de páginas """

costoBasico = float(500)
costoPag = float(20.20)
costoTela = float(700)
costoEsp = float(1036)

cantidadPag = int(input("¿Cuantas páginas tiene el libro? = "))

if cantidadPag < 300:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoBasico))
elif cantidadPag > 300 and cantidadPag < 600:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoTela))
elif cantidadPag > 600:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoEsp))
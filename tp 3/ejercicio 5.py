costoBasico = float(500)
costoPag = float(20.20)
costoTela = float(700)
costoEsp = float(836)

cantidadPag = int(input("¿Cuantas páginas tiene el libro? = "))

if cantidadPag < 300:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoBasico))
elif cantidadPag > 300 and cantidadPag < 600:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoTela))
elif cantidadPag > 600:
    print("El libro cuesta $", ((cantidadPag * costoPag) + costoEsp))
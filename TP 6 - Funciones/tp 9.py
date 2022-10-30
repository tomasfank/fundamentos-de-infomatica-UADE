""" Escribir una función que reciba como parámetros un número de día, un número de mes
y un número de año y devuelva la cantidad de días que faltan hasta fin de mes. Luego desarrollar
tres programas para:
    - Ingresar una fecha formada por tres enteros (días, mes y año) e imprimir la cantidad
    de días que faltan para fin de año.
    - Ingresar una fecha fomrada por tres enteros (día, mes y año) e imprimir la cantidad
    de días transcurridos en ese año hasta la fecha.
    - Ingresar dos fechas formadas por tres enteros (día, mes y año) e imprimir cuanto tiempo
    transcurrió entre ambas, expresando el resultado en años, meses y días.
Los tres programas deben realizar su trabajo a través de la funcion indicada al comienzo """

def fecha(x, y, z):
    if z % 100 == 0 or z % 400 == 0 or z % 4 != 0: #Año NO bisiesto
        if y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12:
            
    elif z % 4 == 0: #Año bisiesto
            
    
""" Crear un programa que pida un número de mes (por ejemplo 4) y escriba el nombre del mes
en letras ("abril"). Verificar que el mes sea válido y mostrar un mensaje de "error" en caso
de que no lo sea """

mes = int(input("Ingresa un número del 1 al 12 = "))

if mes == 1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("Vuelve a ejecutar el programa e ingresa un valor válido")
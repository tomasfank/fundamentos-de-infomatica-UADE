numero = int(input("ingrese un valor"))
cant = 2
band = 0

while band == 0 and cant < numero:
    if numero % cant == 0:
        band = 1
    else:
        cant = cant + 1
if band == 0:
    print("el numero ", numero, " es primo")
else:
    print("el numero ", numero, " no es primo")
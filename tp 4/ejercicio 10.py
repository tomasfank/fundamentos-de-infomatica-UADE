numero = int(input("ingrese un numero"))
a = 1
t = 1

if numero > 0:
    while a <= numero:
        t = t * a
        a = a + 1
    print("el factorial de ", numero, "es", t)
else:
    print("el numero no es mayor que 0") 
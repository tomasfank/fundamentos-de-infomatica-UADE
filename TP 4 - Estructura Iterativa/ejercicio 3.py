#Ejercicio 3
numero = int(input("Ingrese un número = "))

if numero == -1:
    print("no se ingresaron valores")
else:
    mayor = numero
    menor = numero
    while numero != -1:
        if numero > mayor:
            mayor = numero
        else:
            if menor < numero:
                menor = numero
        numero = int(input("Ingrese un número = "))
        
print("Mayor =", mayor, "Menor =", menor)
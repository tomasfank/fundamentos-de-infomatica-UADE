contador = 0
sumaPares = 0

while sumaPares <= 100:
    num = int(input("ingrese un numero = "))
    contador = contador + 1
    if num % 2 == 0:
        sumaPares = sumaPares + num

print("Se ingresaron un total de ", contador, " numeros")
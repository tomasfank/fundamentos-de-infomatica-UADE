num1 = 42
num2 = 176
contador = num1
suma = 0

while contador < num2:
    contador = contador + 1
    if contador % 2 != 0:
        suma = suma + contador
        print("suma =", suma)
print("total =", suma)
numero = int(input("ingrese un numero"))
N = numero
contador = 0

while numero > 0:
    op = numero // 10
    contador = contador + 1
    numero = op
    
print("El número", N, "tiene", contador, "números")
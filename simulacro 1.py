numero = int(input("Ingrese un valor = "))
nrot = numero
cant = 0

if numero < 0:
    numero = numero * (-1)
    
while numero > 0:
    div = numero // 10
    cant = cant + 1
    numero = div
print("el numero", nrot, "tiene", cant, "digitos")
    

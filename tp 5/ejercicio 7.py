numero = int(input("Ingrese un número"))
copiaNumero = numero
revesNumero = 0

while numero > 0:
    op = numero % 10
    revesNumero = revesNumero * 10 + op
    numero = numero // 10
    
print("Al derecho", copiaNumero, "Al revés", revesNumero)
def leer_vendedor(max):
    n = int(input("numero de vendedor"))
    while (n != -1 and (n<1 or n>max)):
        print("***vendedor invalido***")
        n = int(input("ingrese numero de vendedor valido"))
    return n

VENDEDORES = 50
ventas = []

for i in range(VENDEDORES+1):
    ventas.append(0)
    
vendedor = leer_vendedor(VENDEDORES)

while vendedor != -1:
    importe = int(input("importe de la venta"))
    ventas[vendedor] = ventas[vendedor]+importe
    vendedor = leer_vendedor(VENDEDORES)
    
for i in range(1, VENDEDORES+1):
    print("El vendedor", i, "vendio", ventas[i])
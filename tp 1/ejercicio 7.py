salario = int(100000)
comision = int(10000)
nombre = input("Nombre del vendedor ")
cantidadVentas = int(input("Cuantas ventas realizo "))
valorVentas = float(input("Valor total de ventas "))

salarioTotal = float(salario + (comision * cantidadVentas) + ((valorVentas * 5) / 100))

print("Vendedor =", nombre, "Sueldo = $", salarioTotal)
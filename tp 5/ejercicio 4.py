nroCliente = int(input("Ingrese el número de cliente"))
totalFactura = float(input("Ingrese el total de la factura"))
descuento = 0
multa = 0
dia = 0

while dia <= 10:
    dia = dia + 1
    if totalFactura * 0.02 >= 200:
        descuento = totalFactura - (totalFactura * 0.02)
    else:
        descuento = totalFactura - 200
while dia <= 20:
    dia = dia + 1
    
if dia > 20:
    if totalFactura * 0.10 >= 350:
        multa = totalFactura + (totalFactura * 0.10)
    else:
        multa = totaFactura + 350
        
print("Cliente =", nroCliente)
print("Total de la factura = $", totalFactura)
print("Pagando en los 10 primeros días = $", descuento)
print("Pagando en los siguientes 10 días = $", totalFactura)
print("Pagando pasado los 20 días = $", multa)

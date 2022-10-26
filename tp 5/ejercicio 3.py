precioBase = float(input("Ingrese el precio del producto"))
cantidad = int(input("Ingrese la cantidad a comprar"))
cantidadAcumulada = 0

if cantidad == -1:
    print("El cantidad ingresada no es válida")
    else:
        while cantidad != -1:
            #Precio base x 12 productos
            if cantidad > 0 and cantidad <= 12:
                precio = precioBase
                cantidadAcumulada = cantidadAcumulada + cantidad 
            else:
                #Precio con 10% de descuento de 13 hasta 100 productos
                if cantidad > 12 and cantidad <= 100:
                    precio = ((precioBase * 12) + ((cantidad - 12) * (precioBase * 0.1)))
                    cantidadAcumulada = cantidadAcumulada + cantidad 
                else:
                    #Precio con 25% de descuento más de 100 productos
                    if cantidad > 100:
                        precio = ((precioBase * 12) + ((cantidad - 12) * (precioBase * 0.1)) + ((cantidad - 100) * (precioBase * 0.25)))
                        cantidadAcumulada = cantidadAcumulada + cantidad
                        
#Precio promedio del total de productos
precioPromedio = precio / cantidad
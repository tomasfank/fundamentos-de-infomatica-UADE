patente = int(input("ingrese el ultimo numero de la patente"))
contadorPar = 0
contadorImpar = 0

if patente == -1:
    print("No se ingreso nigun dato")
else:
    while patente != -1:
        if (patente < 10 and patente >= 0) and (patente % 2 == 0):
            contadorPar = contadorPar + 1
            patente = int(input("ingrese el ultimo numero de la patente"))
        else:
            if (patente < 10 and patente >= 0) and (patente % 2 == 1):
                contadorImpar = contadorImpar + 1
                patente = int(input("ingrese el ultimo numero de la patente"))
            else:
                print("el dato ingresado no es valido")
                patente = int(input("ingrese un numero valido"))
                
print("Patentes pares = ", contadorPar, "Patentes impares = ", contadorImpar)
                    
            
nroVisitantes = 2

while nroVisitantes != 0:
    if nroVisitantes == 2:
        nombre1= input("Ingrese el nombre del primer visitante ")
        edad1 = int(input("Ingrese su edad "))
        altura1 = float(input("Ingrese su altura "))
        if edad1 >= 15 and altura1 >= 1.5:
            mensaje1 = "puede acceder a la montaña rusa"
        else:
            mensaje1 = "NO puede acceder a la montaña rusa"
    elif nroVisitantes == 1:
        nombre2= input("Ingrese el nombre del segundo visitante ")
        edad2 = int(input("Ingrese su edad "))
        altura2 = float(input("Ingrese su altura "))
        if edad2 >= 15 and altura2 >= 1.5:
            mensaje2 = "puede acceder a la montaña rusa"
        else:
            mensaje2 = "NO puede acceder a la montaña rusa"
    nroVisitantes = nroVisitantes - 1
    
print(nombre1, mensaje1)
print(nombre2, mensaje2)

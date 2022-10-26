dia = int(input("INGRESE UN DIA = "))
mes = int(input("INGRESE UN MES = "))
año = int(input("INGRESE UN AÑO = "))
fecha = True 

if año > 0:
    if mes > 0 and mes <= 12:
        if mes == 2:
            mes = mes 
            if año % 100 == 0 or año % 400 == 0 or año % 4 != 0:
                if dia > 0 and dia <= 28:
                    dia = dia 
            elif año % 4 == 0:
                if dia > 0 and dia <= 29:
                    fecha = fecha
            else:
                fecha = not fecha
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 0 and dia <= 31:
                fecha = fecha
            else:
                fecha = not fecha
        else:
            if dia > 0 and dia <= 30:
                fecha = fecha
            else:
                fecha = not fecha
    else:
        fecha = not fecha
else:
    fecha = not fecha
    
if fecha == True:
    mensaje = "La fecha es valida"
else:
    mensaje = "La fecha es invalida"
    
print(mensaje)
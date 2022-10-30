alumno = int(input("Ingrese el legajo del alumno"))
aprobado = 0
desaprobado = 0
aplazo = 0

if alumno == -1:
    print("No se ingreso ningun número de legajo")
else:
    while alumno != -1:
        nota = float(input("ingrese la nota del alumno")) 
        if nota >= 4 and nota <= 10:
            aprobado = aprobado + 1
            alumno = int(input("Ingrese el legajo del alumno"))
        else:
            if nota > 1 and nota < 4:
                desaprobado = desaprobado + 1
                alumno = int(input("Ingrese el legajo del alumno"))
            else:
                if nota == 1:
                    aplazo = aplazo + 1
                    alumno = int(input("Ingrese el legajo del alumno"))
                else:
                    print("La nota ingresada no es válida")
                    alumno = int(input("Ingrese el legajo del alumno"))
                
totalAlumnos = aprobado + desaprobado + aplazo                
promedioAplazos = (aplazo * 100) / totalAlumnos

print("-Total de alumnos", totalAlumnos, "-Aprobados =", aprobado, "-Desaprobados =", desaprobado, "-Porcentaje de aplazos =", promedioAplazos)

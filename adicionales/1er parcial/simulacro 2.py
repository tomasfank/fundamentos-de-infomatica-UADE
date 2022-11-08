"""
Ejercicio 2: 
Se ingresa por teclado el numero de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en la variable del legajo.
Se debe validar que la nota ingresada sea entre 1 y 10.
Se debe informar:
a) Cantidad de alumnos con nota >= 7
b) Cantidad de alumnos con nota >= 4 y < 7
c) Porcentaje de alumnos aplazados.
d) cantidad total de alumnos.
e) la nota mas alta.
"""

legajo = int(input("Ingrese el legajo del alumno = "))
cantAlumnos = 0
nota7 = 0
nota4 = 0
notaInt = 0
porcAplazos = 0
notaAlta = 0

if legajo == -1:
    print("No se ingreso ningun legajo")
else:
    while legajo != -1:
        nota = int(input("Ingrese la nota del alumno"))
        if nota > notaAlta:
            notaAlta = nota
        #Alumnos promocionados
        if nota >= 7 and nota <= 10:
            cantAlumnos = cantAlumnos + 1
            nota7 = nota7 + 1
            legajo = int(input("Ingrese el legajo del alumno = "))
        else:
            #Alumnos aprobados
            if nota < 7 and nota >= 4:
                cantAlumnos = cantAlumnos + 1
                nota4 = nota4 + 1
                legajo = int(input("Ingrese el legajo del alumno = "))
            else:
                #Alumnos aplazados
                if nota < 4 and nota > 0:
                    cantAlumnos = cantAlumnos + 1
                    notaInt = notaInt + 1 
                    legajo = int(input("Ingrese el legajo del alumno = "))
                else:
                    print("La nota ingresada no es valida")
                    legajo = int(input("Ingrese el legajo del alumno = "))
                
#Porcentaje de aplazos                
porcAplazos = ((notaInt * 100) / cantAlumnos)

print("Total de alumnos =", cantAlumnos, "Alumnos promocionados =", nota7, "Alumnos aprobados =", nota4,
      "Porcentaje de alumnos aplazados = %",porcAplazos, "Nota más alta =", notaAlta) 
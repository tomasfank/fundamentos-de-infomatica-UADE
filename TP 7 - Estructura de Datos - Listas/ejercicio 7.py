""" Una escuela necesita conocer cuántos alumnos cumplen años cada mes del
año con el propósito de ofrecerles un agasajo especial en su día.
Desarrollar un programa que lea el número de legajo y fecha de nacimiento
(día, mes, año) de cada uno de los alumnos que concurren a dicha escuela.
La carga finaliza con un número de legajo "-1". Emitir un informe donde
aparezca -mes por mes- cúantos alumnos cumplen años a lo largo del año.
Imprimir también una leyenda que indique cúal es el mes con mayor cantidad
de cumpleaños. """

def legajo():
    nro = int(input("Ingrese el número de legajo del alumno"))
    while nro != -1:
        alumnos.append(nro)
        nro = int(input("Ingrese el número de legajo del alumno"))
   

MESES = 12
alumnos = []

    

a = legajo()
print(a) 
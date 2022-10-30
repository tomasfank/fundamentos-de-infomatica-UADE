""" Ingresar las notas de los dos parciaes de un alumno e indicar si promocionó, aprobó o si
debe recuperar. Informar un error si el valor de alguna nota no está entre 0 y 10
    - Se promociona cuando las notas de ambos parciales son mayores o iguales a 7
    - Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4
    - Se debe recuperar cuando al menos una de lass dos notas es menor a 4
"""

nota1 = float(input("Ingrese nota del primer parcial (del 1 al 10)= "))
nota2 = float(input("Ingrese nota del segundo parcial (del 1 al 10)= "))

if (nota1 >= 0) and (nota1 <= 10) and (nota2 >= 0) and (nota2 <= 10):
    if (nota1 >= 7) and (nota2 >= 7):
        print("El alumno promociona la materia")
    elif (nota1 >= 4) and (nota2 >= 4):
        print("El alumno va a final")
    else:
        print("El alumno debe recuperar un parcial")
else:
    print("Las notas ingresadas no son válidas") 
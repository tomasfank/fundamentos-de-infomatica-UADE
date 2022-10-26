nota1 = float(input("Ingrese nota del primer parcial (del 1 al 10)= "))
nota2 = float(input("Ingrese nota del segundo parcial (del 1 al 10)= "))
promedio = int((nota1 + nota2) / 2)
print("El promedio es = ",promedio)

if promedio >= 7 and promedio <= 10:
    print("El alumno promociona la materia")
elif promedio >= 4 and promedio <= 6:
    print("El alumno va a final")
elif promedio > 10 or promedio < 0:
    print("Alguna nota esta mal, repita el programa")
else:
    print("el alumno no aprueba la materia")
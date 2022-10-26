pregunta1 = input("2 + 2 = 5?")
pregunta2 = input("La capital de alemania  es Berlin?")
pregunta3 = input("El caballo blanco de San Martin. Era de color negro?")

if pregunta1 == "si" or pregunta1 == "SI" or pregunta1 == "Si" or pregunta1 == "sI":
    respuesta1 = "correcta"
else:
    respuesta1 = "incorrecta"
    
if pregunta2 == "si" or pregunta2 == "SI" or pregunta2 == "Si" or pregunta2 == "sI":
    respuesta2 = "correcta"
else:
    respuesta2 = "incorrecta"
    
if pregunta3 == "si" or pregunta3 == "SI" or pregunta3 == "Si" or pregunta3 == "sI":
    respuesta3 = "correcta"
else:
    respuesta3 = "incorrecta"

print("respuesta 1 =", respuesta1)
print("respuesta 2 =", respuesta2)
print("respuesta 3 =", respuesta3)
edad = int(input("Ingrese su edad"))
booleana = True

if edad >= 0 and edad < 18:
    booleana = not booleana
elif edad >= 18:
    booleana = booleana
else:
    print("Algo salio mal")

print("La persona es mayor de edad?")
print(booleana)
año = int(input("ingrese el año = "))

if año % 100 == 0 or año % 400 == 0 or año % 4 != 0:
    print("No es año bisiesto")
else:
    if año % 4 == 0:
        print("Es año bisiesto")
        
"""
Una fábrica produce bicicletas de montaña. Para construir una bicicleta de montaña se 
necesitan 1.5 kg de acero.
La fábrica vende las bicicletas de montaña a $36.000.
Se pide: 
Considerando que la cantidad de acero disponible en la fábrica por mes se ingresa por 
teclado,
informar la cantidad máxima de bicicletas de montaña que podrá producir la fábrica con 
ese acero.
Si no se llega a producir al menos 50 bicicletas en total, informarlo por pantalla
e indicar cuantas bicicletas de montaña faltarían para cumplir con el objetivo de 
ventas del mes.
Validar que la cantidad de acero disponible para la producción sea mayor a 0.
"""
cantidadAcero = float(input("Cuanto acero posee la fabrica?"))
aceroBici = 1.5
produccionMin = 50

while cantidadAcero <= 0:
    cantidadAcero = float(input("Error! Ingrese una cantidad válida mayor a 0"))
    
produccion = cantidadAcero // aceroBici

if produccion < produccionMin:
    faltante = produccionMin - produccion
    print("La cantidad de acero dispoible es", cantidadAcero)
    print("La cantidad máxima de bicicletas que se prodrá producir es", produccion)
    print("Para cubrir la produccion minima faltan fabricar", faltante, "bicibletas")
else:
    print("La cantidad de acero dispoible es", cantidadAcero)
    print("La cantidad máxima de bicicletas que se prodrá producir es", produccion)

    
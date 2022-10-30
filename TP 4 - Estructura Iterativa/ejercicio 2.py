#ejercicio 2
#para resolver este ejercicio debemos crear un "switch on/off" 
par = False 
num = 0

while num != -1:
    num = int(input("ingrese un número = "))
    par = not par
  
if par == True:
    print("La cantidad ingresada es par")
else:
    print("La cantidad ingresada es impar") 
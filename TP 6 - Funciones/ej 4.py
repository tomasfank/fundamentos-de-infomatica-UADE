""" Devolver True si el número entero recibido como primer parámetro es multiplo del segundo
o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3)
devuelve False """

num1 = int(input("Ingrese el primer número"))
num2 = int(input("Ingrese el segundo número"))

def multiplo(a, b):
    return a % b == 0 

resultado = multiplo(num1, num2)
print(resultado)
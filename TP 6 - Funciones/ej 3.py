""" Imprimir una columna de asteriscos, donde su altura se recibe como parámetro"""

def altura(a):
    n = 0
    while n < a:
        print("*")
        n = n + 1
    
ingreseAltura = int(input("Ingrese una altura"))
h = altura(ingreseAltura)
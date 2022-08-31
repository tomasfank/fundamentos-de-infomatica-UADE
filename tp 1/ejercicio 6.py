medida = float(input("Ingrese una medida en metros "))

centimetros = float(medida * 100)
pulgadas = float(centimetros / 2.54)
pies = float(pulgadas / 12)
yardas = float(pies / 3)

print("centimetros =", centimetros)
print("pulgadas =", pulgadas)
print("pies =", pies)
print("yardas =", yardas)
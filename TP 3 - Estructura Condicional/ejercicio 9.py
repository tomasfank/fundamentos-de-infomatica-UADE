""" Diseñar un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo
básico y si antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto
por cada año de antigüedad, mientras que si es casado se le incrementa en 7%. También se le
realizan los siguientes descuentos:
    - Jubilación: 11%
    - Obra social: 3%
    - Sindicato: 3%
"""

sueldoBasico = float(input("ingrese el sueldo bruto"))
antiguedad = int(input("Cuantos años lleva en la empresa?"))
estadoCivil = input("estado civil (¿S o C?)")

if estadoCivil == "S" or estadoCivil == "s":
    sueldoBruto = float((((5 * antiguedad) * sueldoBasico) / 100) + sueldoBasico)
    jubilacion = ((sueldoBruto * 11) / 100)
    obraSocial = ((sueldoBruto * 3) / 100)
    sindicato = ((sueldoBruto * 3) / 100)
    sueldoNeto = (sueldoBruto - jubilacion - obraSocial - sindicato)
    print("Sueldo báscio = $", sueldoBasico)
    print("Antigüedad =", antiguedad, "años")
    print("Estado civil = Soltero")
    print("Sueldo bruto = $", sueldoBruto)
    print("Jubilacion 11% = $", jubilacion)
    print("Obra Social 3% = $", obraSocial)
    print("Sindicato 3% = $", sindicato)
    print("Sueldo Neto = $", sueldoNeto)
else:
    if estadoCivil == "C" or estadoCivil == "c":
        sueldoBruto = float((((7 * antiguedad) * sueldoBasico) / 100) + sueldoBasico)
        jubilacion = ((sueldoBruto * 11) / 100)
        obraSocial = ((sueldoBruto * 3) / 100)
        sindicato = ((sueldoBruto * 3) / 100)
        sueldoNeto = (sueldoBruto - jubilacion - obraSocial - sindicato)
        print("Sueldo báscio = $", sueldoBasico)
        print("Antigüedad =", antiguedad, "años")
        print("Estado civil = Soltero")
        print("Sueldo bruto = $", sueldoBruto)
        print("Jubilacion 11% = $", jubilacion)
        print("Obra Social 3% = $", obraSocial)
        print("Sindicato 3% = $", sindicato)
        print("Sueldo Neto = $", sueldoNeto)
        
[33mcommit d20a43a1710b03d0c7130d29ca00260c4735038d[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m)[m
Author: tomasfank <tomasfank@outlook.com>
Date:   Wed Aug 31 16:46:54 2022 -0300

    TP1y2

[1mdiff --git a/tp 1/ejercicio 1.py b/tp 1/ejercicio 1.py[m
[1mnew file mode 100644[m
[1mindex 0000000..c5510b9[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 1.py[m	
[36m@@ -0,0 +1,27 @@[m
[32m+[m[32m#ejercicio 1[m
[32m+[m[32m#a[m
[32m+[m[32mprint("hola mundo")[m
[32m+[m
[32m+[m[32m#b[m
[32m+[m[32mnombre = input("ingrese su nombre ")[m
[32m+[m[32mprint("Hola", nombre,"!")[m
[32m+[m
[32m+[m[32m#c[m
[32m+[m[32mnum1 = int(input("Ingrese un número "))[m
[32m+[m[32mnum2 = input("Ingrese otro número ")[m
[32m+[m[32mnum3 = int(num2)[m
[32m+[m[32moperacion = print("El resultado de la suma es =",num1 + num3,"La diferencia es =", num1 - num3)[m
[32m+[m
[32m+[m[32m#d[m
[32m+[m[32mnum1 = int(input("Ingrese un número "))[m
[32m+[m[32mnum2 = int(input("Ingrese otro número "))[m
[32m+[m[32moperación = print("El resultado de la suma es =", num1 + num2, "El promedio entre estos números es =", ((num1 + num2) / 2))[m
[32m+[m
[32m+[m[32m#e[m
[32m+[m[32mfactura = int(input("Ingrese el monto de la factura "))[m
[32m+[m[32miva = int((factura * 21) / 100)[m
[32m+[m[32mprecioMasIva = int(factura + iva)[m
[32m+[m[32mtotal = print("El IVA es de =", iva, "El precio total es de =", precioMasIva)[m
[32m+[m
[32m+[m
[32m+[m[41m              [m
\ No newline at end of file[m
[1mdiff --git a/tp 1/ejercicio 2.py b/tp 1/ejercicio 2.py[m
[1mnew file mode 100644[m
[1mindex 0000000..79b5413[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 2.py[m	
[36m@@ -0,0 +1,45 @@[m
[32m+[m[32m#ejercicio 2[m
[32m+[m[32m#a[m
[32m+[m[32moperacionA = 12 * 4 + 4 * 5[m
[32m+[m[32mprint('El resultado de A es =', operacionA)[m
[32m+[m
[32m+[m[32m#b[m
[32m+[m[32moperacionB = 12 * (4 + 4) * 5[m
[32m+[m[32mprint('El resultado de B es =', operacionB)[m
[32m+[m
[32m+[m[32m#c[m
[32m+[m[32moperacionC = 5 * 4 / 2[m
[32m+[m[32mprint('El resultado de C es =', operacionC)[m
[32m+[m
[32m+[m[32m#d[m
[32m+[m[32moperacionD = 5 * (4 / 2)[m
[32m+[m[32mprint('El resultado de D es =', operacionD)[m
[32m+[m
[32m+[m[32m#e[m
[32m+[m[32moperacionE = 24 / 2 ** 2[m
[32m+[m[32mprint('El resultado de E es =', operacionE)[m
[32m+[m
[32m+[m[32m#f[m
[32m+[m[32moperacionF = (24 / 2) ** 2[m
[32m+[m[32mprint('El resultado de F es =', operacionF)[m
[32m+[m
[32m+[m[32m#g[m
[32m+[m[32moperacionG = -9 ** 2[m
[32m+[m[32mprint('El resultado de G es =', operacionG)[m
[32m+[m
[32m+[m[32m#h[m
[32m+[m[32moperacionH = (-9) ** 2[m
[32m+[m[32mprint('El resultado de H es =', operacionH)[m
[32m+[m
[32m+[m[32m#i[m
[32m+[m[32moperacionI = 10 / 3[m
[32m+[m[32mprint('El resultado de I es =', operacionI)[m
[32m+[m
[32m+[m[32m#j[m
[32m+[m[32moperacionJ = 10 // 3[m
[32m+[m[32mprint('El resultado de J es =', operacionJ)[m
[32m+[m
[32m+[m[32m#k[m
[32m+[m[32moperacionK = 12 % 5[m
[32m+[m[32mprint('El resultado de K es =', operacionK)[m
[32m+[m
[1mdiff --git a/tp 1/ejercicio 3.py b/tp 1/ejercicio 3.py[m
[1mnew file mode 100644[m
[1mindex 0000000..1c7737c[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 3.py[m	
[36m@@ -0,0 +1,14 @@[m
[32m+[m[32m#Primer parcial[m
[32m+[m[32mprimerParcial = float(input("Nota del primer parcial ="))[m
[32m+[m[32m#Imprimo en la consola la entrada del primer parcial[m
[32m+[m[32mprint("La nota del primer parcial es =", primerParcial)[m
[32m+[m
[32m+[m[32m#Segundo parcial[m
[32m+[m[32msegundoParcial = float(input("Nota del segundo parcial ="))[m
[32m+[m[32m#Imprimo la entrada del segundo parcial[m
[32m+[m[32mprint("La nota del segundo parcial es =", segundoParcial)[m
[32m+[m
[32m+[m[32m#Calculo de promedio redondeado[m
[32m+[m[32mpromedio = (primerParcial + segundoParcial) // 2[m
[32m+[m[32m#Devuelvo el promedio calculado[m
[32m+[m[32mprint("El promedio del alumno es =", promedio)[m
\ No newline at end of file[m
[1mdiff --git a/tp 1/ejercicio 4.py b/tp 1/ejercicio 4.py[m
[1mnew file mode 100644[m
[1mindex 0000000..c86c75b[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 4.py[m	
[36m@@ -0,0 +1,22 @@[m
[32m+[m[32m#cantidad de dinero del 1er inversor[m
[32m+[m[32mprimerInversor = 8000[m
[32m+[m[32m#cantidad de dinero del 2do inversor[m
[32m+[m[32msegundoInversor = 6000[m
[32m+[m[32m#cantidad de dinero del 3er inveror[m
[32m+[m[32mtercerInversor = 2000[m
[32m+[m
[32m+[m[32m#fondo total de la inversion[m
[32m+[m[32minversionTotal = primerInversor + segundoInversor + tercerInversor[m
[32m+[m[32mprint('La inversion es de = $', inversionTotal)[m
[32m+[m
[32m+[m[32m#Porcentaje del 1er inversor[m
[32m+[m[32mporcentajePrimerInversor = (primerInversor * 100) / inversionTotal[m
[32m+[m
[32m+[m[32m#Porcentaje del 2do inversor[m
[32m+[m[32mporcentajeSegundoInversor = (segundoInversor * 100) / inversionTotal[m
[32m+[m
[32m+[m[32m#Porcentaje del 3er inversor[m
[32m+[m[32mporcentajeTercerInversor = (tercerInversor * 100) / inversionTotal[m
[32m+[m
[32m+[m[32m#imprimimos los resultados[m
[32m+[m[32mprint('El primer inversor aporta un %', porcentajePrimerInversor, '. El segundo inversor aporta un %', porcentajeSegundoInversor, '. El tercer inversor aporta un %', porcentajeTercerInversor)[m
[1mdiff --git a/tp 1/ejercicio 5.py b/tp 1/ejercicio 5.py[m
[1mnew file mode 100644[m
[1mindex 0000000..6c25e46[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 5.py[m	
[36m@@ -0,0 +1,26 @@[m
[32m+[m[32m#Preguntamos cuato dinero quiere invertir la persona[m
[32m+[m[32minversion = float(input('¿Cuanto dinero quiere invertir? '))[m
[32m+[m
[32m+[m[32m#primer mes[m
[32m+[m[32mprimerMes = ((inversion * 2) / 100) + inversion[m
[32m+[m[32mprint('El primer mes acumula $', primerMes)[m
[32m+[m
[32m+[m[32m#segundo mes[m
[32m+[m[32msegundoMes = ((primerMes * 2) / 100) + primerMes[m
[32m+[m[32mprint('El segundo mes acumula $', segundoMes)[m
[32m+[m
[32m+[m[32m#tercer mes[m
[32m+[m[32mtercerMes = ((segundoMes * 2) / 100) + segundoMes[m
[32m+[m[32mprint('El tercer mes acumula $', tercerMes)[m
[32m+[m
[32m+[m[32m#cuatro mes[m
[32m+[m[32mcuartoMes = ((tercerMes * 2) / 100) + tercerMes[m
[32m+[m[32mprint('El cuarto mes acumula $', cuartoMes)[m
[32m+[m
[32m+[m[32m#quinto mes[m
[32m+[m[32mquintoMes = ((cuartoMes * 2) / 100) + cuartoMes[m
[32m+[m[32mprint('El quinto mes acumula $', quintoMes)[m
[32m+[m
[32m+[m[32m#sexto mes[m
[32m+[m[32msextoMes = ((quintoMes * 2) / 100) + quintoMes[m
[32m+[m[32mprint('El sexto mes acumula $', sextoMes)[m
\ No newline at end of file[m
[1mdiff --git a/tp 1/ejercicio 6.py b/tp 1/ejercicio 6.py[m
[1mnew file mode 100644[m
[1mindex 0000000..592979b[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 6.py[m	
[36m@@ -0,0 +1,11 @@[m
[32m+[m[32mmedida = float(input("Ingrese una medida en metros "))[m
[32m+[m
[32m+[m[32mcentimetros = float(medida * 100)[m
[32m+[m[32mpulgadas = float(centimetros / 2.54)[m
[32m+[m[32mpies = float(pulgadas / 12)[m
[32m+[m[32myardas = float(pies / 3)[m
[32m+[m
[32m+[m[32mprint("centimetros =", centimetros)[m
[32m+[m[32mprint("pulgadas =", pulgadas)[m
[32m+[m[32mprint("pies =", pies)[m
[32m+[m[32mprint("yardas =", yardas)[m
\ No newline at end of file[m
[1mdiff --git a/tp 1/ejercicio 7.py b/tp 1/ejercicio 7.py[m
[1mnew file mode 100644[m
[1mindex 0000000..ac71e2f[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 7.py[m	
[36m@@ -0,0 +1,9 @@[m
[32m+[m[32msalario = int(100000)[m
[32m+[m[32mcomision = int(10000)[m
[32m+[m[32mnombre = input("Nombre del vendedor ")[m
[32m+[m[32mcantidadVentas = int(input("Cuantas ventas realizo "))[m
[32m+[m[32mvalorVentas = float(input("Valor total de ventas "))[m
[32m+[m
[32m+[m[32msalarioTotal = float(salario + (comision * cantidadVentas) + ((valorVentas * 5) / 100))[m
[32m+[m
[32m+[m[32mprint("Vendedor =", nombre, "Sueldo = $", salarioTotal)[m
\ No newline at end of file[m
[1mdiff --git a/tp 1/ejercicio 8.py b/tp 1/ejercicio 8.py[m
[1mnew file mode 100644[m
[1mindex 0000000..c90656a[m
[1m--- /dev/null[m
[1m+++ b/tp 1/ejercicio 8.py[m	
[36m@@ -0,0 +1 @@[m
[32m+[m[32mretira = int(input("cuanto dinero quiere retirar?")[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 1.py b/tp 2/ejercicio 1.py[m
[1mnew file mode 100644[m
[1mindex 0000000..b7b5603[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 1.py[m	
[36m@@ -0,0 +1,9 @@[m
[32m+[m[32m#variables enteras[m
[32m+[m[32mn1 = int(input("ingrese un número entero"))[m
[32m+[m[32mn2 = int(input("ingrese otro número entero"))[m
[32m+[m[32m#condición[m[41m [m
[32m+[m[32mif n1 == n2:[m
[32m+[m[32m    print("Los números son iguales")[m
[32m+[m[32m#en caso de no cumplirse la condición[m[41m [m
[32m+[m[32melse:[m
[32m+[m[32m    print("Los números son distintos")[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 2.py b/tp 2/ejercicio 2.py[m
[1mnew file mode 100644[m
[1mindex 0000000..2fe0a83[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 2.py[m	
[36m@@ -0,0 +1,6 @@[m
[32m+[m[32mn = int(input("ingrese un número entero"))[m
[32m+[m
[32m+[m[32mif n % 2 == 0:[m
[32m+[m[32m    print("el número es par")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("el número es impar")[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 3.py b/tp 2/ejercicio 3.py[m
[1mnew file mode 100644[m
[1mindex 0000000..d247a3b[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 3.py[m	
[36m@@ -0,0 +1,28 @@[m
[32m+[m[32mmes = int(input("Ingresa un número del 1 al 12 = "))[m
[32m+[m
[32m+[m[32mif mes == 1:[m
[32m+[m[32m    print("Enero")[m
[32m+[m[32melif mes == 2:[m
[32m+[m[32m    print("Febrero")[m
[32m+[m[32melif mes == 3:[m
[32m+[m[32m    print("Marzo")[m
[32m+[m[32melif mes == 4:[m
[32m+[m[32m    print("Abril")[m
[32m+[m[32melif mes == 5:[m
[32m+[m[32m    print("Mayo")[m
[32m+[m[32melif mes == 6:[m
[32m+[m[32m    print("Junio")[m
[32m+[m[32melif mes == 7:[m
[32m+[m[32m    print("Julio")[m
[32m+[m[32melif mes == 8:[m
[32m+[m[32m    print("Agosto")[m
[32m+[m[32melif mes == 9:[m
[32m+[m[32m    print("Septiembre")[m
[32m+[m[32melif mes == 10:[m
[32m+[m[32m    print("Octubre")[m
[32m+[m[32melif mes == 11:[m
[32m+[m[32m    print("Noviembre")[m
[32m+[m[32melif mes == 12:[m
[32m+[m[32m    print("Diciembre")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("Vuelve a ejecutar el programa e ingresa un valor válido")[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 4.py b/tp 2/ejercicio 4.py[m
[1mnew file mode 100644[m
[1mindex 0000000..b044eb4[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 4.py[m	
[36m@@ -0,0 +1,13 @@[m
[32m+[m[32mnota1 = float(input("Ingrese nota del primer parcial (del 1 al 10)= "))[m
[32m+[m[32mnota2 = float(input("Ingrese nota del segundo parcial (del 1 al 10)= "))[m
[32m+[m[32mpromedio = int((nota1 + nota2) / 2)[m
[32m+[m[32mprint("El promedio es = ",promedio)[m
[32m+[m
[32m+[m[32mif promedio >= 7 and promedio <= 10:[m
[32m+[m[32m    print("El alumno promociona la materia")[m
[32m+[m[32melif promedio >= 4 and promedio <= 6:[m
[32m+[m[32m    print("El alumno va a final")[m
[32m+[m[32melif promedio > 10 or promedio < 0:[m
[32m+[m[32m    print("Alguna nota esta mal, repita el programa")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("el alumno no aprueba la materia")[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 5.py b/tp 2/ejercicio 5.py[m
[1mnew file mode 100644[m
[1mindex 0000000..5cd1d9b[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 5.py[m	
[36m@@ -0,0 +1,13 @@[m
[32m+[m[32mcostoBasico = float(500)[m
[32m+[m[32mcostoPag = float(20.20)[m
[32m+[m[32mcostoTela = float(700)[m
[32m+[m[32mcostoEsp = float(836)[m
[32m+[m
[32m+[m[32mcantidadPag = int(input("¿Cuantas páginas tiene el libro? = "))[m
[32m+[m
[32m+[m[32mif cantidadPag < 300:[m
[32m+[m[32m    print("El libro cuesta $", ((cantidadPag * costoPag) + costoBasico))[m
[32m+[m[32melif cantidadPag > 300 and cantidadPag < 600:[m
[32m+[m[32m    print("El libro cuesta $", ((cantidadPag * costoPag) + costoTela))[m
[32m+[m[32melif cantidadPag > 600:[m
[32m+[m[32m    print("El libro cuesta $", ((cantidadPag * costoPag) + costoEsp))[m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 6.py b/tp 2/ejercicio 6.py[m
[1mnew file mode 100644[m
[1mindex 0000000..c90f65b[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 6.py[m	
[36m@@ -0,0 +1,9 @@[m
[32m+[m[32mviajeMin = float(50)[m
[32m+[m[32mkm = float(input("cuantos km hizo el taxi? = "))[m
[32m+[m
[32m+[m[32mif km > 0 and km <= 10:[m
[32m+[m[32m    print("El viaje cuesta = $", (viajeMin + (20 * km)))[m
[32m+[m[32melse:[m
[32m+[m[32m    if km > 10:[m
[32m+[m[32m        print("El viaje cuesta = $", (viajeMin + (15 * km)))[m
[32m+[m[41m           [m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 7.py b/tp 2/ejercicio 7.py[m
[1mnew file mode 100644[m
[1mindex 0000000..e308c28[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 7.py[m	
[36m@@ -0,0 +1,8 @@[m
[32m+[m[32maño = int(input("ingrese el año = "))[m
[32m+[m
[32m+[m[32mif año % 100 == 0 or año % 400 == 0 or año % 4 != 0:[m
[32m+[m[32m    print("No es año bisiesto")[m
[32m+[m[32melse:[m
[32m+[m[32m    if año % 4 == 0:[m
[32m+[m[32m        print("Es año bisiesto")[m
[32m+[m[41m        [m
\ No newline at end of file[m
[1mdiff --git a/tp 2/ejercicio 8.py b/tp 2/ejercicio 8.py[m
[1mnew file mode 100644[m
[1mindex 0000000..0fdf285[m
[1m--- /dev/null[m
[1m+++ b/tp 2/ejercicio 8.py[m	
[36m@@ -0,0 +1,34 @@[m
[32m+[m[32msueldoBasico = float(input("ingrese el sueldo bruto"))[m
[32m+[m[32mantiguedad = int(input("Cuantos años lleva en la empresa?"))[m
[32m+[m[32mestadoCivil = input("estado civil (¿S o C?)")[m
[32m+[m
[32m+[m[32mif estadoCivil == "S" or estadoCivil == "s":[m
[32m+[m[32m    sueldoBruto = float((((5 * antiguedad) * sueldoBasico) / 100) + sueldoBasico)[m
[32m+[m[32m    jubilacion = ((sueldoBruto * 11) / 100)[m
[32m+[m[32m    obraSocial = ((sueldoBruto * 3) / 100)[m
[32m+[m[32m    sindicato = ((sueldoBruto * 3) / 100)[m
[32m+[m[32m    sueldoNeto = (sueldoBruto - jubilacion - obraSocial - sindicato)[m
[32m+[m[32m    print("Sueldo báscio = $", sueldoBasico)[m
[32m+[m[32m    print("Antigüedad =", antiguedad, "años")[m
[32m+[m[32m    print("Estado civil = Soltero")[m
[32m+[m[32m    print("Sueldo bruto = $", sueldoBruto)[m
[32m+[m[32m    print("Jubilacion 11% = $", jubilacion)[m
[32m+[m[32m    print("Obra Social 3% = $", obraSocial)[m
[32m+[m[32m    print("Sindicato 3% = $", sindicato)[m
[32m+[m[32m    print("Sueldo Neto = $", sueldoNeto)[m
[32m+[m[32melse:[m
[32m+[m[32m    if estadoCivil == "C" or estadoCivil == "c":[m
[32m+[m[32m        sueldoBruto = float((((7 * antiguedad) * sueldoBasico) / 100) + sueldoBasico)[m
[32m+[m[32m        jubilacion = ((sueldoBruto * 11) / 100)[m
[32m+[m[32m        obraSocial = ((sueldoBruto * 3) / 100)[m
[32m+[m[32m        sindicato = ((sueldoBruto * 3) / 100)[m
[32m+[m[32m        sueldoNeto = (sueldoBruto - jubilacion - obraSocial - sindicato)[m
[32m+[m[32m        print("Sueldo báscio = $", sueldoBasico)[m
[32m+[m[32m        print("Antigüedad =", antiguedad, "años")[m
[32m+[m[32m        print("Estado civil = Soltero")[m
[32m+[m[32m        print("Sueldo bruto = $", sueldoBruto)[m
[32m+[m[32m        print("Jubilacion 11% = $", jubilacion)[m
[32m+[m[32m        print("Obra Social 3% = $", obraSocial)[m
[32m+[m[32m        print("Sindicato 3% = $", sindicato)[m
[32m+[m[32m        print("Sueldo Neto = $", sueldoNeto)[m
[32m+[m[41m        [m
\ No newline at end of file[m

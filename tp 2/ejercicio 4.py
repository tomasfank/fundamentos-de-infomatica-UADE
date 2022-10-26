#cantidad de dinero del 1er inversor
primerInversor = 8000
#cantidad de dinero del 2do inversor
segundoInversor = 6000
#cantidad de dinero del 3er inveror
tercerInversor = 2000

#fondo total de la inversion
inversionTotal = primerInversor + segundoInversor + tercerInversor
print('La inversion es de = $', inversionTotal)

#Porcentaje del 1er inversor
porcentajePrimerInversor = (primerInversor * 100) / inversionTotal

#Porcentaje del 2do inversor
porcentajeSegundoInversor = (segundoInversor * 100) / inversionTotal

#Porcentaje del 3er inversor
porcentajeTercerInversor = (tercerInversor * 100) / inversionTotal

#imprimimos los resultados
print('El primer inversor aporta un %', porcentajePrimerInversor, '. El segundo inversor aporta un %', porcentajeSegundoInversor, '. El tercer inversor aporta un %', porcentajeTercerInversor)

#Preguntamos cuato dinero quiere invertir la persona
inversion = float(input('¿Cuanto dinero quiere invertir? '))

#primer mes
primerMes = ((inversion * 2) / 100) + inversion
print('El primer mes acumula $', primerMes)

#segundo mes
segundoMes = ((primerMes * 2) / 100) + primerMes
print('El segundo mes acumula $', segundoMes)

#tercer mes
tercerMes = ((segundoMes * 2) / 100) + segundoMes
print('El tercer mes acumula $', tercerMes)

#cuatro mes
cuartoMes = ((tercerMes * 2) / 100) + tercerMes
print('El cuarto mes acumula $', cuartoMes)

#quinto mes
quintoMes = ((cuartoMes * 2) / 100) + cuartoMes
print('El quinto mes acumula $', quintoMes)

#sexto mes
sextoMes = ((quintoMes * 2) / 100) + quintoMes
print('El sexto mes acumula $', sextoMes)
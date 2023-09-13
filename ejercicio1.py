'''
carlo morici
Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''
#solicito datos
nombre = input("ingrese su nombre; ")
sueldo = input("ingrese su sueldo ")

#casteo datos
sueldo = float(sueldo)

#calculo de resultados solicitados
sueldo_nuevo = sueldo*1.1
incremento = sueldo*0.1

#imprimo resultados
print("el aumento de su sueldo es de  " + str(incremento) + " y su nuevo sueldo es: " + str(sueldo_nuevo))
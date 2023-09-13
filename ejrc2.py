'''
carlo morici

Ejercicio 2:
Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).


'''

#solicito datos
edad = input("ingrese su edad; ")

#casteo datos
edad = int(edad)

#verifico informacion
if (edad < 13) :
    print("es un niño o niña")
elif (edad < 18) :
    print("es adolescente")
else:
    print("es mayor de edad")


#imprimo resultados
# print("el aumento de su sueldo es de  " + str(incremento) + " y su nuevo sueldo es: " + str(sueldo_nuevo))
'''
carlo morici

Ejercicio 4:
Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'

'''

#solicito datos
edad = input("ingrese su edad: ")
edad = int(edad)
repeticion = True

#while validando ingreso de datos
while (repeticion == True):
    estado = input ("ingrese su estado civil 'soltero' o 'casado': ")
    estado = estado.lower()
    if (estado != "soltero" and estado != "casado"):
        print("no ingresaste valores validos, reintenta")
    else:
        repeticion = False

if (edad < 18 and estado != "soltero"):
    print("Es muy pequeño para NO ser soltero")

#imprimo resultados
# print("el aumento de su sueldo es de  " + str(incremento) + " y su nuevo sueldo es: " + str(sueldo_nuevo))
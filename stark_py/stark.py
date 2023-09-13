'''
carlo morici

Desafio Stark

Industrias Stark es principalmente una empresa de defensa que desarrolla y fabrica
armas avanzadas y tecnologías militares.

Recientemente ha decidido ampliar su departamento de IT y para acceder a las
entrevistas es necesario completar el siguiente desafío, el cual estará dividido en
etapas. Cada semana recibiremos un nuevo pedido de parte de la empresa.

La empresa compartió con todos los participantes cierta información confidencial
de un grupo de superhéroes. Y semana a semana enviará una lista con los nuevos
requerimientos. Quien supere todas las etapas accedera a una entrevista con el
director para de la compañía.
Set de datos

La información a ser analizada se encuentra en el archivo data_stark.py, por tratarse
de una lista, bastará con incluir dicho archivo en el proyecto de la siguiente manera:

from data_stark import lista_personajes

Formato de los datos recibidos

lista_heroes =
[
{
"nombre": "Howard the Duck",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "79.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": "average"
},
{
"nombre": "Rocket Raccoon",
"identidad": "Rocket Raccoon",
"empresa": "Marvel Comics",
"altura": "122.77",
"peso": "25.73",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Brown",
"fuerza": "5",
"inteligencia": "average"
}
]


Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino

NOTA: Se debe construir un menú en el que se sea posible acceder a cada una de
las opciones (A-E)
'''

#importo data
from data_stark import lista_personajes
from menu import cadena_menu

#muestro data
#print(lista_personajes)

#bucle de menu
entrada_menu = str()
while (entrada_menu != "Z" and entrada_menu != "z"):
    entrada_menu = input("\n\n" + cadena_menu + "\n\nopcion: ")
   
   #A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
    if (entrada_menu == "a" or entrada_menu == "A"):
        print("entramos a opcion a")
        for personaje in lista_personajes:
            print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))

    #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
    elif (entrada_menu == "b" or entrada_menu == "B"):
        set_fuerza = set()
        for personaje in lista_personajes:
            set_fuerza.add(int(personaje["fuerza"]))

        print(set_fuerza)
            


    elif (entrada_menu == "z" or entrada_menu == "Z"):
        print ("nos vamos")
    else:
        print("opcion incorrecta. reintenta")









'''
entrada = input("Ingresa un número decimal (positivo o negativo): ")

validar_numero_decimal = lambda x: (True, float(x)) if x.replace('.', '', 1).lstrip('-').isdigit() else (False, None)

es_numero_decimal, numero = validar_numero_decimal(entrada)

if es_numero_decimal:
    print(f"Has ingresado un número decimal válido: {numero}")
else:
    print("El valor ingresado no es un número decimal válido.")
'''


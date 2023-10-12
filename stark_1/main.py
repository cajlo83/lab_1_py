'''
autor: Carlo Morici

Desafio Stark 1

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

#menu que consta de un bucle y un match
entrada_menu = str()
while (entrada_menu != "Z" and entrada_menu != "z"):
    entrada_menu = input(cadena_menu)
    match (entrada_menu):
        
   
#A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
        case "a" | "A":
            print("entramos a opcion a")
            for personaje in lista_personajes:
                print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))





#B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO) 
        case "b" | "B":
            #bucle para calculr fuerza maxima
            max_fuerza = -1    
            for personaje in lista_personajes:
                if (max_fuerza < int(personaje["fuerza"])):
                    max_fuerza = int(personaje["fuerza"])

            #bucle para mostrar a quien cumplea con la fuerza maxima    
            for personaje in lista_personajes:
                if (max_fuerza == int(personaje["fuerza"])):
                    print("{0} - {1}".format(personaje["identidad"], personaje["peso"]))




 #C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
        case "c" | "C":
            #se calcula altura minima con un bucle y una bandera que chequea si es la primera revision
            min_altura = float()
            bandera_min_altura = True 
            for personaje in lista_personajes:
                if (bandera_min_altura):
                    min_altura = float(personaje["altura"])
                    bandera_min_altura = False
                
                elif (min_altura > float(personaje["altura"])):
                    min_altura = float(personaje["altura"])

            #bucle para mostrar a quien cumple con la altura minima    
            for personaje in lista_personajes:
                if (min_altura == float(personaje["altura"])):
                    print("{0} - {1}".format(personaje["nombre"], personaje["identidad"]))




#D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)+++++
        case "D" | "d":
            #se calcula peso masculino promedio con un bucle, un contador y un acumulador
            acumulador_peso_masculino = 0
            contador_masculinos = 0    
            for personaje in lista_personajes:
                if (personaje["genero"] == "M"):
                    contador_masculinos += 1
                    acumulador_peso_masculino += float(personaje["peso"])
            
            #muestro el peso masculino promedio si corresponde
            if(contador_masculinos <= 0):
                print("no hay personajes masculinos")
            else:
                promedio_peso_masculino = acumulador_peso_masculino/contador_masculinos
                print("el peso masculino promedio es " + str(promedio_peso_masculino))




#E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
        case "e" | "E":
            #se suman y se cuentan los datos de las femeninas con un bucle
            acumulador_fuerza_femenino = int()
            contador_femeninos = int()
            for personaje in lista_personajes:
                if (personaje["genero"] == "F"):
                    contador_femeninos += 1
                    acumulador_fuerza_femenino += int(personaje["fuerza"])
            
            #calculo el promedio de fuerza femenina si corresponde
            if(contador_femeninos <= 0):
                print("no hay personajes femeninos")
            else:
                promedio_fuerza_femenino = float(acumulador_fuerza_femenino/contador_femeninos)

                #muestro informacion correspondiente a los resultados
                bandera_correspondientes_E = True
                for personaje in lista_personajes:
                    if(promedio_fuerza_femenino < int(personaje["fuerza"])):
                        print("{0} - {1}".format(personaje["nombre"], personaje["peso"]))
                        bandera_correspondientes_E = False
                #print("promedio de fuerza= " + str(promedio_fuerza_femenino))
                #tambien aviso si no hay datos a mostrar
                if(bandera_correspondientes_E):
                    print("nadie cumple con el requisito")




#OPCION PARA SALIR     
        case "z" | "Z":
            print ("nos vamos")
#OPCION INCORRECTA
        case _:
            print("opcion incorrecta. reintenta")






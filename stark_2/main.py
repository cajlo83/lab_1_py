'''
autor: Carlo Morici

Desafio Stark 2

Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia

NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú

'''

#importo data
from data_stark import lista_personajes
from data_menu import cadena_menu
from archivo_funciones_stark import *

#muestro data
#print(lista_personajes)

#menu que consta de un bucle y un match
entrada_menu = str()
while (entrada_menu != "Z" and entrada_menu != "z"):
    entrada_menu = input(cadena_menu)
    match (entrada_menu):
       



#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
        case "a" | "A":
            print("entramos a opcion A:\n")

            #se filtra lista de coincidencias con el genero NB
            lista_resultado_a = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")
           
            #se muestran resultados al usuario
            if (lista_diccionarios_imprimir_clave(lista_resultado_a,"nombre")):
                print("esas fueron las coincidencias\n")
            else:
                print("no hay coincidencias para mostrar\n")

           

#B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
        case "b" | "B":
            print("entramos a opcion B:\n")

            #se filtra lista de coincidencias con el genero F
            lista_resultado_b = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "F")

            #se filtran coincidencias de estatura maxima
            lista_resultado_b = lista_diccionarios_mayor_valor_numerico(lista_resultado_b,"altura")

            #se muestran resultados al usuario
            if (lista_diccionarios_imprimir_clave(lista_resultado_b,"nombre")):
                print("esas fueron las coincidencias\n")
            else:
                print("no hay coincidencias para mostrar\n")




#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
        case "c" | "C":
            print("entramos a opcion C:\n")

            #se filtra lista de coincidencias con el genero M
            lista_resultado_c = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "M")

            #se filtran coincidencias de estatura maxima
            lista_resultado_c = lista_diccionarios_mayor_valor_numerico(lista_resultado_c,"altura")

            #se muestran resultados al usuario
            if (lista_diccionarios_imprimir_clave(lista_resultado_c,"nombre")):
                print("esas fueron las coincidencias\n")
            else:
                print("no hay coincidencias para mostrar\n")



#D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
        case "D" | "d":
            print("entramos a opcion D:\n")

            #se filtra lista de coincidencias con el genero M
            lista_resultado_d = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "M")
            
            #se filtran coincidencias de fuerza minima
            lista_resultado_d = lista_diccionarios_menor_valor_numerico(lista_resultado_d,"fuerza")
            
            #se muestran resultados al usuario
            if (lista_diccionarios_imprimir_clave(lista_resultado_d,"nombre")):
                print("esas fueron las coincidencias\n")
            else:
                print("no hay coincidencias para mostrar\n")





#E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
        case "e" | "E":
            print("entramos a opcion E:\n")

            #se filtra lista de coincidencias con el genero NB
            lista_resultado_e = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")
            
            #se filtran coincidencias de fuerza minima
            lista_resultado_e = lista_diccionarios_menor_valor_numerico(lista_resultado_e,"fuerza")
            
            #se muestran resultados al usuario
            if (lista_diccionarios_imprimir_clave(lista_resultado_e,"nombre")):
                print("esas fueron las coincidencias\n")
            else:
                print("no hay coincidencias para mostrar\n")




#F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
        case "f" | "F":
            print("entramos a opcion F:\n")

            #se filtra lista de coincidencias con el genero NB
            lista_resultado_f = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")
            
            #se calcula promedio
            resultado_f = lista_diccionarios_calcular_promedio(lista_resultado_f,"fuerza")

            
            #se muestran resultados al usuario
            if (resultado_f != None):
                print("la fuerza promedio de los superhéroes de género NB es: " +str(resultado_f)+ "\n")
            else:
                print("no hay coincidencias para mostrar\n")




#G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
        case "g" | "G":
            print("entramos a opcion G:\n")

            #hago un diccionario para cada color de ojos y su contador
            diccionario_ojos_repetidos = lista_diccionarios_contar_coincidencias(lista_personajes, "color_ojos")

            #se muestran resultados
            if (not(imprimir_diccionario(diccionario_ojos_repetidos))):
                print("El diccionario esta vacio")




#H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
        case "h" | "H":
            print("entramos a opcion H:\n")

            #hago un diccionario para cada color de ojos y su contador
            diccionario_pelos_repetidos = lista_diccionarios_contar_coincidencias(lista_personajes, "color_pelo")

            #se muestran resultados
            if (not(imprimir_diccionario(diccionario_pelos_repetidos))):
                print("El diccionario esta vacio")




#I. Listar todos los superhéroes agrupados por color de ojos.
        case "i" | "I":
            print("entramos a opcion I:\n")

            #hago una copia ordenada de la lista
            lista_h = lista_diccionarios_sorted(lista_personajes,"color_ojos")

            #se muestran resultados
            if (lista_diccionarios_imprimir_nombres_organizados(lista_h, "color_ojos")):
                print("esas fueron los resultados\n")
            else:
                print("no hay resultados para mostrar\n")




#J. Listar todos los superhéroes agrupados por tipo de inteligencia
        case "j" | "J":
            print("entramos a opcion J:\n")

            #hago una copia ordenada de la lista
            lista_j = lista_diccionarios_sorted(lista_personajes,"inteligencia")

            #se muestran resultados
            if (lista_diccionarios_imprimir_nombres_organizados(lista_j, "inteligencia")):
                print("esas fueron los resultados\n")
            else:
                print("no hay resultados para mostrar\n")








#OPCION PARA SALIR     
        case "z" | "Z":
            print ("nos vamos")
#OPCION INCORRECTA
        case _:
            print("opcion incorrecta. reintenta")






from stark_sub_biblioteca import *
from typing import Union



def stark_normalizar_datos(lista_heroes:list[dict])->bool:
    '''
    Recibe: una lista de diccionarios
    Verifica las claves de fuerza, peso y altura de cada heroe para que sean numericas y las rectifica de ser necesario
    Retorna: False en caso de no hacer cambios o de recibir una lista vacio, True en caso contrario.
    '''
    #verifica si la lista esta vacia para hacer el debido retorno
    if lista_heroes == []:
        return False

    #el retorno no cambia a menos que se haga un cambio a lo largo del bucle
    retorno = False
    for heroe in lista_heroes:
        
        #altura: float
        if not isinstance(heroe["altura"], float): #se verifica que el valor de la clave no sea del formato buscado            
            if verificar_numero_real(heroe["altura"]): #se verifica que el valor a castear sea una cadena que represente al formato buscado                
                #se hace el casteo, el redondeo y se cambia el retorno
                altura_casteada = float(heroe["altura"])
                altura_redondeada = round(altura_casteada, 2)
                heroe["altura"] = altura_redondeada
                retorno = True

        #peso: float
        if not isinstance(heroe["peso"], float): #se verifica que el valor de la clave no sea del formato buscado            
            if verificar_numero_real(heroe["peso"]): #se verifica que el valor a castear sea una cadena que represente al formato buscado                
                #se hace el casteo, el redondeo y se cambia el retorno
                peso_casteado = float(heroe["peso"])
                peso_redondeado = round(peso_casteado, 2)
                heroe["peso"] = peso_redondeado
                retorno = True

        #fuerza: int
        if not isinstance(heroe["fuerza"], int): #se verifica que el valor de la clave no sea del formato buscado            
            if verificar_numero_entero(heroe["fuerza"]): #se verifica que el valor a castear sea una cadena que represente al formato buscado                
                #se hace el casteo y se cambia el retorno
                heroe["fuerza"] = int(heroe["fuerza"])
                retorno = True
        
    return retorno




def obtener_dato(heroe: dict, dato:str)-> Union[bool, str]:
    '''
    Recibe: un diccionario que representa un heroe, una cadena que representa una clave en el diccionario
    Retorna: False en caso de no haber nombre para el diccionario o estar vacio, de lo contrario retorna el contenido de la clave "dato"
    '''
    #si el diccionario esta vacio o no contiene las claves correspondientes, retorna false
    if (heroe == {}) or not ("nombre" in heroe) or not (dato in heroe):
        return False
    
    #si no hubo retorno False, se verifica el contenido de heroe[dato]
    return heroe[dato]




def obtener_nombre(heroe: dict)-> Union[bool, str]:
    '''
    Recibe: un diccionario que representa un heroe
    Retorna: el nombre de ese heroe en formato "Nombre: Howard the Duck", False en caso de error
    '''
    #si el diccionario esta vacio o no contiene las claves correspondientes, retorna false
    if (heroe == {}) or not ("nombre" in heroe):
        return False
    
    #si no hubo retorno False, se da el formato deseado a los datos obtenidos para hacer el debido retorno
    cadena_retorno = f'Nombre: {heroe["nombre"]}'
    return cadena_retorno




def obtener_nombre_y_dato(heroe: dict, dato:str)-> Union[bool, str]:
    '''
    Recibe: un diccionario que representa un heroe y una cadena que representa una clave en el diccionario
    Retorna: la informacion en formato "Nombre: Venom | fuerza: 500". False en caso de error
    '''
    
    #si heroe es un diccionario vacio, retorna False
    if heroe == {}:
        return False
    
    #solicito los datos buscados y retorno false en caso de inconveniente
    dato_recibido = obtener_dato(heroe, dato)
    nombre_recibido = obtener_nombre(heroe)
    if (nombre_recibido == False) or (dato_recibido == False):
        return False
    
    #si no hubo retorno False, se da el formato deseado a los datos obtenidos para hacer el debido retorno
    cadena_retorno = f'{nombre_recibido} | {dato}: {dato_recibido}'
    return cadena_retorno




def obtener_maximo(lista_diccionarios:list[dict], clave_numerica:str)->Union[bool,int,float]:
    '''
    Recibe: una lista de diccionarios y una clave cuyo contenido debe ser tipo numerico
    retorna: el maximo valor encontrado de dicha clave (int o float). False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_diccionarios == []:
        return False

    bandera_primera = True
    for diccionario in lista_diccionarios:

        if (isinstance(diccionario[clave_numerica], float)) or (isinstance(diccionario[clave_numerica], int)): #se verifica que el valor represente a un numero real o entero
            
            if (bandera_primera): #primera comparacion de valores numericos con una bandera
                bandera_primera = False
                numero_mayor = diccionario[clave_numerica]

            elif (numero_mayor < diccionario[clave_numerica]):
                numero_mayor = diccionario[clave_numerica]

    return numero_mayor




def obtener_minimo(lista_diccionarios:list[dict], clave_numerica:str)->Union[bool,int,float]:
    '''
    Recibe: una lista de diccionarios y una clave cuyo contenido debe ser tipo numerico
    retorna: el minimo valor encontrado de dicha clave (int o float). False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_diccionarios == []:
        return False

    bandera_primera = True
    for diccionario in lista_diccionarios:
        
        if (isinstance(diccionario[clave_numerica], float)) or (isinstance(diccionario[clave_numerica], int)): #se verifica que el valor represente a un numero real o entero
            
            if (bandera_primera): #primera comparacion de valores numericos con una bandera
                bandera_primera = False
                numero_menor = diccionario[clave_numerica]

            elif (numero_menor > diccionario[clave_numerica]):
                numero_menor = diccionario[clave_numerica]

    return numero_menor




def obtener_dato_cantidad(lista_diccionarios:list[dict], clave_numerica:str, valor: Union[int, float])->list[dict]:
    '''
    Recibe: una liste da diccionarios, una clave_numerica que debe estar presente en los diccionarios y un valor que debe cumplir el contenido de clave_numerica
    retorna: una lista de heroes coincidentes
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_diccionarios == []:
        return False

    #se crea una lista vacia que sera retornada
    lista_final = []
    
    for diccionario in lista_diccionarios: #se recorren los diccionarios en la lista con un bucle
        if (valor == diccionario[clave_numerica]): #se verifica si el diccionario evaluado cumple el requisito
            lista_final.append(diccionario) #si cumple, entonces el diccionario se guarda en lista final

    return lista_final

def stark_imprimir_heroes(lista_personajes:list[dict])->bool:
    '''
    Recibe: una lista de heroes
    Retorna: False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_personajes == []:
        return False    

    #si no hubo retorno entonces imprime
    
    #titulos
    print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9}\n".format("nombre", "identidad", "empresa", "altura", "peso", "genero", "color_ojos", "color_pelo", "fuerza", "inteligencia"))
    for personaje in lista_personajes:
                #datos
                print("{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9}".format(personaje["nombre"], personaje["identidad"], personaje["empresa"], personaje["altura"], personaje["peso"], personaje["genero"], personaje["color_ojos"], personaje["color_pelo"], personaje["fuerza"], personaje["inteligencia"]))
    return True




def sumar_dato_heroe(lista_personajes:list[dict], clave_numerica:str)->Union[bool,int,float]: 
    '''
    Recibe: una liste da diccionarios y una clave_numerica que debe estar presente en los diccionarios
    Retorna: La suma de los valores. False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_personajes == []:
        return False
    
    
    retorno = 0 #variable donde se guarda la sumatoria de datos
    for personaje in lista_personajes:

        #si personaje no es un diccionario o si es un diccionario vacio, retorna False
        if not(isinstance(personaje,dict)) or (personaje == {}):
            return False
        
        retorno += personaje[clave_numerica] #si el diccionario cumple los parametros, entonces se guarda el dato buscado

    return retorno




def dividir(divisor:Union[int,float], dividendo:Union[int,float])->float: 
    '''
    verificar si el divisor es 0, en caso de serlo, retornar False, caso contrario realizar la división entre los parámetros y retornar el resultado
    '''

    #si el dividendo es 0, retorna False
    if dividendo == 0:
        return False
    
    return divisor/dividendo




def calcular_promedio(lista_personajes:list[dict], clave_numerica:str)->float:
    '''
    Recibe: una liste da diccionarios y una clave_numerica que debe estar presente en los diccionarios
    Retorna: el promedio de los valores. False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_personajes == []:
        return False
    
    suma = sumar_dato_heroe(lista_personajes, clave_numerica) #se calcula la suma de los datos
    promedio = dividir(suma, len(lista_personajes)) # promedio = suma de elementos / cantidad de elementos
    
    return promedio

def mostrar_promedio_dato(lista_personajes:list[dict], clave_numerica:str)->bool:
    '''
    Recibe: una liste da diccionarios y una clave_numerica que debe estar presente en los diccionarios
    muestra el promedio correspondiente segun lo indicado en clave_numerica
    Retorna: False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_personajes == []:
        return False
    
    #verifica que los valores sean tipo int o float, de lo contrario retorna False
    for personaje in lista_personajes:
        if not(isinstance(personaje[clave_numerica],int)) and not(isinstance(personaje[clave_numerica],float)):
            return False
        
    #calculo el promedio y lo muestro
    promedio = calcular_promedio(lista_personajes, clave_numerica)
    print(f"El promedio de {clave_numerica} es: {promedio}")

    return True




def imprimir_menu():
    cadena_menu = """
    *****     *****     *****     *****     *****     *****     *****     *****     *****     *****     *****     
A. Normalizar datos (No se debe poder acceder a los otros puntos) 
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB 
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M 
F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB 
G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB 
H. Determinar cuántos superhéroes tienen cada tipo de color de ojos. 
I. Determinar cuántos superhéroes tienen cada tipo de color de pelo. 
J. Listar todos los superhéroes agrupados por color de ojos. 
K. Listar todos los superhéroes agrupados por tipo de inteligencia

Z. Salir"""

    print(cadena_menu)




def validar_entero(cadena_entrada:str)->bool: 
    '''
    Verifica que cadena_entrada sea un string conformado únicamente por dígitos.
    Retorna: True o False
    '''

    #con una funcion lambda y el metodo isdigit se verifica si el string corresponde o no a un entero
    validar_numero_no_decimal = lambda x: (True) if x.isdigit() else (False)

    retorno = validar_numero_no_decimal(cadena_entrada)

    return retorno




def stark_menu_principal()->Union[bool,str]:
    '''
    Imprime el menu y solicita al usuario escoger una opcion
    Retorna: una opcion correcta o False
    '''
    imprimir_menu() #imprime el menu
    entrada_menu = input("\topcion:") #solicita la opcion

    match (entrada_menu):
        case 'a' | 'A' | 'b' | 'B' | 'c' | 'C' | 'd' | 'D' | 'e' | 'E' | 'f' | 'F' | 'g' | 'G' | 'h' | 'H' | 'i' | 'I' | 'j' | 'J' | 'k' | 'K' | 'z' | 'Z' :
            return entrada_menu
        case _:
            return False


















def stark_marvel_app(lista_personajes:list[dict]):
    '''
    Recibe: la lista de personajes
    muestra el menu, valida la opcion seleccionada y hace la llamada de funcion correspondiente
    '''

    bandera_a = False #bandera que avisa la no ejecucion de la opcion A

    #se muestra el menu en un bucle controlado por "entrada_menu"
    entrada_menu =""
    while (entrada_menu != "Z" and entrada_menu != "z"):
        entrada_menu = stark_menu_principal() #el valor de entrada_menu es controlado con la funcion stark_menu_principal()



        match (entrada_menu):

        #A. Normalizar datos (No se debe poder acceder a los otros puntos)
            case "a" | "A":
                print("entramos a opcion A:\n")

                # bandera_a controlara el ingres a todas las opciones del menu
                bandera_a = True

                # True: almenos un dato se pudo normalizar. False: error en lista o datos modificados previamente.
                if stark_normalizar_datos(lista_personajes): 
                    print("Datos Normalizados")
                else:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")   




        #B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB 
            case "b" | "B":
                print("entramos a opcion B:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:
                    
                    #se filtra lista de coincidencias con el genero NB
                    lista_resultado_a = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")
                
                    #se muestran resultados al usuario
                    if (lista_diccionarios_imprimir_clave(lista_resultado_a,"nombre")):
                        print("\nesas fueron las coincidencias\n")
                    else:
                        print("no hay coincidencias para mostrar\n")
                else:
                    print("AVISO: Debe normalizar los datos para continuar")




        #C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
            case "c" | "C":
                print("entramos a opcion C:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #se filtra lista de coincidencias con el genero F
                    lista_femeninas = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "F")

                    #se calcula la altura mas alta de la lista filtrada
                    mas_alta = obtener_maximo(lista_femeninas,"altura")

                    #se filtran los personajes que coinciden con lo requerido
                    lista_mas_altas = obtener_dato_cantidad(lista_personajes,"altura" ,mas_alta)

                    #se muestran resultados al usuario
                    if stark_imprimir_heroes(lista_mas_altas):
                        print("\nesas fueron las coincidencias\n")
                    else:
                        print("no hay coincidencias para mostrar\n")
                    
                else:
                    print("AVISO: Debe normalizar los datos para continuar")




        #D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
            case "D" | "d":
                print("entramos a opcion D:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #se filtra lista de coincidencias con el genero M
                    lista_masculinos = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "M")

                    #se calcula la altura mas alta de la lista filtrada
                    mas_alto = obtener_maximo(lista_masculinos,"altura")

                    #se filtran los personajes que coinciden con lo requerido
                    lista_mas_altos = obtener_dato_cantidad(lista_masculinos,"altura" ,mas_alto)
                    
                    #se muestran resultados al usuario
                    if stark_imprimir_heroes(lista_mas_altos):
                        print("\nesas fueron las coincidencias\n")
                    else:
                        print("no hay coincidencias para mostrar\n")

                else:
                    print("AVISO: Debe normalizar los datos para continuar")





        #E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M 
            case "e" | "E":
                print("entramos a opcion E:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #se filtra lista de coincidencias con el genero M
                    lista_masculinos = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "M")

                    #se calcula la fuerza mas baja de la lista filtrada
                    mas_debil_m = obtener_minimo(lista_masculinos,"fuerza")

                    #se filtran los personajes que coinciden con lo requerido
                    lista_mas_debiles_m = obtener_dato_cantidad(lista_masculinos,"fuerza" ,mas_debil_m)
                    
                    #se muestran resultados al usuario
                    if stark_imprimir_heroes(lista_mas_debiles_m):
                        print("\nesas fueron las coincidencias\n")
                    else:
                        print("no hay coincidencias para mostrar\n")

                else:
                    print("AVISO: Debe normalizar los datos para continuar")




        #F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB 
            case "f" | "F":
                print("entramos a opcion F:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #se filtra lista de coincidencias con el genero NB
                    lista_nb = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")

                    #se calcula la fuerza mas baja de la lista filtrada
                    mas_debil_nb = obtener_minimo(lista_nb,"fuerza")
                    if mas_debil_nb is not False:

                        #se filtran los personajes que coinciden con lo requerido
                        lista_mas_debiles_nb = obtener_dato_cantidad(lista_nb,"fuerza" ,mas_debil_nb)
                        
                        #se muestran resultados al usuario
                        if stark_imprimir_heroes(lista_mas_debiles_nb):
                            print("\nesas fueron las coincidencias\n")
                    else:
                        print("no hay coincidencias para mostrar\n")

                else:
                    print("AVISO: Debe normalizar los datos para continuar")


 


        #G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB 
            case "g" | "G":
                print("entramos a opcion G:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #se filtra lista de coincidencias con el genero NB
                    lista_nb = lista_diccionarios_buscar_coincidencias(lista_personajes, "genero", "NB")

                    promedio = calcular_promedio(lista_nb,"fuerza")
                    if promedio is not False:
                        print(f'el promedio de fuerza de los presonajes NB es: {promedio}')
                    else:
                        print("no hay datos para calcular.")
                else:
                    print("AVISO: Debe normalizar los datos para continuar")






        #H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            case "h" | "H":
                print("entramos a opcion H:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #hago un diccionario para cada color de ojos y su contador
                    diccionario_ojos_repetidos = lista_diccionarios_contar_coincidencias(lista_personajes, "color_ojos")

                    #se muestran resultados
                    if (not(imprimir_diccionario(diccionario_ojos_repetidos))):
                        print("El diccionario esta vacio")
                else:
                    print("AVISO: Debe normalizar los datos para continuar")



        # I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            case "i" | "I":
                print("entramos a opcion I:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #hago un diccionario para cada color de pelo y su contador
                    diccionario_pelos_repetidos = lista_diccionarios_contar_coincidencias(lista_personajes, "color_pelo")

                    #se muestran resultados
                    if (not(imprimir_diccionario(diccionario_pelos_repetidos))):
                        print("El diccionario esta vacio")
                else:
                    print("AVISO: Debe normalizar los datos para continuar")


        #J. Listar todos los superhéroes agrupados por color de ojos.
            case "j" | "J":
                print("entramos a opcion I:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:
                    
                    print("metodo antiguo*********************************")
                    #hago una copia ordenada de la lista
                    lista_J = lista_diccionarios_sorted(lista_personajes,"color_ojos")

                    #se muestran resultados
                    resultado_J = stark_imprimir_heroes(lista_J)
                    if (resultado_J == False):
                        print("no hay resultados para mostrar\n")
                    else:
                        print("esas fueron los resultados\n")


                    ###################################################


                    print("metodo nuevo*********************************")
                    # hace una lista de los distintos colores de ojos
                    lista_color_ojos = lista_diccionarios_listar_coincidencias(lista_personajes, "color_ojos")
                    
                    for color in lista_color_ojos: #recorro la lista de colores
                        print(f'\ncolor {color}:')
                        for personaje in lista_personajes: #recorro la lista de personajes 
                            if personaje["color_ojos"] == color or (personaje["color_ojos"] == "" and color == "no data"): #si hay coincidencia, se imprime el nombre
                                nombre_j = obtener_nombre(personaje) 
                                print(nombre_j)
                else:
                    print("AVISO: Debe normalizar los datos para continuar")




        #K. Listar todos los superhéroes agrupados por tipo de inteligencia
            case "K" | "k":
                print("entramos a opcion K:\n")

                #si bandera_a es False entonces aun no se ha ejecutado la opcion A, y no se debe acceder aun a la opcion
                if bandera_a:

                    #hago una copia ordenada de la lista
                    lista_K = lista_diccionarios_sorted(lista_personajes,"inteligencia")

                    #se muestran resultados
                    resultado_J = stark_imprimir_heroes(lista_K)
                    if (resultado_J == False):
                        print("no hay resultados para mostrar\n")
                    else:
                        print("esas fueron los resultados\n")


                    ###################################################


                    print("metodo nuevo*********************************")
                    # hace una lista de las distintas inteligencias
                    lista_inteligencias = lista_diccionarios_listar_coincidencias(lista_personajes, "inteligencia")
                    
                    for inteligencia in lista_inteligencias: #recorro la lista de inteligencias
                        print(f'\ninteligencia {inteligencia}:')
                        for personaje in lista_personajes: #recorro la lista de personajes 
                            if personaje["inteligencia"] == inteligencia or (personaje["inteligencia"] == "" and inteligencia == "no data"): #si hay coincidencia, se imprime el nombre
                                nombre_k = obtener_nombre(personaje) 
                                print(nombre_k)
                else:
                    print("AVISO: Debe normalizar los datos para continuar")




        #OPCION PARA SALIR     
            case "z" | "Z":
                print ("Adios")
                

        #OPCION incorrecta     
            case False:
                print ("\n\t__--ERROR: opcion incorrecta--__")
                
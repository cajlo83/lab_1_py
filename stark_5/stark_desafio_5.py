import json
from stark_sub_biblioteca import *
import re





def imprimir_menu_desafio_5():
    '''
    imprime el menu de opciones
    '''
    str_menu = """
----------------------------------------------------------------------------------------------------------------------
|    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M                           |
|    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F                           |
|    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M                                    |
|    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F                                    |
|    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M                                    |
|    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F                                    |
|    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M                             |
|    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F                             |
|    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)    |
|    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.                                            |
|    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.                                            |
|    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de                                  |
|    no tener, Inicializarlo con ‘No Tiene’).                                                                        |
|    M. Listar todos los superhéroes agrupados por color de ojos.                                                    |
|    N. Listar todos los superhéroes agrupados por color de pelo.                                                    |
|    O. Listar todos los superhéroes agrupados por tipo de inteligencia                                              |
|                                                                                                                    |
|    Z. Salir                                                                                                        |
----------------------------------------------------------------------------------------------------------------------
    """
    print(str_menu)



def stark_menu_principal_desafio_5():
    '''
    Genera la interaccion entre el usuario y la maquina a travez del menu
    valida con regex que la entrada sea correcta
    '''

    imprimir_menu_desafio_5()
    entrada = input("Seleccione una opción: ")
   
    # re.match() retorna None que puede ser interpretado como False o un objeto match que peude ser interpretado como True
    if re.match(r'^[a-oA-OzZ]$', entrada.strip()): # se eliminan caracteres ' ' para facilitar interaccion

        return entrada.upper() # se retorna en mayusculas
    else:
        return -1
        






def stark_marvel_app_5(lista_heroes:list[dict]):
    '''
    Recibe: la lista de personajes
    ejecuta el codigo constantemente decidiendo a que punto del menu entrar hasta que se envie el comando de salida
    '''
    if not valida_lista(lista_heroes):
        print("No se recibio correctamente lista_personajes desde el archivo o la lista esta vacia")
        return


    bandera_normalizacion = False
    bandera_iniciales = False
    bandera_codigos = False
    while True:
        opcion = stark_menu_principal_desafio_5()

        match opcion:

            case 'Z':
                print("***")
                break

            case -1:
                print("**AVISO****\t No se ha escogido una opcion valida \t****AVISO**")


'''
            case '1':
                stark_imprimir_nombres_con_iniciales(lista_heroes)
                bandera_iniciales = True

            case '2':
                stark_generar_codigos_heroes(lista_heroes)
                bandera_codigos = True

            case '3':
                stark_normalizar_datos(lista_heroes)
                bandera_normalizacion = True
            case '4':
                stark_imprimir_indice_nombre(lista_heroes)
            case '5':
                if bandera_normalizacion:
                    if not bandera_codigos or not bandera_iniciales:
                        print("Puede que no se muestren algunos datos si no pasa primero por las opciones 1 y 2")
                    stark_navegar_fichas(lista_heroes)
                else:
                    print("primero se deben normalizar los datos.")
'''

def leer_archivo (nombre_archivo:str) -> list[dict]:
    '''
    Recibe: el nombre/la direccion de un archivo junto con su extensión (ejemplo: 'archivo.csv').
    Abre el archivo en modo lectura. Recupera la data del archivo la cual inicialmente sera una diccionario que contiene una lista de diccionarios.
    Retorna: la lista de diccionarios.

    '''

    with open(nombre_archivo, 'r') as archivo:
        data = json.load(archivo) # {heroes:lista[]}
        lista = data.get('heroes', []) # heroes[]
        return lista


def guardar_archivo (nombre_archivo:str, contenido:str) -> bool:
    '''
    Recibe: el nombre/la direccion con el cual se guardará el archivo junto con su extensión (ejemplo: 'archivo.csv').
    Abre el archivo en modo 'w+''. y guarda el texto almacenado en contenido
    Retorna: bool
    '''

    try:
        with open(nombre_archivo, 'w+') as archivo:
            json.dump(contenido, archivo)
            print(f"se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"‘Error al crear el archivo: {nombre_archivo}")
        return True

'''

#guardar de texto plano a formato json

    try:
        with open(nombre_archivo, 'w+') as archivo:
            json.dump(contenido, archivo, indent=4, separators=(',\n', ': '))
            print(f"se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"‘Error al crear el archivo: {nombre_archivo}")
        return True
'''

def capitalizar_palabras(cadena_entrada:str) -> str:
    '''
    Recibe una cadena de caracteres con una o varias palabras
    Se separa la cadena en palabras, se capitaliza cada una y se vuelven a unir en una misma cadena
    Retorna: La Cadena Con Cada Palabra Capitalizada
    '''

    lista_palabras = cadena_entrada.split()
    lista_capitalizada = []
    for palabra in lista_palabras:
        lista_capitalizada.append(palabra.capitalize())

    cadena_salida = ' '.join(lista_capitalizada)

    return cadena_salida

def obtener_nombre_capitalizado(diccionario:dict) -> str:
    '''
    Recibe: un diccionario que se presume contiene la key 'nombre'
    Retorna: una cadena con formato "Nombre: Venom"
    '''

    nombre_heroe = diccionario.get('nombre', '?') # metodo get en caso de error en el nombre
    nombre_heroe = capitalizar_palabras(nombre_heroe)

    cadena_salida = f"Nombre: {nombre_heroe}"

    return cadena_salida


def obtener_nombre_y_dato(diccionario:dict, clave_str:str) -> str:
    '''
    Recibe: un diccionario que se presume contiene la key 'nombre' y la clave representada por clave_str
    Retorna: una cadena con formato "Nombre: Venom | clave: contenido_clave"
    '''
    # para el nombre
    cadena_nombre = obtener_nombre_capitalizado(diccionario)

    # para la clave
    cadena_clave = obtener_dato_diccionario(diccionario, clave_str)

    # salida
    cadena_salida = f"{cadena_nombre} | {cadena_clave}"
    return cadena_salida




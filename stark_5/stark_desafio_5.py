from stark_sub_biblioteca import *
import re
import json








################################ parte 1 ################################

def imprimir_menu_desafio_5():
    '''
    imprime el menu de opciones
    '''
    str_menu = """
-----------------------------------------------------------------------------------------------------------------------------
|    A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M                                  |
|    B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F                                  |
|    C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M                                           |
|    D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F                                           |
|    E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M                                           |
|    F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F                                           |
|    G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M                                    |
|    H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F                                    |
|    I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)           |
|    J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.                                                   |
|    K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.                                                   |
|    L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener,                               |
|       Inicializarlo con ‘No Tiene’).                                                                                      |
|    M. Listar todos los superhéroes agrupados por color de ojos.                                                           |
|    N. Listar todos los superhéroes agrupados por color de pelo.                                                           |
|    O. Listar todos los superhéroes agrupados por tipo de inteligencia                                                     |
|                                                                                                                           |
|    Z. Salir                                                                                                               |
-----------------------------------------------------------------------------------------------------------------------------
    """
    imprimir_dato(str_menu)



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

    while True:
        opcion = stark_menu_principal_desafio_5()

        match opcion:

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
            case 'A':
                print("*** opcion A ***")
                if not stark_guardar_heroe_genero(lista_heroes, 'M'):
                    print("error en opcion A")

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
            case 'B':
                print("*** opcion B ***")
                if not stark_guardar_heroe_genero(lista_heroes, 'F'):
                    print("error en opcion B")

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            case 'C':
                print("*** opcion C ***")
                if not stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 'altura', 'maximo','M'):
                    print("error en opcion C")

# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            case 'D':
                print("*** opcion D ***")
                if not stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 'altura', 'maximo','F'):
                    print("error en opcion D")

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
            case 'E':
                print("*** opcion E ***")
                if not stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 'altura', 'minimo','M'):
                    print("error en opcion E")

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
            case 'F':
                print("*** opcion F ***")
                if not stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 'altura', 'minimo','F'):
                    print("error en opcion F")

# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            case 'G':
                print("*** opcion G ***")
                if not stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,'M'):
                    print("error en opcion G")

# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            case 'H':
                print("*** opcion H ***")
                if not stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes,'F'):
                    print("error en opcion H")

# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            case 'J':
                print("*** opcion J ***")
                if not stark_calcular_cantidad_por_tipo(lista_heroes,'color_ojos'):
                    print("error en opcion J")

# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
            case 'K':
                print("*** opcion K ***")
                if not stark_calcular_cantidad_por_tipo(lista_heroes,'color_pelo'):
                    print("error en opcion K")

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
            case 'L':
                print("*** opcion L ***")
                if not stark_calcular_cantidad_por_tipo(lista_heroes,'inteligencia'):
                    print("error en opcion L")

# M. Listar todos los superhéroes agrupados por color de ojos.
            case 'M':
                print("*** opcion M ***")
                if not stark_listar_heroes_por_dato(lista_heroes,'color_ojos'):
                    print("error en opcion M")

# N. Listar todos los superhéroes agrupados por color de pelo.
            case 'N':
                print("*** opcion N ***")
                if not stark_listar_heroes_por_dato(lista_heroes,'color_pelo'):
                    print("error en opcion N")

# O. Listar todos los superhéroes agrupados por tipo de inteligencia
            case 'O':
                print("*** opcion O ***")
                if not stark_listar_heroes_por_dato(lista_heroes,'inteligencia'):
                    print("error en opcion O")


            case 'Z':
                print("*** saliendo ***")
                break

            case -1:
                print("**AVISO****\t No se ha escogido una opcion valida \t****AVISO**")



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
    directorio_archivo = armar_directorio_stark_5(nombre_archivo)

    try:
        with open(directorio_archivo, 'w+') as archivo:
            archivo.write(contenido)
            print(f"se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"‘Error al crear el archivo: {nombre_archivo}")
        return False

'''

#guardar de texto plano a formato json

    try:
        with open(nombre_archivo, 'w+') as archivo:
            json.dump(contenido, archivo, indent=4, separators=(',\n', ': '))
            print(f"se creo el archivo: {nombre_archivo}")
            return True
    except Exception:
        print(f"‘Error al crear el archivo: {nombre_archivo}")
        return False
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

    # salidas:
    cadena_salida = f"{cadena_nombre} | {cadena_clave}"
    return cadena_salida








################################ parte 2 ################################

def es_genero(heroe:dict, genero_buscado:str) -> bool:
    '''
    Recibe: un diccionario que representa a un heroe y un string que representa al genero buscado
    verifica que se haya ingresado un genero correcto a buscar y que el heroe coincida con el genero buscado
    Retorna: True o False
    
    '''
    return genero_buscado in ['M', 'F','NB'] and diccionario_coincidencia(heroe,'genero', genero_buscado)

def stark_guardar_heroe_genero(lista_heroes:list[dict], genero_buscado:str) -> bool:
    '''
    Recibe: una lista de diccionarios que representa a una lista de heroes y un string que representa un genero buscado
    Imprime los heroes que coinciden con el parametro y ademas los guarda en un archivo .csv
    Retorna: True o False
    '''

    lista_nombres = [] 
    
    for heroe in lista_heroes:
        if es_genero(heroe, genero_buscado):
            nombre_actual = obtener_nombre_capitalizado(heroe)
            imprimir_dato(nombre_actual)
            
            lista_nombres.append(nombre_actual) # los nombres se guardan en una lista
    nombres_string_csv = ', '.join(lista_nombres) # se convierte la lista de nombres en un string que contiene los nombres en CSV

    print(f'nombres_string_csv: {nombres_string_csv}')
    print(f'nombre_actual: {nombre_actual}')
    nombre_archivo = r"heroes_" + genero_buscado + ".csv"
    return guardar_archivo(nombre_archivo,nombres_string_csv) # abre en w+






################################ parte 3 ################################




def calcular_max_genero(lista_diccionarios:list[dict], clave_numerica:str, genero_buscado: str) -> Union[bool,dict]:
    '''
    Recibe: una lista de diccionarios, una clave cuyo contenido debe ser tipo numerico y un genero
    retorna: el diccionario que contenga el maximo valor encontrado de dicha clave (int o float). False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if not valida_lista(lista_diccionarios):
        return False

    bandera_primera = True
    diccionario_retorno = {}
    for diccionario in lista_diccionarios:

        #se verifica que diccionario['genero'] == genero_buscado y que diccionario[clave_numerica] represente a un numero
        if diccionario['genero'] == genero_buscado and (verificar_numero_flotante(diccionario[clave_numerica]) or verificar_numero_entero(diccionario[clave_numerica])): 

            numero_actual = float(diccionario[clave_numerica]) # en caso de ser el nuevo mayor, se castea solo una vez
            if (bandera_primera): #primera comparacion de valores numericos con una bandera
                bandera_primera = False
                numero_mayor = numero_actual 
                diccionario_retorno = diccionario

            elif (numero_mayor < numero_actual):
                numero_mayor = numero_actual
                diccionario_retorno = diccionario

    return diccionario_retorno




def calcular_min_genero(lista_diccionarios:list[dict], clave_numerica:str, genero_buscado: str) -> Union[bool,dict]:
    '''
    Recibe: una lista de diccionarios, una clave cuyo contenido debe ser tipo numerico y un genero
    retorna: el diccionario que contenga el minimo valor encontrado de dicha clave (int o float). False en caso de error
    '''

    #si la lista recibida esta vacia, retorna False
    if lista_diccionarios == []:
        return False

    bandera_primera = True
    diccionario_retorno = {}
    for diccionario in lista_diccionarios:

        #se verifica que diccionario['genero'] == genero_buscado y que diccionario[clave_numerica] represente a un numero real o entero
        if diccionario['genero'] == genero_buscado and (verificar_numero_flotante(diccionario[clave_numerica]) or verificar_numero_entero(diccionario[clave_numerica])): 

            
            numero_actual = float(diccionario[clave_numerica]) # en caso de ser el nuevo mayor, se castea solo una vez
            if (bandera_primera): #primera comparacion de valores numericos con una bandera
                bandera_primera = False
                numero_menor = numero_actual 
                diccionario_retorno = diccionario

            elif (numero_menor > numero_actual):
                numero_menor = numero_actual
                diccionario_retorno = diccionario

    return diccionario_retorno



def calcular_max_min_dato_genero(lista_diccionarios:list[dict], clave_numerica:str, tipo_calculo:str, genero_buscado: str) -> Union[bool,dict]:
    '''
    recorre la lista de diccionarios buscando al heroe que cumple con el dato a calcular ('maximo' o 'minimo') en la clave numerica y del genero especificado
    retorna: al heroe que cumpla los requisitos
    '''
    
    match tipo_calculo:
        case 'maximo':
            funcion = calcular_max_genero
        case 'minimo':
            funcion = calcular_min_genero
        case _:
            print("calcular_max_min_genero: no se recibio un tipo_calculo valido")
            return False

    return funcion(lista_diccionarios, clave_numerica, genero_buscado)  




def stark_calcular_imprimir_guardar_heroe_genero(lista_diccionarios:list[dict], clave_numerica:str, tipo_calculo:str, genero_buscado: str) -> bool:
    '''
    busca el heroe que cumpla con el genero y el calculo de clave numerica
    imprime el resultado por pantalla y lo guarda en un archivo con formato heroes_calculo_key_genero.csv
    Recibe: una lista de diccionarios, una clave_numerica que debe estar presente en el diccionario, el tipo de calculo ('maximo','minimo') y el genero buscado
    Retorna: True o False
    '''

    diccionario_local = calcular_max_min_dato_genero(lista_diccionarios,clave_numerica,tipo_calculo,genero_buscado) # se busca el diccionario
    # se arma cadena de salida 


    match tipo_calculo:
        case 'maximo':
            str_salida = f'Mayor {clave_numerica}: {obtener_nombre_y_dato(diccionario_local, clave_numerica)}'
        case 'minimo':
            str_salida = f'Menor {clave_numerica}: {obtener_nombre_y_dato(diccionario_local, clave_numerica)}'
        case _:
            print("stark_calcular_imprimir_guardar_heroe_genero: no se recibio un tipo_calculo valido")
            return False
    
    imprimir_dato(str_salida)

    nombre_archivo = "heroes_" + tipo_calculo + "_" + clave_numerica + "_" + genero_buscado + ".csv"
    return guardar_archivo(nombre_archivo, str_salida)










################################ parte 4 ################################
    




 



def sumar_dato_heroe_genero(lista_personajes:list[dict], clave_numerica:str, genero_buscado:str)->Union[int,float]: 
    '''
    Recibe: una liste da diccionarios y una clave_numerica que debe estar presente en los diccionarios que a su vez deben ser del genero especificado
    Retorna: La suma de los valores. -1 en caso de error
    '''


    
    sumatoria = 0 #variable donde se guarda la sumatoria de datos
    
    # se itera y se valida
    for personaje in lista_personajes:
        if not(isinstance(personaje,dict)) or (personaje == {}):
            return -1
        
        if personaje["genero"] == genero_buscado and verificar_numero_flotante(personaje[clave_numerica]):
            sumatoria += float(personaje[clave_numerica]) #si el diccionario cumple los parametros, entonces se suma el dato buscado

    return sumatoria






def cantidad_heroes_genero(lista_diccionarios:list[dict], genero_buscado:str) -> int:
    '''
    Recibe una lista de diccionarios y un genero
    recorre lista_diccionarios contando cuantos tienen el genero buscado
    Retorna: la cantidad de coincidencias encontradas
    '''
    contador = 0
    for diccionario in lista_diccionarios: # recorro la lista
        if diccionario["genero"] == genero_buscado: # evaluo data
            contador += 1 # cuento

    return contador # retorno







def calcular_promedio_genero(lista_personajes:list[dict], clave_numerica:str, genero_buscado:str)->Union[bool,float]: 
    '''
    Recibe: una lista da diccionarios y una clave_numerica que debe estar presente en los diccionarios que a su vez deben ser del genero especificado
    Retorna: El promedio de los valores. -1 en caso de error
    '''

    # fase de sumatoria
    sumatoria = sumar_dato_heroe_genero(lista_personajes, clave_numerica, genero_buscado)
    if sumatoria < 0:
        print("calcular_promedio_genero: error en diccionarios") 
        return False
    elif sumatoria == 0: # se previene division por 0
        return 0

    # conteo y retorno
    conteo = cantidad_heroes_genero(lista_personajes, genero_buscado)
    return dividir(sumatoria, conteo)




def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_personajes:list[dict],genero_buscado:str) -> bool:
    '''
    Recibe una lista de personajes y un genero a buscar
    verifica se reciba una lista no vacia, verifica sus coincidencias de genero, calcula el promedio, lo muestra y lo guarda
    Retorna: True o False
    '''
    if not valida_lista(lista_personajes):
        print("Error: Lista de heroes vacia")
        return False
    
    promedio = calcular_promedio_genero(lista_personajes, 'altura', genero_buscado)
    if promedio is False:
        print("stark_calcular_imprimir_guardar_promedio_altura_genero: promedio == False")
        return False
    
    cadena_salida = f'Altura promedio genero {genero_buscado}: {promedio:.2f}'
    imprimir_dato(cadena_salida)

    nombre_archivo = "heroes_promedio_altura_" + genero_buscado + ".csv"
    return guardar_archivo(nombre_archivo, cadena_salida)










################################ parte 5 ################################





def calcular_cantidad_tipo(lista_diccionarios:list[dict],tipo_dato:str)->dict:
    '''
    verifica los elementos en lista_diccionarios para ver cuantos tipos de clave_lista hay y contar sus repeticiones.
    Retorna: contenido default en caso de error o un diccionario de contadores con los distintos valores en la clave buscada y sus repeticiones.
    '''
    
    if not valida_lista(lista_diccionarios):
        diccionario =\
        {
            "Error": "La lista se encuentra vacia"
        }
        
        return diccionario
            
    diccionario = lista_diccionarios_contar_coincidencias(lista_diccionarios, tipo_dato)
    return diccionario



def guardar_cantidad_heroes_tipo(diccionario_variedades_contadas:dict, tipo_dato:str) -> bool:
    '''
    Itera las keys del diccionario para guardarlas en un archivo
    Recibe: un diccionario con informacion de caracteristicas contadas y el nombre de dicha caracteristica
    Retorna: True o False
    '''
    
    cadena_diccionarios_archivo = ""

    for clave, valor in diccionario_variedades_contadas.items():
        cadena_salida = f"caracterisitca: {tipo_dato} {clave} - cantidad de heroes: {valor}"
        
        if cadena_diccionarios_archivo:
            cadena_diccionarios_archivo = cadena_diccionarios_archivo + '\n' + cadena_salida
        else:
            cadena_diccionarios_archivo = cadena_salida

        print(cadena_salida)
   

    nombre_archivo = f"heroes_cantidad_{tipo_dato}.csv"
    return guardar_archivo(nombre_archivo, cadena_diccionarios_archivo)





def stark_calcular_cantidad_por_tipo(lista_heroes:list[dict], tipo_dato:str) -> bool:
    '''
    itera la lista, verifica el contenido de la clave indicada. hace un conteo de las repeticiones y las guarda en un archivo
    Recibe: una lista de diccionarios que representan cada uno a un heroe y el tipo de dato que se desea buscar
    Retorna: True o False
    
    '''

    diccionario_cantidades = calcular_cantidad_tipo(lista_heroes, tipo_dato) # se hace el conteo
    return guardar_cantidad_heroes_tipo(diccionario_cantidades, tipo_dato) # se guarda el archivo










################################ parte 6 ################################





def obtener_lista_de_tipos(lista_diccionarios:list[dict], clave_buscada:str) -> set[str]:
    '''
    Recibe una lista de diccionarios y una clave que debe estar en los mismos
    recorre lista_diccionarios generando una lista de los distintos valores que existen, sin repeticiones (no es un set)
    Retorna: una lista de las distintos posibles valores que tienen dichas claves
    '''
    lista_salida = []
    for diccionario in lista_diccionarios: # recorro la lista 
        valor_clave = normalizar_dato(diccionario[clave_buscada], 'N/A') # extraigo el valor
        lista_salida.append(capitalizar_palabras(valor_clave)) # capitalizo y agrego a la lista

    return set(lista_salida) # se convierte a set para eliminar repeticiones




def normalizar_dato(dato_heroe, valor_defecto:str):
    '''
    Verifica que el dato de heroe no este vacio
    Recibe: el dato del heroe y un valor por defecto
    Retorna: el valor por defecto en caso de recibirse una cadena vacia o el dato del heroe sin modificar en caso de estar
    '''
    if not dato_heroe:
        return valor_defecto
    
    return dato_heroe





def normalizar_heroe(diccionario_heroe:dict, clave_diccionario_heroe:str) -> dict:
    '''
    capitaliza y normaliza el contenido de diccionario_heroe[clave_diccionario_heroe] y capitaliza el nombre del heroe
    Recibe: un diccionario que representa a un heroe y una clave en el diccionario 
    Retorna: el diccionaro con las modificaciones pertinentes
    '''


    # para el valor
    valor_salida = capitalizar_palabras(diccionario_heroe[clave_diccionario_heroe])
    valor_salida = normalizar_dato(valor_salida, "N/A")
    diccionario_heroe[clave_diccionario_heroe] = valor_salida

    # para el nombre
    nombre_capitalizado = capitalizar_palabras(diccionario_heroe["nombre"])
    diccionario_heroe["nombre"] = nombre_capitalizado

    return diccionario_heroe


def obtener_heroes_por_tipo(lista_heroes:list[dict], set_variedades:set[str], clave_evaluada:str) ->dict[list[str]] :
    '''
    Genera un diccionario con distintas listas de nombres que coincidan con una caracteristica evaluada
    Recibe: una lista de heroes, el set de variedades que puede tener la clave evaluada y la clave evaluada
    Retorna: un diccionario de listas de nombres de las coincidencias
    '''

   
    diccionario_salida = {} # creo el diccionario de salida

    for variedad in set_variedades: # A. itero el set de variedades
        if variedad not in diccionario_salida: # B. si la variedad no esta en el diccionario, se le genera un lista vacia correspondiente
            diccionario_salida[variedad] = []

        for heroe in lista_heroes: # C. con un for anidado itero la lista de heroes y normalizo datos
            heroe = normalizar_heroe(heroe, clave_evaluada)

            if diccionario_coincidencia(heroe,clave_evaluada,variedad): # D. Verifico coincidencia
                nombre_heroe = heroe["nombre"]

                diccionario_salida[variedad].append(capitalizar_palabras(nombre_heroe)) # E. Lo agrega a a la lista correspondiente

    return diccionario_salida





def guardar_heroes_por_tipo(diccionario_listas_coincidentes:dict[list[str]], clave_evaluada:str) -> bool:
    '''
    Guarda diccionario_listas_coincidentes en un archivo y muestra sus datos por pantalla
    Recibe: el diccionario con las listas y un string que ayudara a nombrar el archivo a guardar
    Retorna: True o False
    
    '''

    cadena_archivo_formateada = ""
    for clave_lista_coincidentes, valor_lista_coincidentes in diccionario_listas_coincidentes.items():
        
        # se formatea la lista de coincidencias
        cadena_coincidencias_formateadas = ""
        for coincidencia in valor_lista_coincidentes:
            if cadena_coincidencias_formateadas:
                cadena_coincidencias_formateadas += " | " + coincidencia
            else: 
                cadena_coincidencias_formateadas = coincidencia # primera iteracion no incluye el separador 

        # se muestra la lista de coincidencias formateadas
        cadena_salida = f'{clave_evaluada} {clave_lista_coincidentes}: {cadena_coincidencias_formateadas}'
        print(cadena_salida)

        # se formatea la cadena del archivo
        if cadena_archivo_formateada:
            cadena_archivo_formateada += "\n" + cadena_salida
        else: 
            cadena_archivo_formateada = cadena_salida # primera iteracion no incluye el separador 
        


    nombre_archivo = f'heroes_segun_{clave_evaluada}.csv'
    return guardar_archivo(nombre_archivo, cadena_archivo_formateada)




def stark_listar_heroes_por_dato(lista_heroes:list[dict], clave_evaluada:str) -> bool:
    '''
    
    '''
    # A.
    set_tipos = obtener_lista_de_tipos(lista_heroes, clave_evaluada)


    # B.
    diccionario_listas = obtener_heroes_por_tipo(lista_heroes, set_tipos, clave_evaluada)

    # C.
    return guardar_heroes_por_tipo(diccionario_listas, clave_evaluada)


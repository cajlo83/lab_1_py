from typing import Union #importo funciones que asisten con la documentacion
from stark_sub_biblioteca import *
import re



def extraer_iniciales(nombre_heroe:str) -> str:
    '''
    Recibe: un str que representa un nombre
    evalua que la cadena no este vacia, elimina la cadena " the " y "-", extrae sus iniciales en mayusculas.
    retorna: un str que representa las iniciales de nombre_heroe o 'N/A' en caso de error

    '''
    
    #Se niega el valor de nombre_heroe para obtener un booleano que represente verdadero o falso y determinar si esta vacio
    if not nombre_heroe:
        return 'N/A'
    

    nombre_heroe = nombre_heroe.replace(" the "," ") # reemplazar " the " con " "
    nombre_heroe = nombre_heroe.replace("-","") # reemplazar "-" con ""
    lista_palabras = nombre_heroe.split() # Dividir el nombre en palabras y guardarlos en una lista de str 
    iniciales = [] # lista de iniciales

    
    #se itera la lista para guardar solo la primera letra de cada palabra en mayuscula, y se guarda en la lista de iniciales
    for palabra in lista_palabras:
        inicial  = palabra[0].upper()
        iniciales.append(inicial)


    iniciales = ".".join(iniciales) + "." # colocar un "." luego de cada inicial y guardarlo en formato str

    return iniciales




def definir_iniciales_nombre(heroe:dict) -> bool:
    '''
    Recibe: un diccionario que representa un heroe
    verifica que el parametro recibido sea un diccionario conteniendo la clave 'nombre', genera las iniciales correspondientes y guarda la clave: valor en el diccionario recibido
    Retorna: True en caso de exito, False en caso de error
    '''

    # se valida que heroe es un diccionario que contenga la clave 'nombre', sino retorna false
    if not isinstance(heroe, dict) or 'nombre' not in heroe:
        return False

    iniciales = extraer_iniciales(heroe['nombre']) # recibo las iniciales
    heroe['iniciales'] = iniciales # agrego la nueva clave al diccionario
    
    return True




def agregar_iniciales_nombre(lista_heroes:list[dict]) -> bool:
    '''
    Recibe: una lista de diccionarios, cada diccionario debe representar un heroe
    valida que lista_heroes sea una lista que no este vacia, recorre los diccionarios que contiene y le asigna las iniciales a cada heroe
    Retorna: True en caso de haber finalizado con éxito o False en caso de que haya ocurrido un error
    '''

    # se valida que lista_heroes sea una lista que no este vacia
    if not valida_lista(lista_heroes):
        return False

    # itera la lista de heroes asignando iniciales a cada uno. aprovecha el retorno de definir_iniciales_nombre() para determinar si hay que salir del bucle
    for heroe in lista_heroes:
        if not definir_iniciales_nombre(heroe):
            print('El origen de datos no contiene el formato correcto')
            return False

    return True # retorna True en caso de no haber problemas




def stark_imprimir_nombres_con_iniciales(lista_heroes: list[dict]):
    '''
    Recibe: la lista de heroes
    imprime personajes con el sigueinte formato: "* Howard the Duck (H.D.)"
    Retorno: None
    '''

    # se evalua que lista_heroes sea del tipo lista, que la lista no este vacia y que haya exito agregando las iniciales en los diccionarios. 
    if not valida_lista(lista_heroes) or not agregar_iniciales_nombre(lista_heroes):
        return # None implicito


    # Se itera la lista imprimiendo los datos con el formato requerido 
    for heroe in lista_heroes:
        print(f"* {heroe['nombre']} ({heroe['iniciales']})")




def generar_codigo_heroe(id_heroe:int, genero_heroe:str) -> str:
    '''
    Recibe: un numero entero y un str que puede ser "M", "F" o "NB".
    valida el contenido de los argumentos recibidos y los organiza en formato:
        F-00000001\n
        M-00000002\n
        NB-0000010
    retorna: "N/A" o un string con un formato previamente indicado.
    '''
    

    # verifica que id_heroe sea un numero entero y que se haya indicado un genero valido, sino se retorna con 'N/A'
    if not isinstance(id_heroe, int) or genero_heroe not in ('M', 'F', 'NB'):
        return 'N/A'
    

    # se calcula el parametro para zfill segun el genero_heroe
    if genero_heroe == "NB": 
        cantidad_relleno = 7
    else: 
        cantidad_relleno = 8

    # se da formato a la cadena y se retorna 
    codigo = f"{genero_heroe}-{str(id_heroe).zfill(cantidad_relleno)}"
    return codigo




def agregar_codigo_heroe(heroe:dict, id_heroe:int) -> bool:
    '''
    Recibe: un diccionario que representa a un heroe y su numero de ID.
    Valida que el diccionario no este vacio. Obtiene un codigo de heroe y valida que cumpla con una longitud de 10 caracteres.
    Retorna: False en caso de no pasar las validaciones, True en caso que si.
    '''
    # se recibe el codigo y se verifica que cumpla con los parametros correspondientes
    codigo = generar_codigo_heroe(id_heroe, heroe['genero'])
    if codigo == 'N/A' or len(codigo) != 10:
        return False


    # se valida que heroe sea un diccionario y que no este vacio
    if not isinstance(heroe, dict) or heroe == {}:
        return False

    # se asigna clave: valor al diccionario
    heroe['codigo_heroe'] = codigo
    return True





def stark_generar_codigos_heroes(lista_heroes: list[dict]):
    '''
    Recibe: una lista de heroes
    valida que lista_heroes sea una lista no vacia. Genera un codigo segun el genero y la posicion del heroe en la lista y lo guarda en su diccionario correspondiente
    Retorno: None
    '''


    # valido que lista_heroes sea una lista no vacia
    if not valida_lista(lista_heroes):
        return
    
    id = 1  # se controla el numero de ID que inicia en 1

    for heroe in lista_heroes:
        if not agregar_codigo_heroe(heroe, id):
            return
        id += 1  # se incrementa el numero de ID en cada repeticion

    # se imprimen la informacion al usuario
    print(f"Se asignaron {len(lista_heroes)} códigos")
    print(f"* El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}")
    print(f"* El código del último héroe es: {lista_heroes[-1]['codigo_heroe']}") # al colocar -1 se busca la primera posicion desde el final de la lista




def sanitizar_entero(numero_str:str) -> int():
    '''
    Recibe: una cadena que se espera represente un entero positivo para retornarlo
    Retorna: 
        Si contiene carácteres no numéricos retornar -1
        Si el número es negativo se deberá retornar un -2
        Si ocurren otros errores que no permiten convertirlo a entero entonces se deberá retornar -3
    '''

    # se verifica que numero_str sea una cadena de caracteres no vacia
    if not isinstance(numero_str, str) or numero_str == "":
        return -3

    #se verifica que la cadena efectivamente solo contenga caracteres que puedan representar a un numero entero
    if verificar_numero_entero(numero_str):
        num_retorno = int(numero_str)
    else:
        return -1

    # se filtra que no sea un entero negativo
    if num_retorno < 0:
        return -2

    return num_retorno





def sanitizar_flotante(numero_str:str) -> Union[int, float]:
    '''
    Recibe: una cadena que se espera represente un entero positivo para retornarlo
    Retorna: 
        int:
            Si contiene carácteres no numéricos retornar -1.
            Si el número es negativo se deberá retornar un -2.
            Si ocurren otros errores que no permiten convertirlo a flotante entonces se deberá retornar -3.
        float: el numero casteado en caso de pasar las validaciones.
    '''

    # se verifica que numero_str no sea una cadena de caracteres no vacia
    if not isinstance(numero_str, str) or numero_str == "":
        return -3
    
    # se verifica que la cadena efectivamente solo contenga caracteres que puedan representar a un numero flotante
    if verificar_numero_flotante(numero_str):
        num_retorno = float(numero_str)
    else:
        return -1

    # se filtra que no sea un flotante negativo
    if num_retorno < 0:
        return -2

    return num_retorno




def sanitizar_string(valor_str:str, valor_por_defecto:str = '-') -> str:
    '''
   Recibe: una cadena que se espera represente solo texto y tal vez caracteres de espacio (' ') y un parametro opcional (inicialmente: valor_por_defecto = '-')
   verifica que valor_str represente una cadanea con caracteres alfabeticos y/o espacios ' '. 
   Si se encuentra un '/' lo reemplaza con ' '. 
   Elimina los espacios ' ' a los extremos de la cadena
   Retorna: 
    valor_str en minusculas.
    valor_por_defecto en minusculas en caso de haberse recibido y valor_str == "".
    '''

    # se verifica que la cadena no este vacia y sus posibles retornos, tambien si la cadena esta vacia se retorna 'N/A', mismo resultado que retornaria luego de pasar los filtros siguientes
    if valor_str == "":
        if valor_por_defecto != '-':
            return valor_por_defecto.lower()
        
        return 'N/A'

    # valido que no hayan caracteres numericos en valor_str
    lista_numeros = re.findall("[0-9]",valor_str)
    if len(lista_numeros) > 0:
        return 'N/A'
    
    #verifico si hay caracteres '/' y se reemplazan por ' 'en caso de si haber
    if '/' in valor_str:
        valor_str = valor_str.replace('/', ' ')
    
    # se eliminan espacios a los lados 
    valor_str = valor_str.strip()

    # como el espacio es un caracter valido, se filtra antes de chequear los caracteres invalidos conm isalpha()
    cadena_sin_espacios = valor_str.replace(' ', '')
    if not cadena_sin_espacios.isalpha():
        return 'N/A'

    return valor_str




def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str) -> bool:
    '''
    Recibe:
        ● heroe: un diccionario con los datos del personaje
        ● clave: un string que representa el dato a sanitizar (la clave del diccionario). Por ejemplo altura (distingue mayusculas y minusculas)
        ● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede tomar los valores: ‘STRING’, ‘ENTERO’ o ‘FLOTANTE’ (no distingue mayusculas o minusculas)

    Verifica el contenido de la heroe[clave] y lo sanitiza segun tipo_dato

    Retorna: 
        True en caso de hacer un cambio. False en caso de no hacerlo
    '''

    # se verifica que el diccionario heroe tenga la clave buscada, debe estar perfectamente escrito
    if clave not in heroe:
        print('La clave especificada no existe en el héroe')
        return False

    valor = heroe[clave] # se evita la posibilidad de acceder y modificar heroe[clave] en un momento inconveniente o mantener su valor original en caso de error

    # se pasa el texto de tipo_dato a mayusculas y se verifica su coincidencia por medio de un match
    tipo_dato = tipo_dato.upper()
    match tipo_dato:
        case "STRING":
            heroe[clave] = sanitizar_string(valor)

        case "ENTERO":
            bandera_entero = sanitizar_entero(valor)
            if bandera_entero < 0:
                return False
            heroe[clave] = bandera_entero

        case "FLOTANTE":
            bandera_flotante = sanitizar_flotante(valor)
            if bandera_flotante < 0:
                return False
            heroe[clave] = bandera_flotante

        case _:
            print('Tipo de dato no reconocido')
            return False

    return True





def stark_normalizar_datos(lista_heroes:list[dict]):
    '''
    Recibe: 
        lista_heroes: la listas personajes
        recorre la lista de héroes y sanitizar los valores solo de las siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e ‘inteligencia’
    Retorna: None
    '''

    # Se verifica que se reciba una lista no vacia
    if not valida_lista(lista_heroes) :
        print("Error: Lista de héroes vacía")
        return

    # Se itera la lista de diccionarios y se sanitizan sus claves
    for heroe in lista_heroes:
        sanitizar_dato(heroe, 'altura', 'flotante')
        sanitizar_dato(heroe, 'peso', 'flotante')
        sanitizar_dato(heroe, 'color_ojos', 'string')
        sanitizar_dato(heroe, 'color_pelo', 'string')
        sanitizar_dato(heroe, 'fuerza', 'entero')
        sanitizar_dato(heroe, 'inteligencia', 'string')

    print('Datos normalizados')




def generar_indice_nombres(lista_heroes:list[dict]) -> list[str]:
    '''
    Recibe una lista de diccionarios
    verifica que la lista no este vacia y que cada uno de sus elementos sean diccionarios con la clave 'nombre'
    Retorna: una lista de palabras de nombres, o una lista vacia
    '''


    #valido que la lista cumpla los parametros
    if not valida_lista(lista_heroes):
        return []

    # itera la lista verificando que cada elemento sea un diccionario con la clave 'nombre'
    nombres = []
    for heroe in lista_heroes:
        if isinstance(heroe, dict) and 'nombre' in heroe:

            # con re.split se arma una lista de palabras del nombre actual evaluandose. con nombres.extend se guarda en la lista general de palabras de nombre
            nombres.extend(re.split("\s+",heroe['nombre']))
        else:
            print("El origen de datos no contiene el formato correcto")
            return []
            

    return nombres




def stark_imprimir_indice_nombre(lista_heroes:list[dict]):
    '''
    imprime las palabras de los nombres de los heroes separado por guiones '-'
    '''
    nombres = generar_indice_nombres(lista_heroes)
    if valida_lista(nombres): 
        indice = '-'.join(nombres) # se guarda las palabras de nombres separadas por '-' en la varaible indice y se imprime
        print(indice)





def convertir_cm_a_mtrs(valor_cm:float) -> float:
    '''
    Recibe: valor_cm que deberá ser un flotante mayor que 0
    Retorna: el valor de los cm convertido a m; o -1 en caso de no pasar la validacion
    '''
    # se valida el formato
    if not isinstance(valor_cm, (int, float)) or valor_cm < 0:
        return -1

    return float(valor_cm / 100)




def generar_separador(patron:str, largo:int, imprimir:bool=True) -> str:
    '''
    recibe:
        ● patron: un carácter que se utilizará como patrón para generar el separador.
        ● largo: un número que representa la cantidad de caracteres que va ocupar el separador.
        ● imprimir: un parámetro opcional del tipo booleano (por default definir en True).
    retorna: un str compuesto por el contenido de patron repetido tantas veces como largo lo indique.
    si imprimir == true: imprime el str generado

    '''

    #se verifica que patron y largo tengan el formato y la dimension que nos interesa
    if not (isinstance(patron, str) and 1 <= len(patron) <= 2) or not (isinstance(largo, int) and 1 <= largo <= 235):
        return 'N/A'

    separador = patron * largo

    if imprimir:
        print(separador)

    return separador




def generar_encabezado(titulo:str):
    '''
    Recibe: 
        titulo str que sera el titulo del encabezado
    retorna un str con el sigueinte formato:
    ************************************************************
    TITULO
    ************************************************************
    
    '''
    titulo_mayus = titulo.upper()
    separador = generar_separador('*', 20, False)
    #encabezado = separador + "\n"
    encabezado = f"{separador}\n{titulo_mayus}\n{separador}"

    
    '''
    # esta version saca el encabezado centrado

    separador = generar_separador('*', len(titulo)*3)
    encabezado = f"{separador}\n{' '*len(titulo)}{titulo.upper()}\n{separador}" 
    '''

    return encabezado




def imprimir_ficha_heroe(heroe:dict):
    '''
    imprime los datos del heroe:dict recibido en formato de ficha
    '''

    #verifico que heroe sea un diccionario
    if not isinstance(heroe, dict):
        return

    # genero los encabezados
    encabezado_principal = generar_encabezado("Principal")
    encabezado_fisico = generar_encabezado("Fisico")
    encabezado_senas_particulares = generar_encabezado("Señas Particulares")

    # PRINCIPAL
    print(encabezado_principal)

    print(f"NOMBRE DEL HÉROE: {heroe['nombre']} ({heroe.get('iniciales', 'No disponibles')})")
    print(f"IDENTIDAD SECRETA: {heroe.get('identidad', '')}")
    print(f"CONSULTORA: {heroe.get('empresa', '')}")
    print(f"CÓDIGO DE HÉROE : {heroe.get('codigo_heroe', 'No disponibles')}")
    
    # FISICO
    print(encabezado_fisico)
    print(f"ALTURA: {convertir_cm_a_mtrs(heroe.get('altura', 0)):0.2f} Mtrs.")
    #peso=heroe.get('peso', 0):0.2f
    print(f"PESO: {heroe.get('peso', 0):0.2f} Kg.")
    print(f"FUERZA: {heroe.get('fuerza', 0)} N")

    # SEÑAS PARTICULARES
    print(encabezado_senas_particulares)
    print(f"COLOR DE OJOS: {heroe['color_ojos']}")
    print(f"COLOR DE PELO: {heroe['color_pelo']}")




def stark_navegar_fichas(lista_heroes:list[dict]):
    '''
    Navega las fichas de los heroes
    '''

    # valida que lista_heroes sea una lista no vacia
    if not valida_lista(lista_heroes):
        return

    # calculo el largo de la lista para control de la misma
    total_heroes = len(lista_heroes)

    # con un bucle y la variable posicion se controla la navegacion entre fichas
    posicion = 0
    while True:

        # se castea el elemento de la lista a heroe actual para conveniencia al acceder a su info
        heroe_actual = lista_heroes[posicion]
        imprimir_ficha_heroe(heroe_actual)

        opciones = "[ 1 ] Ir a la izquierda\t[ 2 ] Ir a la derecha\t[ S ] Salir"
        entrada = input(f"\n{opciones}: ")


        match entrada:
            case '1':
                posicion -= 1
                if posicion < 0: # posicion minima
                    posicion = 0

            case '2':
                posicion += 1
                if posicion > total_heroes - 1: # posicion maxima
                    posicion = total_heroes - 1

            case 'S' | 's':# salida
                break




def imprimir_menu():
    '''
    imprime el menu
    '''
    menu = """
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
    """
    print(menu)




def stark_menu_principal():
    '''
    Genera la interaccion entre el usuario y la maquina a travez del menu
    '''
    while True:
        imprimir_menu()
        entrada = input("Seleccione una opción: ")
        return entrada




def stark_marvel_app_3(lista_heroes:list[dict]):
    '''
    Recibe: la lista de personajes
    ejecuta el codigo constantemente hasta que se envie el comando de salida
    '''
    if not valida_lista(lista_heroes):
        print("No se recibio correctamente lista_personajes desde data_stark.py o la lista esta vacia")
        return


    bandera_normalizacion = False
    bandera_iniciales = False
    bandera_codigos = False
    while True:
        opcion = stark_menu_principal()

        match opcion:
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

            case 's' | 'S':
                break

            case _:
                print("Opcion incorrecta, reintente")






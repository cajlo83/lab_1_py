

def verificar_numero_entero(cadena_entrada:str)->bool: 
    '''
    Verifica si los caracteres de cadena_entrada corresponden a un numero entero (positivo o negativo)
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos lstrip y isdigit se verifica si el string corresponde o no a un entero
    validar_numero_no_decimal = lambda x: (True) if x.strip('-').isdigit() else (False)

    retorno = validar_numero_no_decimal(cadena_entrada)

    return retorno


def verificar_numero_flotante(cadena_entrada:str)->bool:
    '''
    Verifica si cadena_entrada corresponde a un numero flotante
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos replace,lstrip y isdigit se verifica si el string corresponde o no a un flotante
    validar_numero_decimal = lambda x: (True) if x.replace('.', '', 1).strip('-').isdigit() else (False)

    retorno = validar_numero_decimal(cadena_entrada)

    return retorno


def valida_lista(lista:list, len_lista:int=0):
    '''
    Recibe una variable que se validara que sea una lista cuya longitud sea mayor que len_lista (parametro opcional, por defecto= 0)
    Retorna: True o False
    '''

    if isinstance(lista, list) and len(lista) > len_lista:
        return True
    return False

def obtener_dato_diccionario(diccionario:dict, clave:str) -> str:
    '''
    retorna el valor de diccionario[clave] en formato "clave: valor"
    '''

        # para la clave
    clave_solicitada = diccionario.get(clave, '?')
    return f'{clave.capitalize()}: {clave_solicitada}'
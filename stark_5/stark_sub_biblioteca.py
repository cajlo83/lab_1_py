from typing import Union
import os



def verificar_numero_entero(cadena_entrada:str)->bool: 
    '''
    Verifica si los caracteres de cadena_entrada corresponden a un numero entero (positivo o negativo)
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos lstrip y isdigit se verifica si el string corresponde o no a un entero
    validar_numero_no_decimal = lambda x: (True) if x.strip('-').isdigit() else (False)

    retorno = validar_numero_no_decimal(cadena_entrada)

    return retorno




def imprimir_dato(dato):
    '''
    Funcion redundante que imprime un dato
    '''
    print(dato)



def verificar_numero_flotante(cadena_entrada:str)->bool:
    '''
    Verifica si cadena_entrada corresponde a un numero flotante
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos replace,lstrip y isdigit se verifica si el string corresponde o no a un flotante
    validar_numero_decimal = lambda x: (True) if x.replace('.', '', 1).strip('-').isdigit() else (False)

    retorno = validar_numero_decimal(cadena_entrada)

    return retorno


def valida_lista(lista:list, len_lista:int=0, de_caracteres:bool = False) -> bool:
    '''
    Recibe una variable que se validara que sea una lista cuya longitud sea mayor que len_lista (parametro opcional, por defecto= 0). de_caracteres es una alternativa para validar listas de caracteres(strings)
    Retorna: True o False
    '''
    if de_caracteres: #valida strings
        return isinstance(lista, str) and len(lista) > len_lista
    return isinstance(lista, list) and len(lista) > len_lista
    
    

def obtener_dato_diccionario(diccionario:dict, clave:str) -> str:
    '''
    retorna el valor de diccionario[clave] en formato "clave: valor"
    '''

        # para la clave
    clave_solicitada = diccionario.get(clave, '?')
    
    if verificar_numero_flotante(clave_solicitada): # se da un formato conveniente para valores flotantes
        clave_solicitada = float(clave_solicitada)
        cadena_retorno = f'{clave.capitalize()}: {clave_solicitada:.2f}'

    else:
        cadena_retorno = f'{clave.capitalize()}: {clave_solicitada}'


    return cadena_retorno



def diccionario_coincidencia(diccionario:dict,clave:str,valor) -> bool:
    '''
    recibe: un diccionario, una clave y un valor
    verifica que diccionario[clave] == valor
    Retorna: True o False
    '''

    return clave in diccionario and diccionario[clave] == valor
         

def dividir(divisor:Union[int,float], dividendo:Union[int,float]) -> Union[float,bool]: 
    '''
    verificar si el divisor es 0, en caso de serlo, retornar False, caso contrario realizar la división entre los parámetros y retornar el resultado
    '''

    #si el dividendo es 0, retorna False
    if dividendo == 0:
        return False
    
    return divisor/dividendo



def lista_diccionarios_contar_coincidencias(lista_diccionarios:list[dict],clave_lista:str)->dict:
    '''
    verifica los elementos en lista_diccionarios para ver cuantos tipos de clave_lista hay y contar sus repeticiones.
    Retorna: un diccionario de contadores con los distintos valores en la clave buscada y sus repeticiones.
    '''

    diccionario_final ={}
    #bucle para recorrer la lista, diccionario por diccionario
    for diccionario in lista_diccionarios:
        if valida_lista(diccionario[clave_lista], de_caracteres=True): # verifica que el valor de la clave en evaluacion sea un string no vacio
            valor_lista = diccionario[clave_lista] # guardo el string no vacio que pasara a ser una clave del diccionario de contadores a crear
            clave_diccionario = capitalizar_palabras(valor_lista)

            # verifico si el elemento clave_diccionario pertenece a diccionario_final. suma 1 a un contador si existe, inicializa otro contador en 1 si no existe
            if clave_diccionario in diccionario_final:
                diccionario_final[clave_diccionario] += 1
            else:
                diccionario_final[clave_diccionario] = 1

    # retorno el diccionario con resultados
    return diccionario_final






def lista_diccionarios_contar_coincidencias_inclusivo(lista_diccionarios:list[dict], clave_lista:str)->dict:
    '''
    verifica los elementos en lista_diccionarios para ver cuantos tipos de clave_lista hay y contar sus repeticiones.
    Retorna: un diccionario de contadores con los distintos valores en la clave buscada y sus repeticiones.
    '''

    diccionario_final ={}
    #bucle para recorrer la lista, diccionario por diccionario
    for diccionario in lista_diccionarios:
        if valida_lista(diccionario[clave_lista], de_caracteres=True): # verifica que el valor de la clave en evaluacion sea un string no vacio
            valor_lista = diccionario[clave_lista] # guardo el string no vacio que pasara a ser una clave del diccionario de contadores a crear
            clave_diccionario = capitalizar_palabras(valor_lista)

        else: # como alternativa se configura como "NO DATA" en caso de recibirse un dato vacio para contarlos con una palabra "no vacia"
            clave_diccionario ="No Tiene" 

        # verifico si el elemento clave_diccionario pertenece a diccionario_final. suma 1 a un contador si existe, inicializa otro contador en 1 si no existe
        if clave_diccionario in diccionario_final:
            diccionario_final[clave_diccionario] += 1
        else:
            diccionario_final[clave_diccionario] = 1

    # retorno el diccionario con resultados
    return diccionario_final



def capitalizar_palabras(palabra:str) -> str:
    '''
    capitaliza la cadena recibida en palabra
    '''

    return palabra.capitalize()


def armar_directorio_stark_5(nombre_archivo:str) -> str:
    directorio_trabajo = os.getcwd()
    directorio_archivo = f'{directorio_trabajo}\lab_1_py\stark_5\{nombre_archivo}'
    return directorio_archivo
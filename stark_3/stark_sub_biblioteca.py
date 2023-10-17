def verificar_numero_real(cadena_entrada:str)->bool:
    '''
    Verifica si cadena_entrada corresponde a un numero real
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos replace,lstrip y isdigit se verifica si el string corresponde o no a un flotante
    validar_numero_decimal = lambda x: (True) if x.replace('.', '', 1).lstrip('-').isdigit() else (False)

    retorno = validar_numero_decimal(cadena_entrada)

    return retorno

#se implemento esta funcion antes de que se me solicitara hacer “validar_entero”, esta si valida numeros negativos
def verificar_numero_entero(cadena_entrada:str)->bool: 
    '''
    Verifica si cadena_entrada corresponde a un numero entero
    Retorna: True o False
    '''

    #con una funcion lambda y los metodos lstrip y isdigit se verifica si el string corresponde o no a un entero
    validar_numero_no_decimal = lambda x: (True) if x.lstrip('-').isdigit() else (False)

    retorno = validar_numero_no_decimal(cadena_entrada)

    return retorno




def diccionario_coincidencia(diccionario:dict,clave:str,valor) -> bool:
    '''
    verifica que diccionario[clave] == valor
    Retorna: True o False
    '''

    return clave in diccionario and diccionario[clave] == valor
         






def lista_diccionarios_buscar_coincidencias(lista_diccionarios:list[dict],clave:str,valor)->list[dict]:
    '''
    Recorre "lista_diccionarios" buscando una "clave" coincidente con "valor".
    Agrega al diccionario coincidencte a lista_final
    Retorna lista_final, si no hubo ningun dato retorna una lista sin elementos.
    '''
    lista_final = []
    
    for diccionario in lista_diccionarios:
        if diccionario_coincidencia(diccionario,clave, valor):
            lista_final.append(diccionario)
    
    return lista_final




def lista_diccionarios_imprimir_clave(lista_diccionarios:list[dict],clave:str)->bool:
    '''
    Muestra el valor de las claves correspondientes en lista_diccionarios si corresponde
    Retorna: True en caso de imprimir datos. False en caso de no imprimir datos

    '''
    retorno = False
    if (len(lista_diccionarios) > 0):
        for diccionario in lista_diccionarios:
            print(diccionario[clave])
        
        retorno = True

    
    return retorno





def lista_diccionarios_listar_coincidencias(lista_diccionarios:list[dict], clave:str) -> list[str]:
    '''
    Recibe una lista de diccionarios y una clave que debe estar en los mismos
    recorre lista_diccionarios generando una lista de los distintos valores que existen, sin repeticiones (no es un set)
    Retorna: una lista de las distintos posibles valores que tienen dichas claves
    '''
    lista_salida = []
    for diccionario in lista_diccionarios: # recorro la lista
        valor_clave = diccionario[clave] # extraigo el valor
        if valor_clave == "": # evaluo data
            valor_clave = "NO DATA"
        else:
            valor_clave = valor_clave.upper() # se cambia a mayuscula para casos de repeticiones

        if valor_clave not in lista_salida: # si el valor aun no esta en la lista, se agrega 
            lista_salida.append(valor_clave)

    return lista_salida





def lista_diccionarios_contar_coincidencias(lista_diccionarios:list[dict],clave_lista:str)->dict:
    '''
    verifica los elementos en lista_diccionarios para ver cuantos tipos de clave_lista hay y contar sus repeticiones.
    Retorna: un diccionario de contadores con los distintos valores en la clave buscada y sus repeticiones.
    '''

    diccionario_final ={}
    #bucle para recorrer la lista diccionario por diccionario
    for diccionario in lista_diccionarios:
        if diccionario[clave_lista] != "": # verifica que el valor de la clave en evaluacion no sea un string vacio
            valor_lista = diccionario[clave_lista] # guardo el string no vacio que pasara a ser una clave del diccionario de contadores a crear
            clave_diccionario = valor_lista.upper()

        else:
            clave_diccionario ="NO DATA" #como alternativa se configuro como "no data" en caso de recibirse un dato vacio

        #verifico si el elemento clave_diccionario pertenece a diccionario_final. suma 1 a un contador si existe, inicializa otro contador en 1 si no existe
        if clave_diccionario in diccionario_final:
            diccionario_final[clave_diccionario] += 1
        else:
            diccionario_final[clave_diccionario] = 1

    #retorno el diccionario con resultados
    return diccionario_final





def imprimir_diccionario(diccionario:dict)->bool:
    '''
    Recibe un diccionario para imprimirlo en el formato clave: valor
    Retorno: True en caso de imprimir, False de no mostrar nada
    '''

    retorno = False
    if(len(diccionario) > 0):
        #imprimo resultados con un bucle y el metodo .items() para facilitar la interaccion clave:valor
        for clave, valor in diccionario.items():
                print(f"{clave}: {valor}")
        retorno = True

    
    return retorno




def lista_diccionarios_sorted(lista_diccionarios:list[dict],clave:str)->list[dict]:
    '''
    recibe lista_diccionarios para ordenarla segun lo indicado en clave
    Retorna: una copia de la lista original, pero organizada
    '''
    
    lista_final = sorted(lista_diccionarios, key=lambda x: x[clave])

    return lista_final


    
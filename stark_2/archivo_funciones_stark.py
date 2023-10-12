
def lista_diccionarios_buscar_coincidencias(lista_diccionarios:list[dict],clave:str,valor)->list[dict]:
    '''
    Recorre "lista_diccionarios" buscando una "clave" coincidente con "valor".
    Agrega al diccionario coincidencte a lista_final
    Retorna lista_final, si no hubo ningun dato retorna una lista sin elementos.
    '''
    lista_final = []
    
    for diccionario in lista_diccionarios:
        if clave in diccionario and diccionario[clave] == valor:
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



def lista_diccionarios_mayor_valor_numerico(lista_diccionarios:list[dict],clave_numerica:str)->list[dict]:
    '''
    Recorre cada diccionario en lista_diccionarios evaluando si el valor de "clave_numerica" es numerico.
    Si es numerico interactua con lista_final verificando mayor valor, si no es numerico pasa al siguiente.
    Retorna lista_final, si no hubo ningun dato retorna una lista sin elementos.
    '''
    lista_final = []

    bandera_primera = True
    
    for diccionario in lista_diccionarios:
        #se verifica que el valor represente a un numero real
        if(verificar_numero_real(diccionario[clave_numerica])):
            #primera comparacion de valores numericos con una bandera
            if (bandera_primera):
                bandera_primera = False
                numero_mayor = float(diccionario[clave_numerica])
                lista_final.append(diccionario)

            elif (numero_mayor < float(diccionario[clave_numerica])):
                numero_mayor = float(diccionario[clave_numerica])
                lista_final = []
                lista_final.append(diccionario)

            elif (numero_mayor == float(diccionario[clave_numerica])):
                lista_final.append(diccionario)

    return lista_final




def lista_diccionarios_menor_valor_numerico(lista_diccionarios:list[dict],clave_numerica:str)->list[dict]:
    '''
    Recorre cada diccionario en lista_diccionarios evaluando si el valor de "clave_numerica" es numerico.
    Si es numerico interactua con lista_final verificando menor valor, si no es numerico pasa al siguiente.
    Retorna lista_final, si no hubo ningun dato retorna una lista sin elementos.
    '''
    lista_final = []

    bandera_primera = True
    
    for diccionario in lista_diccionarios:

        #se verifica que el valor represente a un numero real
        if(verificar_numero_real(diccionario[clave_numerica])):

            #primera comparacion de valores numericos con una bandera
            if (bandera_primera):
                bandera_primera = False
                numero_menor = float(diccionario[clave_numerica])
                lista_final.append(diccionario)

            elif (numero_menor > float(diccionario[clave_numerica])):
                numero_menor = float(diccionario[clave_numerica])
                lista_final = []
                lista_final.append(diccionario)

            elif (numero_menor == float(diccionario[clave_numerica])):
                lista_final.append(diccionario)
                
       

    return lista_final




def lista_diccionarios_validacion_valor_numerico(lista_diccionarios:list[dict],clave_numerica:str)->list[dict]:
    '''
    Recorre cada diccionario en lista_diccionarios evaluando si el valor de "clave_numerica" es numerico.
    Si es numerico se agrega a lista_final, sino pasa al siguiente.
    Retorna lista_final.
    '''
    lista_final = []
    
    for diccionario in lista_diccionarios:

        #se verifica que el valor represente a un numero real y lo guarda en la lista de salida
        if(verificar_numero_real(diccionario[clave_numerica])):
            lista_final.append(diccionario)
       

    return lista_final




def lista_diccionarios_calcular_promedio(lista_diccionarios:list[dict],clave_numerica:str)->float:
    '''
    verifica que hayan elementos en lista_diccionarios para calcular el promedio de la clave_numerica indicada.
    Retorna: promedio en caso de que los datos esten bien, None en caso de error.
    '''
    #se verifica que el valor de cada clave_numerica represente a un numero real y lo guarda en lista_final
    lista_final = lista_diccionarios_validacion_valor_numerico(lista_diccionarios,clave_numerica)
    
    #una vez que se verifica el tipo de dato correcto, se declaran variables y se hacen los calculos
    acumulador = 0
    len_lista = len(lista_final)
    if (len_lista > 0):
        for diccionario in lista_final:
            acumulador += float(diccionario[clave_numerica])
        
        #promedio = acumulador / cantidad de datos que se acumularon
        promedio = acumulador / len_lista
    else:
        promedio = None
    
    return promedio





def lista_diccionarios_contar_coincidencias(lista_diccionarios:list[dict],clave_lista:str)->dict:
    '''
    verifica los elementos en lista_diccionarios para ver cuantos tipos de clave_lista hay y contar sus repeticiones.
    Retorna: un diccionario con los distintos valores en la clave buscada y sus repeticiones.
    '''

    diccionario_final ={}
    #bucle para recorrer la lista
    for diccionario in lista_diccionarios:
        clave_diccionario = diccionario[clave_lista]

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


    

def lista_diccionarios_imprimir_nombres_organizados(lista_diccionarios:list[dict],clave:str)->bool:
    '''
    recibe una lista de diccionarios la cual va a imprimir una clave tipo "nombre" y otro dato relevante indicado en la variable clave
    Retorno: True en caso de imprimir, False en caso que no
    '''
    retorno = False
    if (len(lista_diccionarios) > 0):
        for personaje in lista_diccionarios: 
            print("{0} \t {1}".format(personaje["nombre"], personaje[clave]))
        retorno = True
    return retorno




def verificar_numero_real(cadena_entrada:str)->bool:
    '''
    Verifica si cadena_entrada corresponde a un numero real
    Retorna: True o False
    '''

    
    validar_numero_decimal = lambda x: (True) if x.replace('.', '', 1).lstrip('-').isdigit() else (False)

    retorno = validar_numero_decimal(cadena_entrada)

    return retorno


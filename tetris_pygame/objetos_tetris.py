from __future__ import annotations
from typing import ForwardRef, Union
# from typing import Union
import pygame
import random



class Bloque:
    def __init__(self, color:tuple[int, int, int], dim:int, x:int, y:int):
        self.color = color
        self.dim = dim
        self.x = x
        self.y = y


pared_refrencia = ForwardRef("Pared") # hay referencias cruzadas entre los metodos de Pared y Figura
class Figura:
    def __init__(self, letra:str, rotacion:int, lista_bloques:list[Bloque]):
        self.letra = letra
        self.rotacion = rotacion
        self.lista_bloques = lista_bloques

    def trasladar(self, direccion:str, cantidad:int, maximo:int):
        mover = True
        if direccion == "izquierda":
            for bloque in self.lista_bloques:
                if bloque.x <= maximo:
                    mover = False
            if mover:
                for bloque in self.lista_bloques:
                    bloque.x -= cantidad
        elif direccion == "derecha":
            for bloque in self.lista_bloques:
                if bloque.x >= maximo:
                    mover = False
            if mover:
                for bloque in self.lista_bloques:
                    bloque.x += cantidad

    def bajar(self, cantidad: int, maximo: int) -> bool:
        '''
        hace bajar la figura y retorna si se toco el tope o no
        '''
        
        # se baja cada bloque una vez, se verifica un posible pase de tope y se calcula su desfase
        desfase = 0
        for bloque in self.lista_bloques:
            bloque.y += cantidad
            if bloque.y > maximo:
                desfase = bloque.y - maximo # solo la posicion Y del fondo de la figura podria desfasarse, osea que solo habra 1 posible valro de desfase

        # se ajusta el desfase de ser necesario
        if desfase > 0:
            for bloque in self.lista_bloques:
                bloque.y -= desfase

        # se controla el retorno
        retorno = False
        for bloque in self.lista_bloques:
            if bloque.y == maximo:
                retorno = True

        return retorno

        

        # while any(bloque.y > maximo for bloque in self.lista_bloques): # en caso de que algun bloque se pasedel tope, forzarlo a quedar en el tope
        #     for bloque in self.lista_bloques:
        #         bloque.y -= 1

        # return any(bloque.y == maximo for bloque in self.lista_bloques)


    def mostrar (self, screen:pygame.surface.Surface):
        for bloque in self.lista_bloques:
            bloque_en_pantalla = pygame.Rect( bloque.x, bloque.y, bloque.dim, bloque.dim)
            pygame.draw.rect(screen, bloque.color, bloque_en_pantalla)


class Pared:
    def __init__(self, tipo_pared:str ,estructura_pared: list[dict[int, int, list[dict[int, bool, Bloque]]]]):
        '''
        estructura_pared[i] = diccionario_columna = 
            {
                "pos_x", "tope_columna", "bloques"[j] = diccionario_bloque_en_fila = 
                {
                    "pos_y", "bool_bloque", "datos_bloque"
                }
            }
        '''
        self.estructura_pared = estructura_pared
        self.tipo_pared = tipo_pared

    # def agregar_bloques_desde_figura(self, figura_actual: Figura):

    #     for bloque_figura in figura_actual.lista_bloques: # recorrer los bloques en la figura
    #         for diccionario_columna in self.estructura_pared: # recorrer las columnas en la estructura
    #             for bloque_pared in diccionario_columna["bloques"] # recorrer los segmentos de fila correspondiente



    def calcular_tope(self, area_jugable:pygame.rect.Rect, dim_bloque: int) -> Union[int, list[int]]:


        if self.tipo_pared == "CLA": # modo clasico
            retorno = area_jugable.bottom - dim_bloque # se recibe el tope por defecto
            for diccionario_columna in self.estructura_pared:
                if retorno < diccionario_columna["tope_columna"]: # se compara si el tope ha cambiado

                    retorno = diccionario_columna["tope_columna"] # se cambia nuevo retorno

        elif self.tipo_pared == "ARE": # modo arena

            lista_topes = []
            for diccionario_columna in self.estructura_pared: # se recorre cada columna
                tope = diccionario_columna["tope_columna"] # se busca el tope de la columna
                lista_topes.append(tope) # se guarda el tope de la columna

            retorno = lista_topes # se guarda la lista como retorno

        return retorno






        # mover = True
        # for bloque in self.lista_bloques:
        #     if bloque.y >= maximo:
        #         mover = False
        # if mover:
        #     for bloque in self.lista_bloques:
        #         bloque.y += cantidad





def crear_lista_bloques_iniciales(color_RGB_bloque:tuple[int, int, int], dim_bloque:int, x_inicial:int, y_inicial:int) -> list[Bloque]:
    '''
    Crea una lista de bloques para el proceso de creacion de una figura nueva
    '''
    lista_bloques = []

    for i in range(4):
        bloque = Bloque(color_RGB_bloque, dim_bloque, x_inicial, y_inicial)
        lista_bloques.append(bloque)
    return lista_bloques


def crear_figura(color_RGB_bloque:tuple[int, int, int], dim_bloque:int, x_inicial:int, y_inicial:int) -> Figura:
    '''
    Crea una figura con formato de "tetramino" en la posicion inicial indicada
    '''
    print(f"crear_figura:\n x inicial={x_inicial}\ty inicial={y_inicial}")

    lista_bloques = crear_lista_bloques_iniciales(color_RGB_bloque, dim_bloque, x_inicial, y_inicial)
    rotacion = 0
    opciones_letra = ["I", "O", "T", "L"]
    letra = random.choice(opciones_letra)

    match letra:
        case "I": # rectangulo, 4 bloques apilados en una fila
            lista_bloques[1].y = lista_bloques[0].y + dim_bloque #abajo 1
            lista_bloques[2].y = lista_bloques[1].y + dim_bloque #abajo 2 
            lista_bloques[3].y = lista_bloques[2].y + dim_bloque #abajo 3

        case "O": # cuadrado, dos filas de dos bloques juntas
            lista_bloques[1].y = lista_bloques[0].y + dim_bloque #abajo
            lista_bloques[2].x = lista_bloques[0].x + dim_bloque #derecha
            lista_bloques[3].y = lista_bloques[0].y + dim_bloque #diagonal 1/2
            lista_bloques[3].x = lista_bloques[0].x + dim_bloque #diagonal 2/2

        case "T": # literalmente la forma de una T
            lista_bloques[1].y = lista_bloques[0].y + dim_bloque #abajo
            lista_bloques[2].x = lista_bloques[0].x + dim_bloque #derecha
            lista_bloques[3].x = lista_bloques[0].x - dim_bloque #izquierda

        case "L": # literalmente la forma de una L
            lista_bloques[1].y = lista_bloques[0].y + dim_bloque #abajo 1
            lista_bloques[2].y = lista_bloques[1].y + dim_bloque #abajo 2 
            lista_bloques[3].y = lista_bloques[2].y #diagonal 1/2
            lista_bloques[3].x = lista_bloques[2].x + dim_bloque #diagonal 1/2

    figura_retorno = Figura(letra, rotacion, lista_bloques)

    return figura_retorno





def crear_pared(tipo_juego:str, espacio_jugable:pygame.rect.Rect, dim_bloque:int) -> Pared:
    '''
    Crea una nueva pared que contendra la informacion de los bloques caidos
    estructura_pared[i] = diccionario_columna = 
        {
            "pos_x", "tope_columna", "bloques_en_fila"[j] = diccionario_bloque_en_fila = 
            {
                "pos_y", "bool_bloque", "datos_bloque"
            }
        }
    '''

    tope_inicial = espacio_jugable.bottom - dim_bloque

    
    

    # primero se crea el contenido de bloques_en_fila:list[dict] ya que inicialmente sera igual para todas las columnas
    bloques_en_fila = []
    for y in range( tope_inicial, (espacio_jugable.top - 1), -dim_bloque): # y pertenece a [bottom-dim_bloque; top] 
        diccionario_bloque_en_fila = {
            "pos_y": y,
            "bool_bloque": False,
            "datos_bloque": None # inicialmente vacio hasta que caiga la primera figura

        }
        print(f"se creo la coordenada vertical= {y} para la pared")
        bloques_en_fila.append(diccionario_bloque_en_fila)


    # ya obtenida la informacion de los distintos datos de una vertical, se hace un proceso similar para obtener 
    # las posiciones horizontales y asignar los valores a diccionario_columna

    print(f"bottom espacio={espacio_jugable.bottom}\ntop espacio={espacio_jugable.top}\nizquierda_Espacio={espacio_jugable.left}\nderacha espacio={espacio_jugable.right} ")
    estructura_pared = [] # estructura matricial a retornar
    for x in range(espacio_jugable.left, espacio_jugable.right, dim_bloque): # x pertenece a [left; rigth-dim_bloque]
        diccionario_columna = {
            "pos_x": x,
            "tope_columna": tope_inicial, 
            "bloques_en_fila": bloques_en_fila
            }
        estructura_pared.append(diccionario_columna) # se agrega la info de la columna y sus segmentos de fila asociados a estructura_pared
        print(f'se creo la coordenada horizontal= {diccionario_columna["pos_x"]} y se asigno el tope={diccionario_columna["tope_columna"]} para la pared y se le asigno el contenido de los datos horizontales')
    print(f'verificacion de ruta de datos estructura_pared[2]["bloques_en_fila"][0]["pos_y"]={estructura_pared[2]["bloques_en_fila"][0]["pos_y"]}')




    # for y in range( (espacio_jugable.bottom - dim_bloque), (espacio_jugable.top - 1), -dim_bloque): # y pertenece a [bottom-dim_bloque; top]

    #     lista_bloques = [] # primero se crea el contenido de diccionario_bloque_en_fila ya que va contenido dentro de diccionario_columna
    #     diccionario_bloque_en_fila = {
    #         "pos_y": y,
    #         "bool_bloque": False,
    #         "datos_bloque": None # inicialmente vacio hasta que caiga la primera figura
    #     }
    #     lista_bloques.append(diccionario_bloque_en_fila)

    #     # ya que se tienen todos los datos del diccionario de columnas, se setean
    #     for x in range(espacio_jugable.left, espacio_jugable.right, dim_bloque): # x pertenece a [left; righ-dim_bloque]
    #         diccionario_columna = {
    #             "pos_x": x,
    #             "tope_columna": espacio_jugable.bottom - dim_bloque, # tope inicial
    #             "bloques_en_fila": lista_bloques
    #         }
    # estructura_pared.append(diccionario_columna) # se agrega la info de la columna y sus segmentos de fila asociados a estructura_pared

    retorno = Pared(tipo_juego, estructura_pared)
    return retorno


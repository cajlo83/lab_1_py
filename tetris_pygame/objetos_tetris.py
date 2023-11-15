from __future__ import annotations
from typing import ForwardRef, Union
# from typing import Union
import pygame
import random
from colores import *



class Bloque:
    def __init__(self, color:tuple[int, int, int], cuadro:pygame.rect.Rect):
        self.color = color
        self.cuadro = cuadro


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
                if bloque.cuadro.x <= maximo:
                    mover = False
            if mover:
                for bloque in self.lista_bloques:
                    bloque.cuadro.x -= cantidad
        elif direccion == "derecha":
            for bloque in self.lista_bloques:
                if bloque.cuadro.x >= maximo:
                    mover = False
            if mover:
                for bloque in self.lista_bloques:
                    bloque.cuadro.x += cantidad

    def bajar(self, cantidad: int, pared_juego: pared_refrencia) -> bool:
        '''
        hace bajar la figura y retorna si se toco el tope o no
        '''

        # se baja cada bloque una vez, se verifica un posible pase de tope y se calcula su desfase
        desfase = -1
        for bloque in self.lista_bloques:
            bloque.cuadro.y += cantidad

            for diccionario_columna in pared_juego.estructura_pared: # recorrer las columnas en la estructura
                for diccionario_bloque_en_fila in diccionario_columna["bloques_en_fila"]:

                    # se verifica un posible choque en bajada (que se traduce en un desfase y un toque de tope)
                    if diccionario_bloque_en_fila["bool_bloque"] and bloque.cuadro.colliderect(diccionario_bloque_en_fila["datos_bloque"].cuadro):
                        pos_final = diccionario_bloque_en_fila["datos_bloque"].cuadro.y - diccionario_bloque_en_fila["datos_bloque"].cuadro.height
                        desfase = bloque.cuadro.y - pos_final
                    # si la pared aun no tiene bloques adheridos, entonces se comprueba con el valor de tope_inicial
                    elif (bloque.cuadro.y >= pared_juego.tope_inicial): 
                        desfase = bloque.cuadro.y - pared_juego.tope_inicial
             

        # se ajusta el desfase de ser necesario
        retorno = desfase >= 0
        if retorno:
            for bloque in self.lista_bloques:
                bloque.cuadro.y -= desfase

        return retorno


    def mostrar (self, screen:pygame.surface.Surface):
        for bloque in self.lista_bloques:
            # bloque_en_pantalla = pygame.Rect( bloque.x, bloque.y, bloque.dim, bloque.dim)
            pygame.draw.rect(screen, bloque.color, bloque.cuadro)


class Pared:
    def __init__(self, tipo_pared:str, tope_inicial:int ,estructura_pared: list[dict[int, int, list[dict[int, bool, Bloque]]]]):
        '''
        estructura_pared[i] = diccionario_columna = {
                "pos_x":int,  
                "bloques_en_fila"[j] = diccionario_bloque_en_fila = {
                        "pos_y:int", 
                        "bool_bloque":bool, 
                        "datos_bloque": Bloque
                    }
            }
        '''
        self.estructura_pared = estructura_pared
        self.tipo_pared = tipo_pared
        self.tope_inicial = tope_inicial

    def agregar_bloques_desde_figura(self, figura_actual: Figura):

        for bloque_figura in figura_actual.lista_bloques: # recorrer los bloques en la figura
            for diccionario_columna in self.estructura_pared: # recorrer las columnas en la estructura
                for bloque_pared in diccionario_columna["bloques_en_fila"]: # recorrer los segmentos de fila correspondiente
                     # verificar si las coordenadas del bloque en la figura coinciden con la pos_x de la columna y la pos_y del bloque en la pared
                    if (bloque_figura.cuadro.x , bloque_figura.cuadro.y) == (diccionario_columna["pos_x"] , bloque_pared["pos_y"]):
                        bloque_pared["bool_bloque"] = True
                        bloque_pared["datos_bloque"] = bloque_figura
                        
                    

    def mostrar (self, screen:pygame.surface.Surface):
        for diccionario_columna in self.estructura_pared: # recorrer las columnas en la estructura
            for diccionario_bloque_en_fila in diccionario_columna["bloques_en_fila"]: # recorrer los segmentos de fila correspondiente
                # bloque_en_pantalla = pygame.Rect( bloque.x, bloque.y, bloque.dim, bloque.dim)
                if diccionario_bloque_en_fila["bool_bloque"]:
                    pygame.draw.rect(screen, diccionario_bloque_en_fila["datos_bloque"].color, diccionario_bloque_en_fila["datos_bloque"].cuadro)
                    # verificar si las coordenadas del bloque en la figura coinciden con la pos_x de la columna y la pos_y del bloque en la pared



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
        rectangulo = pygame.Rect(x_inicial, y_inicial, dim_bloque, dim_bloque)
        bloque = Bloque(color_RGB_bloque, rectangulo)
        lista_bloques.append(bloque)
    return lista_bloques


def crear_figura(dim_bloque:int, x_inicial:int, y_inicial:int) -> Figura:
    '''
    Crea una figura con formato de "tetramino" en la posicion inicial indicada
    '''
    print(f"crear_figura:\n x inicial={x_inicial}\ty inicial={y_inicial}")

    opciones_color = [color_azul, color_amarillo, color_rojo, color_verde, color_naranja]
    color_RGB_bloque = random.choice(opciones_color)
    lista_bloques = crear_lista_bloques_iniciales(color_RGB_bloque, dim_bloque, x_inicial, y_inicial)
    rotacion = 0 
    opciones_letra = ["I", "O", "T", "L"]
    letra = random.choice(opciones_letra)

    match letra:
        case "I": # rectangulo, 4 bloques apilados en una fila
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y + dim_bloque #abajo 1
            lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y + dim_bloque #abajo 2 
            lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y + dim_bloque #abajo 3

        case "O": # cuadrado, dos filas de dos bloques juntas
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y + dim_bloque #abajo
            lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x + dim_bloque #derecha
            lista_bloques[3].cuadro.y = lista_bloques[0].cuadro.y + dim_bloque #diagonal 1/2
            lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x + dim_bloque #diagonal 2/2

        case "T": # literalmente la forma de una T
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y + dim_bloque #abajo
            lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x + dim_bloque #derecha
            lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x - dim_bloque #izquierda

        case "L": # literalmente la forma de una L
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y + dim_bloque #abajo 1
            lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y + dim_bloque #abajo 2 
            lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y #diagonal 1/2
            lista_bloques[3].cuadro.x = lista_bloques[2].cuadro.x + dim_bloque #diagonal 1/2


    
    figura_retorno = Figura(letra, rotacion, lista_bloques)

    print(f'letra: {figura_retorno.letra}\trotacion: {figura_retorno.rotacion}')
    print("info lista de bloques en la figura")
    for bloque in lista_bloques:
        print(f'x={bloque.cuadro.x}\ty={bloque.cuadro.y}')

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


    # ya obtenida la informacion de los distintos datos de una vertical, se hace un proceso similar para obtener 
    # las posiciones horizontales y asignar los valores a diccionario_columna

   # print(f"bottom espacio={espacio_jugable.bottom}\ntop espacio={espacio_jugable.top}\nizquierda_Espacio={espacio_jugable.left}\nderacha espacio={espacio_jugable.right} ")
    

    #debugeo_columnas = 0 #debug columnas 1/2

    estructura_pared = [] # estructura matricial a retornar
    for x in range(espacio_jugable.left, espacio_jugable.right, dim_bloque): # x pertenece a [left; rigth-dim_bloque]

       
        bloques_en_fila = [] # se crea bloques_en_fila:list[dict] 
        for y in range( tope_inicial, (espacio_jugable.top - 1), -dim_bloque): # y pertenece a [bottom-dim_bloque; top] 
            diccionario_bloque_en_fila = {
                "pos_y": y,
                "bool_bloque": False,
                "datos_bloque": None # inicialmente vacio hasta ser ocupado
            }
            bloques_en_fila.append(diccionario_bloque_en_fila)

            # debug coordenadas
           # print(f"se creo una coordenada en la pared con posicion: ({x};{y})")


        diccionario_columna = {
            "pos_x": x,
            "bloques_en_fila": bloques_en_fila
            }
        estructura_pared.append(diccionario_columna) # se agrega la info de la columna y sus segmentos de fila asociados a estructura_pared
        
        
        # debug columnas 1/2
      #  print(f'se creo la columna numero: {debugeo_columnas}')
    #    debugeo_columnas +=1

  
    retorno = Pared(tipo_juego, tope_inicial, estructura_pared)
    return retorno




# def tocar_tope(figura_actual: Figura, pared_juego: Pared) -> bool:


#           for bloque in figura_actual.lista_bloques:
#             for diccionario_columna in pared_juego.estructura_pared: # recorrer las columnas en la estructura
#                 if (bloque.cuadro.x == diccionario_columna["pos_X"]) and (bloque.cuadro.y > diccionario_columna["tope_columna"] ):
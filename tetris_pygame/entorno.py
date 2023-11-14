import pygame
import sys
import time
import typing
import sub_biblioteca
from colores import *
from objetos_tetris import *



def crear_ventana(ancho:int, alto:int, texto_titulo:str) -> pygame.surface.Surface:
    '''
    Recibe: el alto, el ancho y el texto del titulo de la ventana
    Operacion: crea la ventana del programa con el tamaño y el titulo especificados
    Retorna: el objeto surface que representra a la ventana
    '''
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(texto_titulo)
    return ventana


def crear_grilla(espacio_jugable:pygame.rect.Rect, dimension_grilla:int) -> list[tuple]:
    '''
    Recibe: el espacio jugable y la dimension de las grillas
    Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una grilla 
    Retorno: una lista de tuplas que representan limites de una linea recta
    '''

    lista_lineas = []
    
    for x in range(espacio_jugable.left, espacio_jugable.right + 1, dimension_grilla):
        linea = ((x, espacio_jugable.top), (x, espacio_jugable.bottom))
        lista_lineas.append(linea)
    for y in range(espacio_jugable.top, espacio_jugable.bottom + 1, dimension_grilla):
        linea = ((espacio_jugable.left, y), (espacio_jugable.right, y))
        lista_lineas.append(linea)

    return lista_lineas

def crear_puntos_grilla(espacio_jugable, dimension_grilla):
    '''
    Recibe: el espacio jugable y la dimension de las grillas
    Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una lista de puntos (círculos)
    Retorno: una lista de lista (matriz) de tuplas que representan las coordenadas de los puntos
    '''
    matriz_puntos = []
    

    for x in range(espacio_jugable.left, (espacio_jugable.right + 1), dimension_grilla):
        lista_puntos = []
        for y in range(espacio_jugable.top, (espacio_jugable.bottom + 1), dimension_grilla):
            punto = (x, y)
            lista_puntos.append(punto)
        matriz_puntos.append(lista_puntos)
        

    return matriz_puntos

def mostrar_grilla (lista_lineas:list[tuple], screen:pygame.surface.Surface) -> bool:

    if sub_biblioteca.valida_lista(lista_lineas):
        for linea in lista_lineas:
            pygame.draw.line(screen, color_gris, linea[0], linea[1])
        retorno = True
    else:
        retorno = False

    return retorno
        
def mostrar_puntos(matriz_puntos:list[list[tuple]], screen:pygame.surface.Surface, radio: int) -> bool:
    
    retorno = sub_biblioteca.valida_lista(matriz_puntos) # verifica valor del retorno 1/2
    if retorno:
        for fila in matriz_puntos:
            retorno = sub_biblioteca.valida_lista(fila) # verifica valor del retorno 2/2
            if retorno:
                for punto in fila:
                    pygame.draw.circle(screen, color_gris, punto, radio)
            else:
                break

    return retorno


# def mostrar_jugador(figura_jugador:Figura, screen:pygame.surface.Surface,) -> bool:
    
#     lista_figuras_pantalla = []
#     for bloque in figura_jugador.lista_bloques:
#         jugador_en_pantalla = pygame.Rect( bloque.x, bloque.y, bloque.dim, bloque.dim)
#         pygame.draw.rect(screen, bloque.color, jugador_en_pantalla)
#         lista_figuras_pantalla.append(jugador_en_pantalla)

#     return retorno

import pygame
import sys
import time
import espacio_para_jugar
from colores import *
import typing



def crear_ventana(ancho:int, alto:int, texto_titulo:str) -> pygame.surface.Surface:
    '''
    Recibe: el alto, el ancho y el texto del titulo de la ventana
    Operacion: crea la ventana del programa con el tamaño y el titulo especificados
    Retorna: el objeto surface que representra a la ventana
    '''
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(texto_titulo)
    return ventana

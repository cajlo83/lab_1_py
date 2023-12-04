import pygame

from tetris_funciones import *

from tetris_archivos import *

from PIL import Image

import sys


def crear_ventana(ancho:int, alto:int, texto_titulo:str) -> pygame.surface.Surface:
    '''
    Recibe: el alto, el ancho y el texto del titulo de la ventana
    Operacion: crea la ventana del programa con el tamaño y el titulo especificados
    Retorna: el objeto surface que representra a la ventana
    '''
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(texto_titulo)

    #ventana = ventana.convert_alpha()
    return ventana




# Función para mostrar texto en la pantalla
def mostrar_texto(screen:pygame.surface.Surface, texto:str, x:int, y:int, font:pygame.font.Font, color:tuple[int,int,int]) -> pygame.rect.Rect:
    '''
    muestra un texto y retorna un rectangulo con datos de ancho y alto que ocupa en la pantalla
    '''
    texto_renderizado = font.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))
    return texto_renderizado.get_rect()



class Boton:
    def __init__(self, fuente:pygame.font.Font, texto:str, x_texto:int, y_texto:int, color_texto:tuple[int, int, int], color_cuadrado:tuple[int, int, int] ) -> None:
        self.fuente = fuente
        self.texto = texto
        self.x_texto = x_texto
        self.y_texto = y_texto
        self.color_texto = color_texto
        self.color_cuadrado = color_cuadrado

    def mostrar(self,screen:pygame.surface.Surface) -> pygame.rect.Rect:
        '''
        muestra el boton y retorna su rectangulo correspondiente
        '''

        # se renderiza texto para extraer el valor de su rectangulo y crear un rectangulo mas grande a su alrededor
        texto_renderizado = self.fuente.render(self.texto, True, self.color_texto)
        cuadrado_texto = texto_renderizado.get_rect()
        rectangulo_boton = pygame.rect.Rect( (self.x_texto - 5), (self.y_texto - 5), cuadrado_texto.width + 10, cuadrado_texto.height + 10 )

        # se dibujan el cuadrado y el texto
        pygame.draw.rect(screen, self.color_cuadrado, rectangulo_boton )
        screen.blit(texto_renderizado, (self.x_texto, self.y_texto))
        
        # se retorna el cuadrado del boton
        return rectangulo_boton



def mostrar_grilla (lista_lineas:list[tuple], screen:pygame.surface.Surface):
    '''
    muestra una lista de lineas que representan una grilla
    '''

    if valida_lista(lista_lineas):
        for linea in lista_lineas:
            pygame.draw.line(screen, color_negro, linea[0], linea[1])
         
def mostrar_puntos(matriz_puntos:list[list[tuple]], screen:pygame.surface.Surface, radio: int):
    '''
    muestra una lista de puntos 
    '''
    
    
    if valida_lista(matriz_puntos):
        for fila in matriz_puntos:
            if valida_lista(fila):
                for punto in fila:
                    pygame.draw.circle(screen, color_negro, punto, radio)
            else:
                break



def leer_evento() -> tuple[bool, int, tuple[int, int]]:
    '''
    lee posible evento de cierre del bucle y de tecla presionada.
    retorna valores por defecto en caso de no detectarse eventos.
    retorno = (running, tecla_pulsada)
    '''
    retorno_0 = True
    retorno_1 = None
    retorno_2 = (0,0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # salida de pygame
            retorno_0 = False
        elif event.type == pygame.KEYDOWN: # tecla presionada
            retorno_1 = copy.deepcopy(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN: # click presionado
            retorno_2 = copy.deepcopy(event.pos)

    return (retorno_0, retorno_1, retorno_2)


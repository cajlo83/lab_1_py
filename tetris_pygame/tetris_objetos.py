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

    def mover(self, orientacion:str, cantidad:int):
        '''
        mueve un bloque segun una orientacion ("HOR" | "VER") y una cantidad de espacios
        '''

        if orientacion == "HOR":
            self.cuadro.x += cantidad
        elif orientacion == "VER":
            self.cuadro.y += cantidad
        else:
            print (f'error en mover_bloque: horientacion ={orientacion}, cantidad = {cantidad}')
    
    def choque(self, otro_bloque:Bloque) -> bool:
        '''
        verifica una colision entre dos bloques
        '''
        return self.cuadro.colliderect(otro_bloque.cuadro)
    

    def mostrar (self, screen:pygame.surface.Surface):
        '''
        representa al bloque graficamente
        '''
        pygame.draw.rect(screen, self.color, self.cuadro)
    
    
class Figura:
    def __init__(self, letra:str, rotacion:int, lista_bloques:list[Bloque]):
        self.letra = letra
        self.rotacion = rotacion
        self.lista_bloques = lista_bloques

    def mover(self, orientacion:str, cantidad:int=None):
        '''
        mueve una figura segun una orientacion ("HOR" | "VER") y una cantidad de espacios
        '''
        if cantidad is None:
            cantidad = self.lista_bloques[0].cuadro.width

        for bloque in self.lista_bloques:
                bloque.mover(orientacion, cantidad)



    def mostrar (self, screen:pygame.surface.Surface):
        '''
        muestra la lista de bloques en la figura
        '''
        for bloque in self.lista_bloques:
            bloque.mostrar(screen)


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
                    diccionario_bloque_en_fila["datos_bloque"].mostrar(screen)
                    

    def verificar_ganadores(self):
        
        y_max = len(self.estructura_pared[0]["bloques_en_fila"])
        x_max = len(self.estructura_pared)

        lista_retorno = []
        for y in range(y_max): # verifico una altura
            for x in range(x_max): # recorro las posiciones horizontales de esa altura

                # si la posicion no esta ocupada se guarda y se sale del bucle de horizonales
                ganador = self.estructura_pared[x]["bloques_en_fila"][y]["bool_bloque"]
                if not ganador: 
                    break
            
            # si el bucle de horizontales termina con un ganador, se informa la altura en lista_retorno
            if ganador:
                lista_retorno.append(y)

        # se retorna lista_retorno
        return lista_retorno




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


def figura_verificar_devolucion(orientacion: str, figura:Figura, pared:Pared) -> int:
    '''
    verifica una posible choque con la pared o los limites del juego
    '''
    retorno = 0

    if orientacion == "HOR":
        
        tope_derecha = pared.estructura_pared[-1]["pos_x"] # el tope derecho es la posicion de la ultima columna
        tope_izquierda = pared.estructura_pared[0]["pos_x"] # el tope izquierdo es la posicion de la primera columna
        for bloque_figura in figura.lista_bloques:
                
            # Se verifica que no pase los limites por defecto del juego
            if (bloque_figura.cuadro.x > tope_derecha) or (bloque_figura.cuadro.x < tope_izquierda):
                retorno = bloque_figura.cuadro.width
                break

            # se itera para verificar que no haya una colision sucediendo con ningun otro bloque activo de la pared
            for estructura_columna in pared.estructura_pared: 
                for bloque_pared in estructura_columna["bloques_en_fila"]:
                    if bloque_pared["bool_bloque"] and bloque_figura.choque(bloque_pared["datos_bloque"]):

                        retorno = bloque_figura.cuadro.width 
                        break
                if retorno:
                    break             
            if retorno:
                break


    elif orientacion == "VER":
        
        referencia_fondo = pared.tope_inicial 
        for bloque_figura in figura.lista_bloques:
                
            # Se verifica que no pase los limites por defecto del juego
            if (bloque_figura.cuadro.y > referencia_fondo):
                retorno = bloque_figura.cuadro.y - referencia_fondo
                break

            # se itera para verificar que no haya una colision sucediendo con ningun otro bloque activo de la pared
            for estructura_columna in pared.estructura_pared: 
                for bloque_pared in estructura_columna["bloques_en_fila"]:
                    if bloque_pared["bool_bloque"] and bloque_figura.choque(bloque_pared["datos_bloque"]):
                        retorno = bloque_figura.cuadro.y - (bloque_pared["datos_bloque"].cuadro.y - bloque_figura.cuadro.height)
                        
                        print (f'*********************se detecto un choque:****************')
                        print(f'altura bloque_figura={bloque_figura.cuadro.y}\taltura bloque_pared={bloque_pared["datos_bloque"].cuadro.y}\tretorno={retorno}')
                    
                        break
                if retorno:
                    break
            if retorno:
                break

    else:
        print(f'error en figura_verificar_devolucion: orientacion = {orientacion}')
    return retorno


def figura_mover(orientacion: str, figura:Figura, pared:Pared, cantidad:int) -> bool:
    '''
    integra todo el proceso de traslacion de una figura. Indica si ya no puede trasladarse mas
    '''
    retorno = False
    devolucion = 0
    figura.mover(orientacion, cantidad )
    devolucion = figura_verificar_devolucion(orientacion, figura, pared)
    if devolucion:
        if orientacion == "HOR":
            figura.mover(orientacion, -cantidad)
        elif orientacion == "VER":
            figura.mover(orientacion, -devolucion)
            retorno = True


    return retorno
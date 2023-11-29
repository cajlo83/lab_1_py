from __future__ import annotations
from typing import ForwardRef, Union
# from typing import Union
import pygame
import random
from colores import *
from sub_biblioteca import *
import copy




class Bloque:
    def __init__(self, color:tuple[int, int, int], cuadro:pygame.rect.Rect):
        self.color = color
        self.cuadro = cuadro

    @property
    def x(self):
        return self.cuadro.x

    @property
    def y(self):
        return self.cuadro.y

    @property
    def top(self):
        return self.cuadro.top

    @property
    def left(self):
        return self.cuadro.left

    @property
    def right(self):
        return self.cuadro.right

    @property
    def bottom(self):
        return self.cuadro.bottom

    def mover(self, orientacion:str, cantidad:int):
        '''
        mueve un bloque segun una orientacion ("HOR" | "VER") y una cantidad de espacios
        '''

        if orientacion == "HOR":
            self.cuadro.x += cantidad
        elif orientacion == "VER":
            self.cuadro.y += cantidad

    
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
    
    def cambiar_coordenadas(self, nueva_coord:tuple[int, int]):
        self.cuadro.x = nueva_coord[0]
        self.cuadro.y = nueva_coord[1]


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

    def rotar_L(self):
        '''
        rotacion para figuras L
        '''

        dim_bloque = self.lista_bloques[0].cuadro.width
        



        if self.rotacion == 0:

            coord_bloque_0 = ( ( self.lista_bloques[1].cuadro.x - dim_bloque ) , self.lista_bloques[1].cuadro.y )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] + dim_bloque ), coord_bloque_0[1] )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] + dim_bloque ) , coord_bloque_1[1])
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( coord_bloque_2[0] , ( coord_bloque_2[1] - dim_bloque ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)



        if self.rotacion == 1:

            coord_bloque_0 = ( ( self.lista_bloques[2].cuadro.x ) , ( self.lista_bloques[2].cuadro.y + dim_bloque ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] - dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = ( ( coord_bloque_1[0] ) , ( coord_bloque_1[1] - dim_bloque ))
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] - dim_bloque ) , ( coord_bloque_2[1]) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)

        


        if self.rotacion == 2:

            coord_bloque_0 = ( ( self.lista_bloques[2].cuadro.x ) , ( self.lista_bloques[2].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] - dim_bloque ), ( coord_bloque_0[1] ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = ( ( coord_bloque_1[0] - dim_bloque ) , ( coord_bloque_1[1] ))
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] ) , ( coord_bloque_2[1]) + dim_bloque )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)
        


        if self.rotacion == 3:

            coord_bloque_0 = ( ( self.lista_bloques[1].cuadro.x ) , ( self.lista_bloques[1].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = ( ( coord_bloque_1[0] ) , ( coord_bloque_1[1] + dim_bloque ))
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] + dim_bloque ) , ( coord_bloque_2[1]) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)
        

        
        if self.rotacion == 3:
            self.rotacion = 0
        else:
            self.rotacion += 1
            
    def rotar_I(self):
        '''
        rotacion para figuras I
        '''

        dim_bloque = self.lista_bloques[0].cuadro.width
        



        if self.rotacion == 0: # convertir a 1

            coord_bloque_0 = ( ( self.lista_bloques[0].cuadro.x - dim_bloque) , ( self.lista_bloques[0].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] + dim_bloque ), ( coord_bloque_0[1] ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] + dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] + dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)



        if self.rotacion == 1: # convertir a 2

            coord_bloque_0 = ( ( self.lista_bloques[2].cuadro.x ) , ( self.lista_bloques[0].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] ) , ( coord_bloque_1[1] + dim_bloque ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] ) , ( coord_bloque_2[1] + dim_bloque ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)



        if self.rotacion == 2: # convertir a 3

            coord_bloque_0 = ( ( self.lista_bloques[0].cuadro.x - (2 * dim_bloque)) , ( self.lista_bloques[0].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] + dim_bloque ), ( coord_bloque_0[1] ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] + dim_bloque ) , ( coord_bloque_1[1] ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] + dim_bloque ) , ( coord_bloque_2[1] ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)



        if self.rotacion == 3: # convertir a 0

            coord_bloque_0 = ( ( self.lista_bloques[1].cuadro.x ) , ( self.lista_bloques[0].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] ) , ( coord_bloque_1[1] + dim_bloque ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] ) , ( coord_bloque_2[1] + dim_bloque ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)

    
        
        if self.rotacion == 3:
            self.rotacion = 0
        else:
            self.rotacion += 1
            
    def rotar_T(self):
        '''
        rotacion para figuras T
        '''

        dim_bloque = self.lista_bloques[0].cuadro.width
        



        if self.rotacion == 0: # convertir a 1

            coord_bloque_0 = ( ( self.lista_bloques[1].cuadro.x ) , ( self.lista_bloques[1].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] + dim_bloque ), ( coord_bloque_0[1] ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] ) , ( coord_bloque_0[1] - dim_bloque ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_0[0] ) , ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)


        if self.rotacion == 1: # convertir a 2

            coord_bloque_0 = ( ( self.lista_bloques[0].cuadro.x ) , ( self.lista_bloques[0].cuadro.y ) )
            #se mantiene

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] - dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] - dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_0[0] + dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)


        if self.rotacion == 2: # convertir a 3

            coord_bloque_0 = ( ( self.lista_bloques[0].cuadro.x ) , ( self.lista_bloques[0].cuadro.y ) )
            #se mantiene

            coord_bloque_1 = ( ( coord_bloque_0[0] - dim_bloque), ( coord_bloque_0[1] ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] ) , ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_0[0] ) , ( coord_bloque_0[1] - dim_bloque ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)


        if self.rotacion == 3: # convertir a 0

            coord_bloque_0 = ( ( self.lista_bloques[3].cuadro.x ) , ( self.lista_bloques[3].cuadro.y ) )
            self.lista_bloques[0].cambiar_coordenadas(coord_bloque_0)

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + dim_bloque ) )
            self.lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] + dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_0[0] - dim_bloque ) , ( coord_bloque_0[1] ) )
            self.lista_bloques[3].cambiar_coordenadas(coord_bloque_3)

        
        if self.rotacion == 3:
            self.rotacion = 0
        else:
            self.rotacion += 1
   

class Pared:
    def __init__(self, tipo_pared:str, tope_inicial:int, tope_game_over:int ,estructura_pared: list[dict[int, int, list[dict[int, bool, Bloque]]]]):
        '''
        estructura_pared[i] = diccionario_columna = {
                "pos_x":int,  
                "bloques_en_fila"[j] = diccionario_bloque_en_fila = {
                        "pos_y":int, 
                        "bool_bloque":bool, 
                        "datos_bloque": Bloque
                    }
            }
        '''
        self.estructura_pared = estructura_pared
        self.tipo_pared = tipo_pared
        self.tope_inicial = tope_inicial
        self.tope_game_over = tope_game_over

    def agregar_bloques_desde_figura(self, figura_actual: Figura) -> bool:
        '''
        agranda la pared verificando la lista de bloques en la figura cuyas coordenadas deben estar representadas en las coordenadas de la pared.
        en caso de haber almenos un bloque que no coincide con las coordenadas propuestas se considera game over
        '''

        for bloque_figura in figura_actual.lista_bloques: # recorrer los bloques en la figura
            
            # verifica que el cuadro a agregar no este fuera del tope de game_over
            game_over = bloque_figura.cuadro.y < self.tope_game_over 
            if game_over:
                break

            for diccionario_columna in self.estructura_pared: # recorrer las columnas en la estructura
                for bloque_pared in diccionario_columna["bloques_en_fila"]: # recorrer los segmentos de fila correspondiente
                     # verificar si las coordenadas del bloque en la figura coinciden con la pos_x de la columna y la pos_y del bloque en la pared
                    if (bloque_figura.cuadro.x , bloque_figura.cuadro.y) == (diccionario_columna["pos_x"] , bloque_pared["pos_y"]):
                        bloque_pared["bool_bloque"] = True
                        bloque_pared["datos_bloque"] = bloque_figura
                        
        return game_over
                    

    def mostrar (self, screen:pygame.surface.Surface):
        for diccionario_columna in self.estructura_pared: # recorrer las columnas en la estructura
            for diccionario_bloque_en_fila in diccionario_columna["bloques_en_fila"]: # recorrer los segmentos de fila correspondiente
                # bloque_en_pantalla = pygame.Rect( bloque.x, bloque.y, bloque.dim, bloque.dim)
                if diccionario_bloque_en_fila["bool_bloque"]: # muestra el dato solo si el bloque esta en True
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

    def eliminar_filas(self, lista_ganadores:list[int]) -> int:
        '''
        elimina las filas donde se detectaron ganadores
        '''
        

        retorno = 0
        if valida_lista(lista_ganadores):
            y_max = len(self.estructura_pared[0]["bloques_en_fila"])
            x_max = len(self.estructura_pared)
            for y_ganador in reversed(lista_ganadores): # se recorre alturas de las filas de ganadores de la mas alta a la mas baja
                
                # verifico las alturas en [y_ganador, y_max]
                #(recordar que aunque range no incluye el valor de y_max, el valor de la ultima posicion de la fila es y_max -1)
                    
                for y in range(y_ganador, (y_max)): 
                    for x in range(x_max): # recorro las posiciones horizontales de la altura en evaluacion

                        if y == (y_max - 1): # caso de llega a la altura maxima se cambia el valor de la calve "bool_bloque"
                            self.estructura_pared[x]["bloques_en_fila"][y]["bool_bloque"] = False

                        else: # caso de aun no llegar a la altura maxima, toma el valor de las claves "bool_bloque" y "datos_bloque" del bloque siguiente
                          
                            self.estructura_pared[x]["bloques_en_fila"][y]["bool_bloque"] = self.estructura_pared[x]["bloques_en_fila"][y+1]["bool_bloque"]
                            self.estructura_pared[x]["bloques_en_fila"][y]["datos_bloque"] = self.estructura_pared[x]["bloques_en_fila"][y+1]["datos_bloque"]

                            if self.estructura_pared[x]["bloques_en_fila"][y]["bool_bloque"]: # si se recibe un bloque activo, hay que actualizar la posicion de su cuadro asociado
                                nueva_altura = self.estructura_pared[x]["bloques_en_fila"][y]["pos_y"]
                                self.estructura_pared[x]["bloques_en_fila"][y]["datos_bloque"].cuadro.y = nueva_altura

                        

        

            retorno = len(lista_ganadores)


        return retorno

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
                        
                        # print (f'*********************se detecto un choque:****************')
                        # print(f'altura bloque_figura={bloque_figura.cuadro.y}\taltura bloque_pared={bloque_pared["datos_bloque"].cuadro.y}\tretorno={retorno}')
                    
                        break
                if retorno:
                    break
            if retorno:
                break

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
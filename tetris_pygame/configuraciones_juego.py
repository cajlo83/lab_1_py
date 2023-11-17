import pygame
import sys
import time
import typing
import sub_biblioteca
from colores import *
from objetos_tetris import *

class Configuracion:
    def __init__(self,texto_titulo:pygame.surface.Surface, fps:int, dificultad:int, tiempo_entre_movimientos:float, espacio_jugable:pygame.rect.Rect, dimension_bloque:int, puntaje:int, x_jugador:int, y_jugador:int):
        self.texto_titulo = texto_titulo #
        self.fps = fps #
        self.dificultad = dificultad
        self.tiempo_entre_movimientos = tiempo_entre_movimientos #
        self.espacio_jugable = espacio_jugable # 
        self.dimension_bloque = dimension_bloque
        self.puntaje = puntaje #
        self.x_jugador = x_jugador #
        self.y_jugador = y_jugador #
        self.texto_titulo = texto_titulo #


    def crear_grilla(self) -> list[tuple]:
        '''
        Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una grilla 
        Retorno: una lista de tuplas que representan limites de una linea recta
        '''

        lista_lineas = []
        
        for x in range(self.espacio_jugable.left, self.espacio_jugable.right + 1, self.dimension_bloque):
            linea = ((x, self.espacio_jugable.top), (x, self.espacio_jugable.bottom))
            lista_lineas.append(linea)
        for y in range(self.espacio_jugable.top, self.espacio_jugable.bottom + 1, self.dimension_bloque):
            linea = ((self.espacio_jugable.left, y), (self.espacio_jugable.right, y))
            lista_lineas.append(linea)

        return lista_lineas

    def crear_puntos(self) -> list[tuple]:
        '''
        Recibe: el espacio jugable y la dimension de las grillas
        Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una lista de puntos (círculos)
        Retorno: una lista de lista (matriz) de tuplas que representan las coordenadas de los puntos
        '''
        matriz_puntos = []
        

        for x in range(self.espacio_jugable.left, (self.espacio_jugable.right + 1), self.dimension_bloque):
            lista_puntos = []
            for y in range(self.espacio_jugable.top, (self.espacio_jugable.bottom + 1), self.dimension_bloque):
                punto = (x, y)
                lista_puntos.append(punto)
            matriz_puntos.append(lista_puntos)
            

        return matriz_puntos

    def tiempo_entre_pulsos(self, tiempo_transcurrido) -> bool:
        return tiempo_transcurrido >= self.tiempo_entre_movimientos
    
    def mostrar_titulo(self, screen:pygame.surface.Surface):
        screen.blit(self.texto_titulo, (screen.get_width() // 2 - self.texto_titulo.get_width() // 2, 8)) # titulo

def config_crear(ancho_espacio_jugable:int, limite_movimientos_por_segundo:int, dificultad:int ) -> Configuracion:
    '''
    crea el archivo de configuracion el cual contendra variables de uso recurrente a lo largo del juego
    '''
    # espacio jugable
    alto_espacio_jugable = 2 * ancho_espacio_jugable
    espacio_jugable = pygame.Rect(50, 30, ancho_espacio_jugable, alto_espacio_jugable) #
    dimension_bloque = int (ancho_espacio_jugable / 10) #


    # tiempo entre movimientos
    tiempo_entre_movimientos = 1 / limite_movimientos_por_segundo #

    # fps
    fps = limite_movimientos_por_segundo * 5 #

    # posicion inicial del jugador
    x_jugador = int((espacio_jugable.left + espacio_jugable.right) / 2 - dimension_bloque) #
    y_jugador = espacio_jugable.top #

    
    # Texto a mostrar en pantalla
    fuente_texto = pygame.font.Font(None, 36)
    texto_titulo = fuente_texto.render("Juguemos al tetris", True, color_morado) #

    # puntaje
    puntaje = 0 #

    retorno = Configuracion(texto_titulo, fps, dificultad, tiempo_entre_movimientos, espacio_jugable, dimension_bloque, puntaje, x_jugador, y_jugador)
    return retorno

    


def crear_ventana(ancho:int, alto:int, texto_titulo:str) -> pygame.surface.Surface:
    '''
    Recibe: el alto, el ancho y el texto del titulo de la ventana
    Operacion: crea la ventana del programa con el tamaño y el titulo especificados
    Retorna: el objeto surface que representra a la ventana
    '''
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(texto_titulo)
    return ventana




def mostrar_grilla (lista_lineas:list[tuple], screen:pygame.surface.Surface):

    if sub_biblioteca.valida_lista(lista_lineas):
        for linea in lista_lineas:
            pygame.draw.line(screen, color_negro, linea[0], linea[1])
 
        
def mostrar_puntos(matriz_puntos:list[list[tuple]], screen:pygame.surface.Surface, radio: int):
    
    
    if sub_biblioteca.valida_lista(matriz_puntos):
        for fila in matriz_puntos:
            if sub_biblioteca.valida_lista(fila):
                for punto in fila:
                    pygame.draw.circle(screen, color_negro, punto, radio)
            else:
                break



def crear_figura(config: Configuracion) -> Figura:
    '''
    Crea una figura con formato de "tetramino" en la posicion inicial indicada
    '''
  

    opciones_color = [color_azul, color_amarillo, color_rojo, color_verde, color_naranja]
    color_RGB_bloque = random.choice(opciones_color)
    lista_bloques = crear_lista_bloques_iniciales(color_RGB_bloque, config.dimension_bloque, config.x_jugador, config.y_jugador)
    rotacion = 0 
    opciones_letra = ["I", "O", "T", "L"]
    letra = random.choice(opciones_letra)

    match letra:
        case "I": # rectangulo, 4 bloques apilados en una fila
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo 1
            lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y +  config.dimension_bloque #abajo 2 
            lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y +  config.dimension_bloque #abajo 3

        case "O": # cuadrado, dos filas de dos bloques juntas
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo
            lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #derecha
            lista_bloques[3].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #diagonal 1/2
            lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #diagonal 2/2

        case "T": # literalmente la forma de una T
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo
            lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #derecha
            lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x -  config.dimension_bloque #izquierda

        case "L": # literalmente la forma de una L
            lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo 1
            lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y +  config.dimension_bloque #abajo 2 
            lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y #diagonal 1/2
            lista_bloques[3].cuadro.x = lista_bloques[2].cuadro.x +  config.dimension_bloque #diagonal 1/2


    
    figura_retorno = Figura(letra, rotacion, lista_bloques)

    # print(f'letra: {figura_retorno.letra}\trotacion: {figura_retorno.rotacion}')
    # print("info lista de bloques en la figura")
    # for bloque in lista_bloques:
    #     print(f'x={bloque.cuadro.x}\ty={bloque.cuadro.y}')

    return figura_retorno



def crear_pared(tipo_juego:str, config: Configuracion) -> Pared:
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

    tope_inicial = config.espacio_jugable.bottom - config.dimension_bloque


    # ya obtenida la informacion de los distintos datos de una vertical, se hace un proceso similar para obtener 
    # las posiciones horizontales y asignar los valores a diccionario_columna

   # print(f"bottom espacio={espacio_jugable.bottom}\ntop espacio={espacio_jugable.top}\nizquierda_Espacio={espacio_jugable.left}\nderacha espacio={espacio_jugable.right} ")
    

    #debugeo_columnas = 0 #debug columnas 1/2

    estructura_pared = [] # estructura matricial a retornar
    for x in range( config.espacio_jugable.left,  config.espacio_jugable.right, config.dimension_bloque): # x pertenece a [left; rigth-config.dimension_bloque]

       
        bloques_en_fila = [] # se crea bloques_en_fila:list[dict] 
        for y in range( tope_inicial, ( config.espacio_jugable.top - 1), -config.dimension_bloque): # y pertenece a [bottom-config.dimension_bloque; top] 
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


import sqlite3

import os

import pygame

from mi_pygame import *


class BotonImagen:
    def __init__(self, imagen:pygame.surface.Surface, cuadro:pygame.rect.Rect) -> None: 
        self.imagen = imagen
        self.cuadro = cuadro
        
    def mostrar(self, screen:pygame.surface.Surface): #
        screen.blit(self.imagen, self.cuadro)



class Media:
    def __init__(self, pista_facil, pista_normal, pista_dificil, boton_pausa_play:BotonImagen, volumen_actual, volumen_barra:pygame.rect.Rect, pausa_sonido):
        self.pista_facil = pista_facil
        self.pista_normal = pista_normal
        self.pista_dificil = pista_dificil
        self.boton_pausa_play = boton_pausa_play
        self.volumen_actual = volumen_actual
        self.volumen_barra = volumen_barra
        self.pausa_sonido = pausa_sonido

    def reproducir(self, dificultad:int): #
        if dificultad == 1:
            pygame.mixer.music.load(self.pista_facil)
        if dificultad == 2:
            pygame.mixer.music.load(self.pista_normal)
        if dificultad >= 3:
            pygame.mixer.music.load(self.pista_dificil)

        pygame.mixer.music.set_volume(self.volumen_actual)
        pygame.mixer.music.play()

    def dibujar_volumen_barra(self, screen:pygame.surface.Surface): #
        '''
        Dibuja la barra de control de volumen
        '''
        pygame.draw.rect(screen, (169, 169, 169), self.volumen_barra)  # Color gris claro
        pygame.draw.rect(screen, (0, 128, 0), (self.volumen_barra.x, self.volumen_barra.y, self.volumen_actual * self.volumen_barra.width, self.volumen_barra.height))

    def controlar(self, evento_pos): #
        if evento_pos is not (0, 0):
            if self.volumen_barra.collidepoint(evento_pos):
                # Ajusta el volumen de acuerdo a la posición del ratón en la barra
                self.volumen_actual = max(0.0, min(1.0, (evento_pos[0] - self.volumen_barra.x) / self.volumen_barra.width))
                pygame.mixer.music.set_volume(self.volumen_actual)

            elif self.boton_pausa_play.cuadro.collidepoint(evento_pos):
                self.pausa_sonido = not self.pausa_sonido
                if self.pausa_sonido:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    def mostrar_panel_audio(self, screen:pygame.surface.Surface, color_bandeja:tuple[int,int,int]):
        
        fonter = pygame.font.Font(None, 36)
        fonter_size = fonter.get_height()

        # bandeja de sonido
        pygame.draw.rect(screen, color_bandeja, (self.volumen_barra.left - 10 , self.boton_pausa_play.cuadro.top - 20 - fonter_size, (self.volumen_barra.width + 20 ), ( self.volumen_barra.bottom - self.boton_pausa_play.cuadro.top + 30 + fonter_size)))
        mostrar_texto(screen, "Sonido:", self.volumen_barra.left, self.boton_pausa_play.cuadro.top - 10 - fonter_size, fonter, color_blanco)
        
        self.dibujar_volumen_barra(screen)
        self.boton_pausa_play.mostrar(screen)

def crear_media() -> Media: #
    '''
    inicializa la configuracion para reproducir los archivos de sonido
    '''
    directorio_multimedia = armar_directorio_tetris_pygame("media")

    # pista audio facil
    pista_facil = armar_directorio_tetris_pygame("facil - Kingstux_-_04_-_Tetris_Trance.mp3", directorio_multimedia)
    # pista audio normal
    pista_normal = armar_directorio_tetris_pygame("normal - Searching_For_Aliens_-_TETRIS__Halloween_Version_.mp3", directorio_multimedia)
    # pista audio dificil
    pista_dificil = armar_directorio_tetris_pygame("dificil - Dj_Ocean__-_Tetris_Song.mp3", directorio_multimedia)
    # boton_pausa_play
    directorio_pausa_play = armar_directorio_tetris_pygame("pausa_play.png", directorio_multimedia)
    imagen_pausa_play = pygame.image.load(directorio_pausa_play)
    cuadro_pausa_play = imagen_pausa_play.get_rect()
    cuadro_pausa_play.x = 500
    cuadro_pausa_play.y = 500
    boton_pausa_play = BotonImagen(imagen_pausa_play, cuadro_pausa_play)
    # volumen_actual
    volumen_actual = 0.3
    # barra control de volumen
    volumen_barra = pygame.Rect(400, 600, 200, 20)
    # pausa_sonido
    pausa_sonido = False

    

    return Media(pista_facil, pista_normal, pista_dificil, boton_pausa_play, volumen_actual, volumen_barra, pausa_sonido)



def db_crear(directorio:str):
    '''
    Crea la base de datos en caso que no exista
    '''    
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE puntajes
                         (puntaje INTEGER, dificultad INTEGER, nombre TEXT)''') # tablas con orden puntaje - dificultad - nombre
    except sqlite3.Error as e:
        print(f"Error al crear la DB: {e}")
        

def db_insertar_puntaje(directorio:str, puntaje:int, dificultad:int, nombre:str):
    '''
    Agrega una nueva información a la DB
    '''
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO puntajes VALUES (?, ?, ?)", (puntaje, dificultad, nombre))
    except sqlite3.Error as e:
        print(f"Error al insertar puntaje: {e}")


def db_obtener_puntajes_ordenados(directorio:str) -> list[tuple[int, int, str]]:
    '''
    Abre la DB y retorna una lista de duplas (puntaje, dificultad, nombre) ordenadas descendentemente
    '''
    retorno = []
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute("SELECT puntaje, dificultad, nombre FROM puntajes ORDER BY puntaje DESC, dificultad DESC") # ordena los puntajes en forma descendente y secundariamente por dificultad descendente
            puntajes = c.fetchall()
            retorno = puntajes
    except sqlite3.Error as e:
        print(f"Error al obtener puntajes: {e}")
    
    return retorno

def db_nuevo_top_player(directorio_db:str, puntaje_actual:int, dificultad_actual:int):
    '''
    recibe el puntaje actual y verifica si cumple para entrar al top 5
    retorna true o false
    '''
    top_players = db_obtener_puntajes_ordenados(directorio_db)
    nuevo_top_player = False
    for top_player in top_players[:5]:
        if puntaje_actual > top_player[0] or (puntaje_actual == top_player[0] and dificultad_actual > top_player[1]):
            nuevo_top_player = True
            break

            
    return nuevo_top_player

def armar_directorio_tetris_pygame(nombre_archivo:str, directorio_actual:str = None) -> str:
    '''
    crea el directorio para el workspace correspondiente.

    para otras pcs intercambiar las lineas comentadas
    '''

    # # workspace generico
    # if directorio_actual is None:
    #     directorio_trabajo = os.getcwd()
    #     print(f'armar_directorio_tetris_pygame: {directorio_trabajo}')
    #     directorio_archivo = os.path.join(directorio_trabajo, nombre_archivo)
    # else:
    #     directorio_archivo = os.path.join(directorio_actual, nombre_archivo)

    # return directorio_archivo

    # workspace personalizado
    if directorio_actual is None:
        directorio_trabajo = os.getcwd()
        directorio_archivo = os.path.join(directorio_trabajo, 'lab_1_py', 'tetris_pygame', nombre_archivo)
    else:
        directorio_archivo = os.path.join(directorio_actual, nombre_archivo)

    return directorio_archivo


def mostrar_top_5(directorio, screen):
    '''
    Recibe el directorio de la DB y muestra el top 5 en la pantalla.
    '''
    lista_puntajes = db_obtener_puntajes_ordenados(directorio)
    
    font = pygame.font.Font(None, 36)

   

    # Renderiza los puntajes en la pantalla
    horizontal_textos = 30
    altura_textos = 550
    separacion_textos = 50

    # renderiza un fondo
    pygame.draw.rect(screen, (220, 220, 220), (horizontal_textos - 15, altura_textos - (2 * separacion_textos) - 15 , 500, 347))

     # Renderiza el título en la pantalla
    titulo_renderizado = font.render("Top 5 Puntajes", True, (255, 255, 255))
    screen.blit(titulo_renderizado, (horizontal_textos, altura_textos - 2 * separacion_textos))

    # renderizado de las columnas informativas
    texto = 'score      dificultad      nombre'
    renderizado = font.render(texto, True, (255, 255, 255))
    screen.blit(renderizado, (horizontal_textos, altura_textos - 1 * separacion_textos))
    
    for i in range(min(len(lista_puntajes), 5)):
        score, dificultad, nombre = lista_puntajes[i]
        texto = f'{score}           {dificultad}            {nombre}'
        renderizado = font.render(texto, True, (255, 255, 255))
        screen.blit(renderizado, (horizontal_textos, altura_textos + i * separacion_textos))

    pygame.display.flip()
    pygame.time.delay(5000)


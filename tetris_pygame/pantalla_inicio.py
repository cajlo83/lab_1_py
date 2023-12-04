import pygame

from tetris_funciones import *

from mi_pygame import *

from tetris_archivos import *

from PIL import Image

import sys

def cargar_fondo( dimensiones):
    '''
    carga fondo.jpeg 
    '''
    try:
        ubicacion_fondo = armar_directorio_tetris_pygame("media")
        ruta_fondo = armar_directorio_tetris_pygame("fondo.jpeg", ubicacion_fondo)
        imagen = Image.open(ruta_fondo)
        # Escala la imagen a las dimensiones especificadas
        imagen = imagen.resize(dimensiones, Image.ANTIALIAS)
        # Convierte el formato del GIF para pygame
        pygame_imagen = pygame.image.fromstring(imagen.tobytes(), imagen.size, imagen.mode)
        return pygame_imagen
    except Exception as e:
        print(f"Error al cargar el GIF: {e}")
        return None


# Función principal de la pantalla de inicio
def pantalla_inicio(screen:pygame.surface.Surface, directorio_db:str) -> Configuracion:
    '''
    Se encarga de mostrar un menú al inicio del programa donde se elige la dificultad y la opción de ver el ranking.
    Retorna la configuración de la partida.
    '''

      # Obtener dimensiones de la pantalla
    ancho_pantalla, alto_pantalla = screen.get_size()

    # Cargar el GIF como fondo y escalarlo al tamaño de la pantalla

    fondo_dimensiones = (ancho_pantalla, alto_pantalla)
    fondo = cargar_fondo(fondo_dimensiones)


    font = pygame.font.Font(None, 36)
    fonter = pygame.font.Font(None, 60)



    pos_x = 380
    separacion = 69

    boton_facil = Boton(font, "Facil", pos_x, 160 + (separacion * 0), color_verde, color_rojo )
    boton_normal = Boton(font, "Normal", pos_x, 160 + (separacion * 1), color_verde, color_rojo )
    boton_dificil = Boton(font, "Dificil", pos_x, 160 + (separacion * 2), color_verde, color_rojo )
    boton_progresivo = Boton(font, "Progresivo", pos_x, 160 + (separacion * 3), color_verde, color_rojo )
    boton_ranking = Boton(font, "Ranking", pos_x - 200 , 550, color_rojo, color_verde )
    boton_salir = Boton(font, "Salir", 700, 700, color_texto_gris, color_morado )


    
    continuar = True
    redibujar = True
    while continuar:
         

        
        if redibujar:
                
            screen.blit(fondo, (0, 0))

            # bandeja de jugar
            pygame.draw.rect(screen, color_jugar, (pos_x - 160, 140, 300, 270))
            mostrar_texto(screen, "Jugar:", pos_x - 150, 245, fonter, color_amarillo)

            # mostrar botones
            cuadrado_facil = boton_facil.mostrar(screen)
            cuadrado_normal = boton_normal.mostrar(screen)
            cuadrado_dificil = boton_dificil.mostrar(screen)
            cuadrado_progresivo = boton_progresivo.mostrar(screen)
            cuadrado_ranking = boton_ranking.mostrar(screen)
            cuadrado_salir = boton_salir.mostrar(screen)

            pygame.display.flip()
            redibujar = False


        # lectura e interpretacion de eventos
        permanecer, tecla_pulsada, (x, y) = leer_evento()

        if not permanecer:
            pygame.quit()
            sys.exit()
        elif x and y:
            if cuadrado_facil.collidepoint(x, y):
                dificultad = 1
                continuar = False
            elif cuadrado_normal.collidepoint(x, y):
                dificultad = 2
                continuar = False
            elif cuadrado_dificil.collidepoint(x, y):
                dificultad = 3
                continuar = False
            elif cuadrado_progresivo.collidepoint(x, y):
                dificultad = 4
                continuar = False
            elif cuadrado_ranking.collidepoint(x, y):
                mostrar_top_5(directorio_db, screen)
                redibujar = True
            elif cuadrado_salir.collidepoint(x, y):
                pygame.quit()
                sys.exit()

    limite_movimientos_por_segundo = 4 * dificultad
    ancho_espacio_jugable = 250
    
    return config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad)


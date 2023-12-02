import pygame

from tetris_funciones import *

from tetris_archivos import *

from PIL import Image

import sys





# Función para mostrar texto en la pantalla
def mostrar_texto(screen, texto, x, y, font, color):
    texto_renderizado = font.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))



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
    largo_x = 140
    pos_salir = (700, 700, 80, 50)  # Coordenadas y dimensiones del botón "Salir"


    
    continuar = True
    while continuar:
         
        screen.blit(fondo, (0, 0))

        # Dibujar botones
        pygame.draw.rect(screen, color_jugar, (pos_x - 160, 140, largo_x + 170, 270))
        pygame.draw.rect(screen, color_blanco, (pos_x, 150, largo_x, 50))
        pygame.draw.rect(screen, color_blanco, (pos_x, 250, largo_x, 50))
        pygame.draw.rect(screen, color_blanco, (pos_x, 350, largo_x, 50))
        pygame.draw.rect(screen, color_blanco, (pos_x + 170, 300, 170, 50))
        pygame.draw.rect(screen, color_blanco, pos_salir)  # Dibujar botón "Salir"



        # Mostrar texto en botones y titulo
        mostrar_texto(screen, "Jugar:", pos_x - 150, 245, fonter, color_texto_gris)
        mostrar_texto(screen, "Fácil", pos_x + 10, 160, font, color_texto_gris)
        mostrar_texto(screen, "Normal", pos_x + 10, 260, font, color_texto_gris)
        mostrar_texto(screen, "Difícil", pos_x + 10, 360, font, color_texto_gris)
        mostrar_texto(screen, "Ranking", pos_x + 200, 310, font, color_texto_gris)
        mostrar_texto(screen, "Salir", pos_salir[0] + 10, pos_salir[1] + 10, font, color_texto_gris)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pos_x <= x <= (pos_x + largo_x):
                    if 150 <= y <= 200:
                        dificultad = 1
                        continuar = False
                    elif 250 <= y <= 300:
                        dificultad = 2
                        continuar = False
                    elif 350 <= y <= 400:
                        dificultad = 3
                        continuar = False
                    elif 450 <= y <= 500:
                        mostrar_top_5(directorio_db, screen)
                elif (pos_x + 170) <= x <= (pos_x + 170 + 170) and 300 <= y <= (300 + 50):
                    mostrar_top_5(directorio_db, screen)

                elif pos_salir[0] <= x <= (pos_salir[0] + pos_salir[2]) and pos_salir[1] <= y <= (pos_salir[1] + pos_salir[3]):
                    pygame.quit()
                    sys.exit()

    limite_movimientos_por_segundo = 4 * dificultad
    ancho_espacio_jugable = 250
    
    return config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad)


# Función para visualizar puntajes
def visualizar_puntajes():
    print("Mostrando puntajes")


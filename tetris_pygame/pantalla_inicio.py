import pygame
from tetris_funciones import *
from tetris_archivos import *
import sys

# Función para mostrar texto en la pantalla
def mostrar_texto(screen, texto, x, y, font, color):
    texto_renderizado = font.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))

# Función principal de la pantalla de inicio
def pantalla_inicio(screen) -> Configuracion:
    '''
    se encarga de mostrar un menu al inicio del programa donde se elije la dificultad y la opcion de ver el ranking
    '''



   
    
    font = pygame.font.Font(None, 36)

    continuar = True
    while continuar:
        screen.fill(color_negro)

        # Dibujar botones
        pygame.draw.rect(screen, color_blanco, (300, 150, 200, 50))
        pygame.draw.rect(screen, color_blanco, (300, 250, 200, 50))
        pygame.draw.rect(screen, color_blanco, (300, 350, 200, 50))
        pygame.draw.rect(screen, color_blanco, (300, 450, 200, 50))

        # Mostrar texto en botones
        mostrar_texto(screen, "Jugar Fácil", 350, 160, font, color_texto_gris)
        mostrar_texto(screen, "Jugar Normal", 340, 260, font, color_texto_gris)
        mostrar_texto(screen, "Jugar Difícil", 340, 360, font, color_texto_gris)
        mostrar_texto(screen, "Mostrar Ranking", 330, 460, font, color_texto_gris)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 300 <= x <= 500:
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
                        visualizar_puntajes()
        


    limite_movimientos_por_segundo = 4 * dificultad
    ancho_espacio_jugable = 250
    
    return config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad )


# Función para visualizar puntajes
def visualizar_puntajes():
    print("Mostrando puntajes")


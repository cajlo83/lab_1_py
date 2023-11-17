'''
tetris en pygame
autor: Carlo Morici
'''

import pygame
import sys
import time
#import entorno
from configuraciones_juego import *
from objetos_tetris import *
from colores import *


# Inicializar Pygame
pygame.init()

# datos de la partida
modalidad_juego = "CLA"

# limitar FPS para disminuir carga de CPU (1/2)


# Inicializar el reloj de Pygame
reloj = pygame.time.Clock()

# Configuración de la ventana del programa
screen = crear_ventana(800, 600, "tetris pygame Carlo Morici")



# datos de configuracion
dificultad = 1
limite_movimientos_por_segundo = 5 
ancho_espacio_jugable = 250
config = config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad )


matriz_grilla = config.crear_grilla()
matriz_esquinas = config.crear_puntos()

figura_jugador = crear_figura(config)
#           puntaje = 0


# inicializacion pared de bloques
pared_juegos = crear_pared(modalidad_juego, config)

# inicializar tiempo_anterior antes del bucle
tiempo_anterior = time.time()


tocar_fondo = False
# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # se controla la cantidad de movimientos con conteos de tiempo
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_anterior



    # Obtener las teclas presionadas para moverse sin salir del espacio jugable, solo si se cumplio el tiempo establecido entre pulsaciones
    if config.tiempo_entre_pulsos(tiempo_transcurrido):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] : # izquierda
            tiempo_anterior = tiempo_actual # TIEMPO
            figura_mover("HOR", figura_jugador, pared_juegos, -config.dimension_bloque)
            

        if keys[pygame.K_RIGHT] : # derecha 
            tiempo_anterior = tiempo_actual # TIEMPO
            figura_mover("HOR", figura_jugador, pared_juegos, config.dimension_bloque)

            
        if keys[pygame.K_DOWN]: # abajo
            tiempo_anterior = tiempo_actual # TIEMPO
            tocar_fondo = figura_mover("VER", figura_jugador, pared_juegos, config.dimension_bloque)

          

    # en cada ciclo, el movil debe moverse hacia abajo. la velocidad cambia segun la dificultad
    tocar_fondo = figura_mover("VER", figura_jugador, pared_juegos, config.dificultad)

    # verifica un toque te tope
    if tocar_fondo == True: 
        # integrar bloques a la pared
        pared_juegos.agregar_bloques_desde_figura(figura_jugador)
        # chequear si hay filas ganadoras
        lista_ganadores = pared_juegos.verificar_ganadores()
        # asignar puntos 


        # crear nueva figura para el jugador
        figura_jugador = crear_figura(config)




    ########### Dibujar la pantalla ###########
    screen.fill(color_fondo_ventana) # fondo

    # espacio jugable
    pygame.draw.rect(screen, color_gris_oscuro, config.espacio_jugable) # rectangulo


    # se representa graficamente al jugador en pantalla
    figura_jugador.mostrar(screen) 

    # se muestran los bloques de la pared
    pared_juegos.mostrar(screen)

    # elementos esteticos
    mostrar_grilla(matriz_grilla,screen) # grilla
    mostrar_puntos(matriz_esquinas, screen, 3) # esquinas

    # textos

    config.mostrar_titulo(screen)

    pygame.display.flip() # bufer de pantalla

    # limitar FPS para disminuir carga de CPU (2/2)
    reloj.tick(config.fps)

# Salir de Pygame
pygame.quit()
sys.exit()
'''
tetris en pygame
autor: Carlo Morici
'''

import pygame
import sys
#import entorno
from tetris_funciones import *
from colores import *


# Inicializar Pygame
pygame.init()

# datos de la partida
modalidad_juego = "CLA"

# limitar FPS para disminuir carga de CPU (1/2)



# Configuración de la ventana del programa
screen = crear_ventana(800, 600, "tetris pygame Carlo Morici")



# datos de configuracion
dificultad = 5
limite_movimientos_por_segundo = 3 
ancho_espacio_jugable = 250
config = config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad )


matriz_grilla = config.crear_grilla()
matriz_esquinas = config.crear_puntos()

figura_jugador = crear_figura(config)

# inicializacion pared de bloques
pared_juegos = crear_pared(modalidad_juego, config)




tocar_fondo = False
# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # se controla la cantidad de movimientos con conteos de tiempo
    config.tiempo.actualiza_tiempo_actual()
    config.tiempo.actualiza_tiempo_transcurrido()
    

    tocar_fondo = interaccion_teclado(config, pared_juegos, figura_jugador)

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
    config.mostrar_espacio_jugable(screen)


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
    config.tiempo.limitar_fps()

# Salir de Pygame
pygame.quit()
sys.exit()
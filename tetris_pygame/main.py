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
screen = crear_ventana(800, 800, "tetris pygame Carlo Morici")



# datos de configuracion
dificultad = 1
limite_movimientos_por_segundo = 3 
ancho_espacio_jugable = 250
config = config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad )


matriz_grilla = config.crear_grilla()
matriz_esquinas = config.crear_puntos()

figura_jugador = crear_figura(config)

# inicializacion pared de bloques
pared_juegos = crear_pared(modalidad_juego, config)



print(f'fondo espacio jugable == {config.espacio_jugable.bottom}')

# inicio del cronometro
config.tiempo.actualiza_cronometro_inicio()
# Bucle principal
running = True
while running:

    # se leen eventos
    tupla_eventos = leer_evento()
    running = tupla_eventos[0] # se verifica continuidad del bucle
    tecla_pulsada = tupla_eventos[1] # se verifica actividad del teclado


    # se controla la cantidad de movimientos con conteos de tiempo
    config.tiempo.actualiza_tiempo_actual()
    config.tiempo.actualiza_tiempo_transcurrido()
    

    tocar_fondo_manual = interaccion_teclado(config, tecla_pulsada, pared_juegos, figura_jugador)

    # en cada ciclo, el movil debe moverse hacia abajo. la velocidad cambia segun la dificultad
    tocar_fondo_automatico = figura_mover("VER", figura_jugador, pared_juegos, config.dificultad)

    # verifica un toque te tope
    if tocar_fondo_manual or tocar_fondo_automatico: 

        # integrar bloques a la pared, verificar que no se integre un bloque fuera de lugar
        game_over = pared_juegos.agregar_bloques_desde_figura(figura_jugador) 
        if game_over:
            print("\t\tGAME OVER :C")
        else:
            print("\t\tGAME CONTINUE C:")

        # buscar filas ganadoras
        lista_ganadores = pared_juegos.verificar_ganadores()
        # borrar filas ganadoras
        puntaje_subida = pared_juegos.eliminar_filas(lista_ganadores)
        # subir puntos 
        config.subir_puntuacion(puntaje_subida)

        # crear nueva figura para el jugador
        figura_jugador = crear_figura(config)



    ########### Dibujar la pantalla ###########

    # cronometro
    config.cronometro(screen)

    # fondo ventana
    screen.fill(color_fondo_ventana) # fondo

    # espacio seguro
    config.mostrar_espacio_jugable(screen)

    # espacio jugable
    config.mostrar_espacio_seguro(screen)


    # se representa graficamente al jugador en pantalla
    figura_jugador.mostrar(screen) 

    # se muestran los bloques de la pared
    pared_juegos.mostrar(screen)

    # elementos esteticos
    mostrar_grilla(matriz_grilla,screen) # grilla
    mostrar_puntos(matriz_esquinas, screen, 3) # esquinas

    # textos
    config.cronometro(screen)
    config.mensajes_pantalla.mostrar_titulo(screen)
    config.mensajes_pantalla.mostrar_puntaje(screen)

    pygame.display.flip() # bufer de pantalla

    # limitar FPS para disminuir carga de CPU (2/2)
    config.tiempo.limitar_fps()

# Salir de Pygame
pygame.quit()
sys.exit()
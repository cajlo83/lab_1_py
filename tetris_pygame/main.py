'''
tetris en pygame
autor: Carlo Morici
'''

import pygame
import sys
#import entorno
from tetris_funciones import *
from colores import *
from tetris_archivos import *

# Inicializar Pygame
pygame.init()
pygame.mixer.init()


# datos de la partida
modalidad_juego = "CLA"

# obtener directorio_db
directorio_db = armar_directorio_tetris_pygame("prueba_db_puntajes.db")
# se crea la DB en caso que no exista
db_crear(directorio_db)

# Configuración de la ventana del programa
screen = crear_ventana(800, 800, "tetris pygame Carlo Morici")

# datos de configuracion
dificultad = 3
limite_movimientos_por_segundo = 4 * dificultad
ancho_espacio_jugable = 250
config = config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad )

# estetica
matriz_grilla = config.crear_grilla()
matriz_esquinas = config.crear_puntos()

# player
figura_jugador = crear_figura(config)

# inicializacion pared de bloques
pared_juegos = crear_pared(modalidad_juego, config)



# inicializa y reproduce sonido
media = crear_media()
media.reproducir(config.dificultad)



# inicio del cronometro
config.tiempo.actualiza_cronometro_inicio()
# Bucle principal
running = True
pausa = False
game_over = False
while running:

    # se leen eventos
    tupla_eventos = leer_evento()
    running = tupla_eventos[0] # se verifica continuidad del bucle
    tecla_pulsada = tupla_eventos[1] # se verifica actividad del teclado
    click_pulsado = tupla_eventos[2] # se verifica actividad del mouse


    # control de sonido via mouse
    media.controlar(click_pulsado)

    # pausa
    if not game_over:
        pausa = config.estado_pausa(pausa, tecla_pulsada)

            
    if not pausa:

        # se controlan datos de tiempo
        config.tiempo.actualiza_tiempo_actual()
        config.tiempo.actualiza_tiempo_transcurrido()
        config.tiempo.actualiza_cronometro_avance()
        
        # control del jugador via teclado
        tocar_fondo_manual = controles_juego(config, tecla_pulsada, pared_juegos, figura_jugador)


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

    # fondo ventana
    screen.fill(color_fondo_ventana) # fondo

    # controles de sonido
    media.dibujar_volumen_barra(screen)
    media.boton_pausa_play.mostrar(screen)

    #dependen del juego en ejecucion:
    config.mensajes_pantalla.mostrar_puntaje(screen)
    # dependen del game over
    if game_over:
        config.mensajes_pantalla.mostrar_titulo(screen, "GAME OVER")
        nombre_player = config.mensajes_pantalla.pedir_texto(screen, "ingrese un ID entre 3 y 8 caracteres:     ", 100, 400)
        db_insertar_puntaje(directorio_db, config.mensajes_pantalla.entero_puntaje, config.dificultad, nombre_player)
        mostrar_top_5(directorio_db)
        break # salir del bucle principal

        # print(f'el jugador es: {nombre_player} y su score: {config.mensajes_pantalla.entero_puntaje}')
    
    else:
        # espacios
        config.espacio_seguro.mostrar(screen)
        config.espacio_jugable.mostrar(screen)
            
        # dependen de la pausa:
        if not(pausa):
            # textos en pantalla
            config.mensajes_pantalla.mostrar_titulo(screen)
            config.mostrar_cronometro(screen) # evitemos bugs
            
            # gameplaying no se muestra durante la pausa, aqui no toleramos tramposos
            figura_jugador.mostrar(screen) 
            pared_juegos.mostrar(screen)
        else:
            config.mensajes_pantalla.mostrar_titulo(screen, "PAUSA")
        
        # elementos esteticos se dibujan de ultimo
        mostrar_grilla(matriz_grilla,screen) # grilla
        mostrar_puntos(matriz_esquinas, screen, 3) # esquinas

    pygame.display.flip() # bufer de pantalla

    # limitar FPS para disminuir carga de CPU (2/2)
    config.tiempo.limitar_fps()

# Salir de Pygame
pygame.quit()
sys.exit()
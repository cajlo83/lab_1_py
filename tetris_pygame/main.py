import pygame
import sys
from tetris_funciones import *
from colores import *
from tetris_archivos import *
from pantalla_inicio import *

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Datos de la partida
modalidad_juego = "CLA"
directorio_db = armar_directorio_tetris_pygame("prueba_db_puntajes.db")
db_crear(directorio_db)

# Configuración de la ventana del programa
screen = crear_ventana(800, 800, "tetris pygame Carlo Morici")

# Bucle principal
running, menu = True, True

while running:
    if menu:
        config = pantalla_inicio(screen, directorio_db)

        # Luego de la pantalla de inicio
        matriz_grilla, matriz_esquinas = config.crear_grilla(), config.crear_puntos()
        figura_jugador = crear_figura(config)
        pared_juegos = crear_pared(modalidad_juego, config)
        media = crear_media()
        media.reproducir(config.dificultad)
        config.tiempo.actualiza_cronometro_inicio()
        limite_segundos = 100
        menu, pausa, game_over, nuevo_top_player = False, False, False, False

    else:
        tupla_eventos = leer_evento()
        running, tecla_pulsada, click_pulsado = tupla_eventos

        media.controlar(click_pulsado)
        if not game_over:
            pausa = config.estado_pausa(pausa, tecla_pulsada)

        if not pausa:
            config.tiempo.actualiza_tiempo_actual()
            config.tiempo.actualiza_tiempo_transcurrido()
            avance_cronometro = config.tiempo.actualiza_cronometro_avance()
            tocar_fondo_manual = controles_juego(config, tecla_pulsada, pared_juegos, figura_jugador)
            tocar_fondo_automatico = figura_mover("VER", figura_jugador, pared_juegos, config.dificultad)
            game_over = (avance_cronometro > limite_segundos)
            

        if (tocar_fondo_manual or tocar_fondo_automatico) and not game_over:

            game_over = pared_juegos.agregar_bloques_desde_figura(figura_jugador) 
            
            if not game_over:
                lista_ganadores = pared_juegos.verificar_ganadores()
                puntaje_subida = pared_juegos.eliminar_filas(lista_ganadores)
                limite_segundos += puntaje_subida * 3 # se aumenta el limite de tiempo en 3 segundos por cada fila eliminada
                config.subir_puntuacion(puntaje_subida)
                figura_jugador = crear_figura(config)

        # Dibujar la pantalla
        screen.fill(color_fondo_ventana)
        media.dibujar_volumen_barra(screen)
        media.boton_pausa_play.mostrar(screen)
        config.mensajes_pantalla.mostrar_puntaje(screen)

        if game_over:
            config.mensajes_pantalla.mostrar_titulo(screen, "¡¡¡¡¡¡¡¡¡¡GAME OVER!!!!!!!!!!")
            
            # top_players = db_obtener_puntajes_ordenados(directorio_db)
            # nuevo_top_player = False
            # for top_player in top_players[:5]:
            #     if config.mensajes_pantalla.entero_puntaje > top_players[0]:
            #         nuevo_top_player = True
            #         break
            
            nuevo_top_player = db_nuevo_top_player(directorio_db, config.mensajes_pantalla.entero_puntaje, config.dificultad)

            if nuevo_top_player:
                nombre_player = config.mensajes_pantalla.pedir_texto(screen, "ingrese un nombre entre 3 y 8 caracteres: ", 100, 400)
                db_insertar_puntaje(directorio_db, config.mensajes_pantalla.entero_puntaje, config.dificultad, nombre_player)
                mostrar_top_5(directorio_db, screen)
            
            
            
            # en caso de game over y no ser top player se muestra la pantalla por unos segundos para ver resultados finales
            elif not nuevo_top_player:
                pygame.display.flip()
                pygame.time.delay(5000)

            pygame.mixer.music.stop()
            menu, game_over = True, False
        else:
            config.espacio_seguro.mostrar(screen)
            config.espacio_jugable.mostrar(screen)
            if not pausa:
                config.mensajes_pantalla.mostrar_titulo(screen)
                config.mostrar_cronometro(screen, limite_segundos)
                figura_jugador.mostrar(screen)
                pared_juegos.mostrar(screen)
            else:
                config.mensajes_pantalla.mostrar_titulo(screen, "PAUSA")

            mostrar_grilla(matriz_grilla, screen)
            mostrar_puntos(matriz_esquinas, screen, 3)

        pygame.display.flip()
        

            
        config.tiempo.limitar_fps()


# Salir de Pygame
pygame.quit()
sys.exit()
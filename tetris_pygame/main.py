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

segundos_subida = 1000 * 5 # aumento de tiempo al sumar puntos

while running:
    if menu:
        ####################### menu inicial
        config = pantalla_inicio(screen, directorio_db)

        # Luego de la pantalla de inicio
        matriz_grilla, matriz_esquinas = config.crear_grilla(), config.crear_puntos()
        figura_jugador = crear_figura(config)
        pared_juegos = crear_pared(modalidad_juego, config)
        media = crear_media()
        media.reproducir(config.dificultad)
        config.tiempo.actualiza_cronometro_inicio()
        config.tiempo.actualiza_cronometro_fin()
        menu, pausa, game_over, nuevo_top_player = False, False, False, False

    else:

        ############################### Juego
        running, tecla_pulsada, click_pulsado = leer_evento()
        media.controlar(click_pulsado)
        if not game_over:
            pausa = config.estado_pausa(pausa, tecla_pulsada)

        if not pausa:
            config.tiempo.actualiza_tiempo_actual_interacciones()
            config.tiempo.actualiza_tiempo_transcurrido_interacciones()
            tocar_fondo_manual = controles_juego(config, tecla_pulsada, pared_juegos, figura_jugador)
            if config.dificultad == 4: # sube la velocidad a cada minuto
                velocidad_bajada =  ((pygame.time.get_ticks() - config.tiempo.cronometro_inicio) // (60000)) + 1 # milisegundos / (1000 * 60) = minutos
                tocar_fondo_automatico = figura_mover("VER", figura_jugador, pared_juegos, velocidad_bajada)

            else:
                tocar_fondo_automatico = figura_mover("VER", figura_jugador, pared_juegos, config.dificultad)
            game_over = config.tiempo.avanzar_cronometro()
            

        if (tocar_fondo_manual or tocar_fondo_automatico) and not game_over:
            game_over = pared_juegos.agregar_bloques_desde_figura(figura_jugador) 
            
            if not game_over:
                lista_ganadores = pared_juegos.verificar_ganadores()
                puntaje_subida = pared_juegos.eliminar_filas(lista_ganadores)
                config.tiempo.actualiza_cronometro_fin( puntaje_subida * segundos_subida ) # se aumenta el limite de tiempo segun cada fila eliminada
                config.subir_puntuacion(puntaje_subida)
                figura_jugador = crear_figura(config)






        ############################# Dibujos en pantalla
        screen.fill(color_fondo_ventana)
        config.mensajes_pantalla.mostrar_puntaje(screen)

        if game_over:
            config.mensajes_pantalla.mostrar_titulo(screen, "¡¡¡¡¡¡¡¡¡¡GAME OVER!!!!!!!!!!")
            nuevo_top_player = db_nuevo_top_player(directorio_db, config.mensajes_pantalla.entero_puntaje, config.dificultad)

            if nuevo_top_player:
                nombre_player = config.mensajes_pantalla.pedir_texto(screen, "ingrese un nombre entre 3 y 8 caracteres: ", 100, 400)
                db_insertar_puntaje(directorio_db, config.mensajes_pantalla.entero_puntaje, config.dificultad, nombre_player)
                mostrar_top_5(directorio_db, screen)                        
            else: # en caso de game over y no ser top player se muestra la pantalla por unos segundos para ver score final
                pygame.display.flip()
                pygame.time.delay(5000)

            pygame.mixer.music.stop()
            menu, game_over = True, False
        else:
            
            media.mostrar_panel_audio(screen, color_sonido)
            config.espacio_seguro.mostrar(screen)
            config.espacio_jugable.mostrar(screen)
            if not pausa:
                config.mensajes_pantalla.mostrar_titulo(screen)
                config.mostrar_cronometro(screen)
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
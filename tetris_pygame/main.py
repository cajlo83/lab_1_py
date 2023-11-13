import pygame
import sys
import time
import espacio_para_jugar
import background
from objetos_tetris import *
from colores import *


# Inicializar Pygame
pygame.init()

# datos de la partida
modalidad_juego = "CLA"
dificultad = 1

# limitar FPS para disminuir carga de CPU (1/2)
limite_fps = 30

# Inicializar el reloj de Pygame
reloj = pygame.time.Clock()

# Configuración de la ventana del programa
screen = background.crear_ventana(800, 600, "tetris pygame Carlo Morici")

# Establecer parametros de tamaño y movimiento
ancho_espacio_jugable = 250
alto_espacio_jugable = 2 * ancho_espacio_jugable
dim_bloques = int (ancho_espacio_jugable / 10)
limite_movimientos_por_segundo = 3  
tiempo_entre_movimientos = 0.5 / limite_movimientos_por_segundo

# espacio jugable, su posicion, su tamaño y la grilla
espacio_jugable = pygame.Rect(50, 30, ancho_espacio_jugable, alto_espacio_jugable)
lista_grilla = espacio_para_jugar.crear_grilla(espacio_jugable, dim_bloques)
matriz_esquinas = espacio_para_jugar.crear_puntos_grilla(espacio_jugable, dim_bloques)



# datos iniciales del jugador
x_jugador = (espacio_jugable.left + espacio_jugable.right) / 2 - dim_bloques
y_jugador = espacio_jugable.top
figura_jugador = crear_figura(color_morado,dim_bloques,x_jugador, y_jugador)


# inicializacion pared de bloques
pared_bloques = crear_pared(modalidad_juego, espacio_jugable, dim_bloques)




# Texto a mostrar en pantalla
fuente_texto = pygame.font.Font(None, 36)
texto_titulo = fuente_texto.render("Juguemos al tetris", True, color_morado)

# inicializar tiempo_anterior antes del bucle
tiempo_anterior = time.time()

tope_derecha = espacio_jugable.right- dim_bloques
tope_izquierda = espacio_jugable.left


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # se controla la cantidad de movimientos con conteos de tiempo
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_anterior

    # se detecta el/los topes
    tope_inferior = pared_bloques.calcular_tope(espacio_jugable, dim_bloques)


    # Obtener las teclas presionadas para moverse sin salir del espacio jugable, solo si se cumplio el tiempo establecido entre pulsaciones
    if tiempo_transcurrido >= tiempo_entre_movimientos:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: # izquierda
            figura_jugador.trasladar("izquierda", dim_bloques,tope_izquierda)
            tiempo_anterior = tiempo_actual

        if keys[pygame.K_RIGHT]: # derecha 
            figura_jugador.trasladar("derecha", dim_bloques, tope_derecha)
            tiempo_anterior = tiempo_actual
    
        if keys[pygame.K_DOWN]: # abajo
            tocar_tope = figura_jugador.bajar(dim_bloques, tope_inferior)
            tiempo_anterior = tiempo_actual
            
              
                

    # en cada ciclo, el movil debe moverse hacia abajo. la velocidad cambia segun la dificultad
    tocar_tope = figura_jugador.bajar(dificultad, tope_inferior)
    
    # verifica un toque te tope
    if tocar_tope: #asignar puntos 
        # crear nueva figura para el jugador
        figura_jugador = crear_figura(color_morado,dim_bloques,x_jugador, y_jugador)





    ########### Dibujar la pantalla ###########
    screen.fill(color_blanco) # fondo

    # espacio jugable
    pygame.draw.rect(screen, color_rojo, espacio_jugable) # rectangulo

    
    # se representa graficamente al jugador en pantalla
    figura_jugador.mostrar(screen) 

    # elementos esteticos
    if not espacio_para_jugar.mostrar_grilla(lista_grilla,screen): # grilla
        print("error mostrando grilla")
    if not espacio_para_jugar.mostrar_puntos(matriz_esquinas, screen, 3): # esquinas
        print("error mostrando puntos")

    # textos
    screen.blit(texto_titulo, (screen.get_width() // 2 - texto_titulo.get_width() // 2, 8)) # titulo

    pygame.display.flip() # bufer de pantalla

    # limitar FPS para disminuir carga de CPU (2/2)
    reloj.tick(limite_fps)

# Salir de Pygame
pygame.quit()
sys.exit()

import pygame

from tetris_funciones import *

from tetris_archivos import *

from PIL import Image

import sys





# Función para mostrar texto en la pantalla
def mostrar_texto(screen:pygame.surface.Surface, texto:str, x:int, y:int, font:pygame.font.Font, color:tuple[int,int,int]) -> pygame.rect.Rect:
    '''
    muestra un texto y retorna un rectangulo con datos de ancho y alto que ocupa en la pantalla
    '''
    texto_renderizado = font.render(texto, True, color)
    screen.blit(texto_renderizado, (x, y))
    return texto_renderizado.get_rect()


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


class Boton:
    def __init__(self, fuente:pygame.font.Font, texto:str, x_texto:int, y_texto:int, color_texto:tuple[int, int, int], color_cuadrado:tuple[int, int, int] ) -> None:
        self.fuente = fuente
        self.texto = texto
        self.x_texto = x_texto
        self.y_texto = y_texto
        self.color_texto = color_texto
        self.color_cuadrado = color_cuadrado

    def mostrar(self,screen:pygame.surface.Surface) -> pygame.rect.Rect:

        # se renderiza texto para extraer el valor de su rectangulo y crear un rectangulo mas grande a su alrededor
        texto_renderizado = self.fuente.render(self.texto, True, self.color_texto)
        cuadrado_texto = texto_renderizado.get_rect()
        rectangulo_boton = pygame.rect.Rect( (self.x_texto - 5), (self.y_texto - 5), cuadrado_texto.width + 10, cuadrado_texto.height + 10 )

        # se dibujan el cuadrado y el texto
        pygame.draw.rect(screen, self.color_cuadrado, rectangulo_boton )
        screen.blit(texto_renderizado, (self.x_texto, self.y_texto))
        
        # se retorna el cuadrado del boton
        return rectangulo_boton


 



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
  

    boton_facil = Boton(font, "Facil", pos_x, 160, color_texto_azul, color_amarillo )
    boton_normal = Boton(font, "Normal", pos_x, 260, color_texto_azul, color_amarillo )
    boton_dificil = Boton(font, "Dificil", pos_x, 360, color_texto_azul, color_amarillo )
    boton_ranking = Boton(font, "Ranking", pos_x - 200 , 550, color_texto_gris, color_verde )
    boton_salir = Boton(font, "Salir", 700, 700, color_texto_gris, color_morado )

    
    continuar = True
    redibujar = True
    while continuar:
         

        
        if redibujar:
                
            screen.blit(fondo, (0, 0))

            # bandeja de jugar
            pygame.draw.rect(screen, color_jugar, (pos_x - 160, 140, 300, 270))
            mostrar_texto(screen, "Jugar:", pos_x - 150, 245, fonter, color_texto_gris)

            # mostrar botones
            cuadrado_facil = boton_facil.mostrar(screen)
            cuadrado_normal = boton_normal.mostrar(screen)
            cuadrado_dificil = boton_dificil.mostrar(screen)
            cuadrado_ranking = boton_ranking.mostrar(screen)
            cuadrado_salir = boton_salir.mostrar(screen)

            pygame.display.flip()
            redibujar = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print(f'coordenadas raton : ({x},{y})')
                if cuadrado_facil.left <= x <= cuadrado_facil.right and cuadrado_facil.top <= y <= cuadrado_facil.bottom:
                    dificultad = 1
                    continuar = False
                elif cuadrado_normal.left <= x <= cuadrado_normal.right and cuadrado_normal.top <= y <= cuadrado_normal.bottom:
                    dificultad = 2
                    continuar = False
                elif cuadrado_dificil.left <= x <= cuadrado_dificil.right and cuadrado_dificil.top <= y <= cuadrado_dificil.bottom:
                    dificultad = 3
                    continuar = False
                elif cuadrado_ranking.left <= x <= cuadrado_ranking.right and cuadrado_ranking.top <= y <= cuadrado_ranking.bottom:
                    mostrar_top_5(directorio_db, screen)
                    redibujar = True
                elif cuadrado_salir.left <= x <= cuadrado_salir.right and cuadrado_salir.top <= y <= cuadrado_salir.bottom:
                    pygame.quit()
                    sys.exit()

                #     sys.exit()

    limite_movimientos_por_segundo = 4 * dificultad
    ancho_espacio_jugable = 250
    
    return config_crear(ancho_espacio_jugable, limite_movimientos_por_segundo, dificultad)


# Función para visualizar puntajes
def visualizar_puntajes():
    print("Mostrando puntajes")


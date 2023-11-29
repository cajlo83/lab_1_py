import pygame
import sys
import time
import typing
from colores import *
from tetris_objetos import *
import time



class Tiempos:
    def __init__(self, reloj:pygame.time.Clock, tiempo_entre_movimientos:float, tiempo_actual:float, tiempo_transcurrido:float, tiempo_anterior:float, fps:int, conometro_inicio:int, cronometro_avance:int, pausa_inicio:int ):
        self.reloj = reloj #
        self.tiempo_actual = tiempo_actual
        self.tiempo_transcurrido = tiempo_transcurrido
        self.tiempo_anterior = tiempo_anterior #
        self.tiempo_entre_movimientos = tiempo_entre_movimientos
        self.fps = fps #
        self.conometro_inicio = conometro_inicio
        self.cronometro_avance = cronometro_avance
        self.pausa_inicio = pausa_inicio

    def leer_evento(self) -> bool:
        return self.tiempo_transcurrido >= self.tiempo_entre_movimientos
    
    def limitar_fps(self):
        self.reloj.tick(self.fps)

    def actualiza_tiempo_anterior(self):
        self.tiempo_anterior = self.tiempo_actual

    def actualiza_tiempo_actual(self):
        self.tiempo_actual = time.time()

    def actualiza_tiempo_transcurrido(self):
        self.tiempo_transcurrido = self.tiempo_actual - self.tiempo_anterior
    
    def actualiza_cronometro_inicio(self):
        self.conometro_inicio = pygame.time.get_ticks()
    
    def actualiza_cronometro_avance(self) -> int:
        '''
        actualiza el cronometro y retorna su valor en milisegundos
        '''
        self.cronometro_avance = (pygame.time.get_ticks() - self.conometro_inicio) // 1000
        return self.cronometro_avance
    
    def inicia_pausa(self):
        self.pausa_inicio = pygame.time.get_ticks()

    def termina_pausa(self) -> int:
        '''
        se suma el tiempo de pausa a la hora de inicio de ejecucion para tapar el desfase de tiempo causado por el estado de pausa
        '''

        hora_actual = pygame.time.get_ticks()
        tiempo_transcurrido = hora_actual - self.pausa_inicio
        self.conometro_inicio += tiempo_transcurrido
        

class MensajesPantalla:
    def __init__(self,fuente_texto:pygame.font.Font, texto_titulo:str, entero_puntaje:int, tupla_cronometro:tuple[int,int] ) -> None:
        self.fuente_texto = fuente_texto
        self.texto_titulo = texto_titulo
        self.entero_puntaje = entero_puntaje
        self.tupla_cronometro = tupla_cronometro
        

    def mostrar_titulo(self, screen:pygame.surface.Surface, texto_alternativo:str = None):
       
        if valida_lista(texto_alternativo, 1, True):
            texto_salida = self.fuente_texto.render(texto_alternativo , True, color_negro)
        else:
            texto_salida = self.fuente_texto.render(self.texto_titulo , True, color_texto_gris)

        screen.blit(texto_salida, ( screen.get_width() // 2 - texto_salida.get_width() // 2, 8 ) ) # centrado al medio horizontal, 8 de altura

        
    def pedir_texto(self, screen:pygame.surface.Surface, cadena_informativa:str, x:int, y:int) -> str:
        '''
        muestra un cuadro en pantalla solicitando ingresar datos por teclado
        '''
        pantalla_anterior = screen.copy() # copiar la pantalla antes del inicio de la funcion

        # if valida_lista(cadena_informativa, 1, True):
        #     texto_salida = self.fuente_texto.render(cadena_informativa , False , color_negro, color_blanco)
        #     screen.blit(texto_salida, ( x, y ) ) 

        if valida_lista(cadena_informativa, 1, True):
                
            text = ""
            # bucle para recibir datos de teclado y mostrar su cambio a medida que se detectan
            continuar = True
            while continuar:
                for event in pygame.event.get(): # salida de pygame
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN: # tecla enter para terminar etapa de ingreso de datos
                        if event.key == pygame.K_RETURN:
                            # Guardar la puntuación
                            #guardar_puntuacion(text, puntuacion)
                            if valida_lista(text, 3, True): # text debe ser almenos de longitud 3 antes de poder salir
                                continuar = False
                            else: 
                                print("la palabra en text es aun muy corta")

                        elif event.key == pygame.K_BACKSPACE: # tecla borrar
                            text = text[:-1]     
                            screen.blit(pantalla_anterior, (0,0)) # se coloca una copia de la pantalla anterior antes de mostrar cambios por borrado

                        else: # demas teclas
                            if event.unicode.isalnum(): # solo tomar caracteres alfanumericos
                                text += event.unicode

                #screen.fill((255, 255, 255))

                # Renderizar el texto
                input_text = self.fuente_texto.render(f'{cadena_informativa}{text}', False, color_texto_gris, color_blanco)
                screen.blit(input_text, (x, y))

                pygame.display.flip()

            return text[:8] # retorna solo los primeros 8 caracteres


        
    def mostrar_puntaje(self, screen:pygame.surface.Surface):
       
        cadena_salida = f'puntuacion actual: {self.entero_puntaje}'
        texto_salida = self.fuente_texto.render(cadena_salida , True, color_texto_gris)
        screen.blit(texto_salida, ( 3 * (screen.get_width() // 4) - texto_salida.get_width() // 2, 70 ) ) # centrado a 3/4 de la horizontal, 70 de altura
    

    def mostrar_cronometro(self, screen:pygame.surface.Surface, limite_segundos: int):
       
        cadena_salida = f'cronometro    {self.tupla_cronometro[0]}:{self.tupla_cronometro[1]}   /   {limite_segundos//60}:{limite_segundos%60}'
        texto_salida = self.fuente_texto.render(cadena_salida , True, color_texto_gris)
        screen.blit(texto_salida, ( 3 * (screen.get_width() // 4) - texto_salida.get_width() // 2, 130 ) ) # centrado a 3/4 de la horizontal, 130 de altura


class Configuracion:
    def __init__(self, tiempo:Tiempos, mensajes_pantalla:MensajesPantalla, dificultad:int, espacio_jugable:Bloque, espacio_seguro:Bloque, dimension_bloque:int, x_jugador:int, y_jugador:int):
        self.dificultad = dificultad
        self.espacio_jugable = espacio_jugable # 
        self.espacio_seguro = espacio_seguro # 
        self.dimension_bloque = dimension_bloque
        self.x_jugador = x_jugador #
        self.y_jugador = y_jugador #
        self.tiempo = tiempo #
        self.mensajes_pantalla = mensajes_pantalla #


  #  def mostrar_mensaje(self, screen, )

    def mostrar_cronometro(self, screen:pygame.surface.Surface, limite_segundos:int):
        '''
        muestra el cronometro 
        '''                
        tupla = ( int(self.tiempo.cronometro_avance / 60), self.tiempo.cronometro_avance % 60 )


        self.mensajes_pantalla.tupla_cronometro = tupla
        self.mensajes_pantalla.mostrar_cronometro(screen, limite_segundos)
        


    def estado_pausa(self, pausa:bool, tecla_pulsada:int ) -> bool:
        '''
        verifica si hay que entrar o salir de pausa y gestiona el tiempo transcurrido de pormedio
        '''

        if tecla_pulsada == pygame.K_p:
            pausa = not(pausa)
            if pausa:
                self.tiempo.inicia_pausa()
            else:
                self.tiempo.termina_pausa()

        return pausa


    def crear_grilla(self) -> list[tuple]:
        '''
        Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una grilla 
        Retorno: una lista de tuplas que representan limites de una linea recta
        '''

        lista_lineas = []
        
        for x in range(self.espacio_jugable.left, self.espacio_jugable.right + 1, self.dimension_bloque):
            linea = ((x, self.espacio_jugable.top), (x, self.espacio_jugable.bottom))
            lista_lineas.append(linea)
        for y in range(self.espacio_jugable.top, self.espacio_jugable.bottom + 1, self.dimension_bloque):
            linea = ((self.espacio_jugable.left, y), (self.espacio_jugable.right, y))
            lista_lineas.append(linea)

        return lista_lineas

    def crear_puntos(self) -> list[tuple]:
        '''
        Recibe: el espacio jugable y la dimension de las grillas
        Operacion: recorre las dimensiones del espacio jugable saltando posiciones segun el tamaño de la grilla para guardar coordenadas que se usaran para armar una lista de puntos (círculos)
        Retorno: una lista de lista (matriz) de tuplas que representan las coordenadas de los puntos
        '''
        matriz_puntos = []
        

        for x in range(self.espacio_jugable.left, (self.espacio_jugable.right + 1), self.dimension_bloque):
            lista_puntos = []
            for y in range(self.espacio_jugable.top, (self.espacio_jugable.bottom + 1), self.dimension_bloque):
                punto = (x, y)
                lista_puntos.append(punto)
            matriz_puntos.append(lista_puntos)
            

        return matriz_puntos
    
    def mostrar_espacio_jugable(self, screen:pygame.surface.Surface):
        '''
        recibe el screen donde dibujar el espacio jugable y ejecuta el dibujo
        '''
        if self.dificultad == 1:
            color = color_facil

        elif self.dificultad == 2:
            color = color_normal

        elif self.dificultad == 3:
            color = color_dificil

        pygame.draw.rect(screen, color, self.espacio_jugable)
  
    def mostrar_espacio_seguro(self, screen:pygame.surface.Surface):
        '''
        recibe el screen donde dibujar el espacio jugable y ejecuta el dibujo
        '''
        pygame.draw.rect(screen, color_espacio_seguro, self.espacio_seguro)

    def subir_puntuacion(self, puntaje_subida:int):
        '''
        sube el puntaje el cual depende de la dificultad y la cantidad de filas eliminadas
        '''
        aumento = puntaje_subida * self.dificultad * 10
        self.mensajes_pantalla.entero_puntaje += aumento

def mensajes_pantalla_crear() -> MensajesPantalla:
    '''
    crea el contenido inicial para los mensajes en pantalla
    '''

    fuente_texto = pygame.font.Font(None, 36)
    texto_titulo = "JUGUEMOS AL TETRIS"
    entero_puntaje = 0
    tupla_tiempo = (0, 0)

    retorno = MensajesPantalla(fuente_texto, texto_titulo, entero_puntaje, tupla_tiempo)
    return retorno
        
def tiempo_crear(limite_movimientos_por_segundo:int, fps:int) -> Tiempos:
    '''
    crea el contenido inicial para los datos de tiempo
    '''

    tiempo_actual = time.time() #
    tiempo_anterior = time.time() #
    tiempo_entre_movimientos = 1 / limite_movimientos_por_segundo #
    tiempo_transcurrido = tiempo_actual - tiempo_anterior
    reloj = pygame.time.Clock() #
    cronometro = 0
    

    tiempo_retorno = Tiempos(reloj, tiempo_entre_movimientos, tiempo_actual, tiempo_transcurrido, tiempo_anterior, fps, cronometro, cronometro, cronometro)
    
    return tiempo_retorno

def config_crear(ancho_espacio_jugable:int, limite_movimientos_por_segundo:int, dificultad:int ) -> Configuracion:
    '''
    crea el archivo de configuracion el cual contendra variables de uso recurrente a lo largo del juego
    '''
    # espacio jugable
    alto_espacio_jugable = 2 * ancho_espacio_jugable
    espacio_jugable_x = 50
    espacio_jugable_y = 230
    espacio_jugable_cuadro = pygame.Rect(espacio_jugable_x, espacio_jugable_y, ancho_espacio_jugable, alto_espacio_jugable) #
    if dificultad == 1:
        espacio_jugable_color = color_facil

    elif dificultad == 2:
        espacio_jugable_color = color_normal

    elif dificultad == 3:
        espacio_jugable_color = color_dificil
    espacio_jugable = Bloque(espacio_jugable_color, espacio_jugable_cuadro)

     
    # dimension_bloque
    dimension_bloque = int (ancho_espacio_jugable / 10) #
  
    # posicion inicial del jugador
    x_jugador = int((espacio_jugable.left + espacio_jugable.right) / 2 - dimension_bloque) #
    y_jugador = espacio_jugable.top - 150 # (con espacio para que la figura se cree fuera del area de juego)

    # espacio_seguro para el jugador
    alto_espacio_seguro = espacio_jugable_y - y_jugador 
    espacio_seguro_cuadro = pygame.Rect(espacio_jugable_x, y_jugador, ancho_espacio_jugable, alto_espacio_seguro) #
    espacio_seguro = Bloque(color_espacio_seguro, espacio_seguro_cuadro)
    
    # tiempos
    fps = 60
    tiempos = tiempo_crear(limite_movimientos_por_segundo, fps)

    # mensaje en pantalla
    mensajes_pantalla = mensajes_pantalla_crear()

    # retorno
    retorno = Configuracion(tiempos, mensajes_pantalla, dificultad, espacio_jugable, espacio_seguro, dimension_bloque, x_jugador, y_jugador)
    return retorno

def crear_ventana(ancho:int, alto:int, texto_titulo:str) -> pygame.surface.Surface:
    '''
    Recibe: el alto, el ancho y el texto del titulo de la ventana
    Operacion: crea la ventana del programa con el tamaño y el titulo especificados
    Retorna: el objeto surface que representra a la ventana
    '''
    ventana = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(texto_titulo)
    return ventana

def mostrar_grilla (lista_lineas:list[tuple], screen:pygame.surface.Surface):

    if valida_lista(lista_lineas):
        for linea in lista_lineas:
            pygame.draw.line(screen, color_negro, linea[0], linea[1])
         
def mostrar_puntos(matriz_puntos:list[list[tuple]], screen:pygame.surface.Surface, radio: int):
    
    
    if valida_lista(matriz_puntos):
        for fila in matriz_puntos:
            if valida_lista(fila):
                for punto in fila:
                    pygame.draw.circle(screen, color_negro, punto, radio)
            else:
                break

def crear_figura(config: Configuracion) -> Figura:
    '''
    Crea una figura con formato de "tetramino" en la posicion inicial indicada
    '''
  

    opciones_color = [color_azul, color_amarillo, color_rojo, color_verde, color_naranja]
    color_RGB_bloque = random.choice(opciones_color)
    lista_bloques = crear_lista_bloques_iniciales(color_RGB_bloque, config.dimension_bloque, config.x_jugador, config.y_jugador)
    rotacion = 0 
    opciones_letra = ["I", "O", "T", "L"]
    letra = random.choice(opciones_letra)

    coord_bloque_0 = ( config.x_jugador , config.y_jugador )
    match letra:
        case "I": # rectangulo, 4 bloques apilados en una fila

            
            coord_bloque_0 = ( ( lista_bloques[0].cuadro.x ) , ( lista_bloques[0].cuadro.y ) )
            # se mantiene

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + config.dimension_bloque ) )
            lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_1[0] ) , ( coord_bloque_1[1] + config.dimension_bloque ) )
            lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] ) , ( coord_bloque_2[1] + config.dimension_bloque ) )
            lista_bloques[3].cambiar_coordenadas(coord_bloque_3)

            # lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo 1
            # lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y +  config.dimension_bloque #abajo 2 
            # lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y +  config.dimension_bloque #abajo 3

        case "O": # cuadrado, dos filas de dos bloques juntas

            coord_bloque_0 = ( ( lista_bloques[0].cuadro.x ) , ( lista_bloques[0].cuadro.y ) )
            # se mantiene

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + config.dimension_bloque ) )
            lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] + config.dimension_bloque ) , ( coord_bloque_0[1] ) )
            lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = (  (coord_bloque_0[0] + config.dimension_bloque ) , ( coord_bloque_0[1] + config.dimension_bloque ) )
            lista_bloques[3].cambiar_coordenadas(coord_bloque_3)


            # lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo
            # lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #derecha
            # lista_bloques[3].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #diagonal 1/2
            # lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #diagonal 2/2

        case "T": # literalmente la forma de una T

            coord_bloque_0 = ( ( lista_bloques[0].cuadro.x ) , ( lista_bloques[0].cuadro.y ) )
            #se mantiene

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + config.dimension_bloque ) )
            lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = (  (coord_bloque_0[0] + config.dimension_bloque ) , ( coord_bloque_0[1] ) )
            lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_0[0] - config.dimension_bloque ) , ( coord_bloque_0[1] ) )
            lista_bloques[3].cambiar_coordenadas(coord_bloque_3)


            # lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo
            # lista_bloques[2].cuadro.x = lista_bloques[0].cuadro.x +  config.dimension_bloque #derecha
            # lista_bloques[3].cuadro.x = lista_bloques[0].cuadro.x -  config.dimension_bloque #izquierda

        case "L": # literalmente la forma de una L

            

            coord_bloque_1 = ( ( coord_bloque_0[0] ), ( coord_bloque_0[1] + config.dimension_bloque ) )
            lista_bloques[1].cambiar_coordenadas(coord_bloque_1)

            coord_bloque_2 = ( ( coord_bloque_1[0] ) , ( coord_bloque_1[1] + config.dimension_bloque ))
            lista_bloques[2].cambiar_coordenadas(coord_bloque_2)

            coord_bloque_3 = ( ( coord_bloque_2[0] + config.dimension_bloque ) , ( coord_bloque_2[1]) )
            lista_bloques[3].cambiar_coordenadas(coord_bloque_3)

            # lista_bloques[1].cuadro.y = lista_bloques[0].cuadro.y +  config.dimension_bloque #abajo 1
            # lista_bloques[2].cuadro.y = lista_bloques[1].cuadro.y +  config.dimension_bloque #abajo 2 
            # lista_bloques[3].cuadro.y = lista_bloques[2].cuadro.y #diagonal 1/2
            # lista_bloques[3].cuadro.x = lista_bloques[2].cuadro.x +  config.dimension_bloque #diagonal 1/2


    
    figura_retorno = Figura(letra, rotacion, lista_bloques)

    # print(f'letra: {figura_retorno.letra}\trotacion: {figura_retorno.rotacion}')
    # print("info lista de bloques en la figura")
    # for bloque in lista_bloques:
    #     print(f'x={bloque.cuadro.x}\ty={bloque.cuadro.y}')

    return figura_retorno

def crear_pared(tipo_juego:str, config: Configuracion) -> Pared:
    '''
    Crea una nueva pared que contendra la informacion de los bloques caidos
    estructura_pared[i] = diccionario_columna = 
        {
            "pos_x", "tope_columna", "bloques_en_fila"[j] = diccionario_bloque_en_fila = 
            {
                "pos_y", "bool_bloque", "datos_bloque"
            }
        }
    '''

    tope_inicial = config.espacio_jugable.bottom - config.dimension_bloque
    tope_game_over = config.espacio_jugable.top


    # ya obtenida la informacion de los distintos datos de una vertical, se hace un proceso similar para obtener 
    # las posiciones horizontales y asignar los valores a diccionario_columna

   # print(f"bottom espacio={espacio_jugable.bottom}\ntop espacio={espacio_jugable.top}\nizquierda_Espacio={espacio_jugable.left}\nderacha espacio={espacio_jugable.right} ")
    

    #debugeo_columnas = 0 #debug columnas 1/2

    estructura_pared = [] # estructura matricial a retornar
    for x in range( config.espacio_jugable.left,  config.espacio_jugable.right, config.dimension_bloque): # x pertenece a [left; rigth-config.dimension_bloque] (numeros ascendentes)

       
        bloques_en_fila = [] # se crea bloques_en_fila:list[dict] 
        for y in range( tope_inicial, ( config.espacio_jugable.top - 1), -config.dimension_bloque): # y pertenece a [bottom-config.dimension_bloque; top] (numeros descendentes)
            diccionario_bloque_en_fila = {
                "pos_y": y, # guarda la coordenada y de la pantalla, indistinto a la coordenada y de la matriz
                "bool_bloque": False,
                "datos_bloque": None # inicialmente vacio hasta ser ocupado
            }
            bloques_en_fila.append(diccionario_bloque_en_fila)

            # debug coordenadas
           # print(f"se creo una coordenada en la pared con posicion: ({x};{y})")


        diccionario_columna = {
            "pos_x": x,
            "bloques_en_fila": bloques_en_fila
            }
        estructura_pared.append(diccionario_columna) # se agrega la info de la columna y sus segmentos de fila asociados a estructura_pared
        
        
        # debug columnas 1/2
      #  print(f'se creo la columna numero: {debugeo_columnas}')
    #    debugeo_columnas +=1

  
    retorno = Pared(tipo_juego, tope_inicial, tope_game_over, estructura_pared)
    return retorno

def controles_juego(config:Configuracion, tecla_pulsada:int, pared_juegos:Pared, figura_jugador:Figura) -> bool():
    '''
    verifica las interacciones de teclado relacionadas con el control de la figura. retorna bool que depende de si se ejecuta la funcion de bajada y se toca fondo
    '''
    
    retorno = False
    if config.tiempo.leer_evento():


        if tecla_pulsada == pygame.K_LEFT: # izq
            figura_mover("HOR", figura_jugador, pared_juegos, -config.dimension_bloque)

        elif tecla_pulsada == pygame.K_RIGHT: # der
            figura_mover("HOR", figura_jugador, pared_juegos, config.dimension_bloque)

        elif tecla_pulsada == pygame.K_DOWN: # aba
            retorno = figura_mover("VER", figura_jugador, pared_juegos, config.dimension_bloque)
        
        elif tecla_pulsada == pygame.K_UP: # arr
            if figura_rotar(figura_jugador, pared_juegos):
                config.tiempo.actualiza_tiempo_anterior() # TIEMPO



        # # mantiene pulsacion
        # keys = pygame.key.get_pressed()

        # if keys[pygame.K_LEFT] : # izquierda
        #     config.tiempo.actualiza_tiempo_anterior() # TIEMPO
        #     figura_mover("HOR", figura_jugador, pared_juegos, -config.dimension_bloque)
            

        # if keys[pygame.K_RIGHT] : # derecha 
        #     config.tiempo.actualiza_tiempo_anterior() # TIEMPO
        #     figura_mover("HOR", figura_jugador, pared_juegos, config.dimension_bloque)

            
        # if keys[pygame.K_DOWN]: # abajo
        #     config.tiempo.actualiza_tiempo_anterior() # TIEMPO
        #     retorno = figura_mover("VER", figura_jugador, pared_juegos, config.dimension_bloque)

            
        # if keys[pygame.K_UP]: # arriba
        #     print("tecla arriba inicio")
        #     if figura_rotar(figura_jugador, pared_juegos): # sin rotacion efectiva no hay actualizacion en tiempos
        #         config.tiempo.actualiza_tiempo_anterior() # TIEMPO
        #         print("tecla arriba fin")
                
            
            

    return retorno

def figura_rotar(figura_jugador:Figura, pared_juegos:Pared) -> bool:
    '''
    controla la rotacion en la figura_jugador.
    retorna True en caso de que el proceso sea exitoso y False en caso de fallar
    '''

    lista_bloques_original = copy.deepcopy(figura_jugador.lista_bloques) # respaldo de la figura
    rotacion_original = figura_jugador.rotacion
    letra = figura_jugador.letra

    
    if letra == "L":
        figura_jugador.rotar_L()


    if letra == "T":
        figura_jugador.rotar_T()


    if letra == "I":
        figura_jugador.rotar_I()

    # cuadrados no rotan



    retorno = True

    # si se detectan choques en la figura entonces se regresa a la version respaldada
    if ( figura_verificar_devolucion("HOR", figura_jugador, pared_juegos) != 0 ) or  ( figura_verificar_devolucion("VER", figura_jugador, pared_juegos) != 0 ):
        figura_jugador.lista_bloques = lista_bloques_original
        figura_jugador.rotacion = rotacion_original
        retorno = False

    return retorno

def leer_evento() -> tuple[bool, int]:
    '''
    lee posible evento de cierre del bucle y de tecla presionada.
    retorna valores por defecto en caso de no detectarse eventos.
    retorno = (running, tecla_pulsada)
    '''
    retorno_0 = True
    retorno_1 = None
    retorno_2 = None

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # salida de pygame
            retorno_0 = False
        elif event.type == pygame.KEYDOWN: # tecla presionada
            retorno_1 = copy.deepcopy(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN: # click presionado
            retorno_2 = copy.deepcopy(event.pos)

    return (retorno_0, retorno_1, retorno_2)


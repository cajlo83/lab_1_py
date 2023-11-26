import sqlite3
import os

def db_crear(directorio:str):
    '''
    Crea la base de datos en caso que no exista
    '''    
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE puntajes
                         (puntaje INTEGER, dificultad INTEGER, nombre TEXT)''') # tablas con orden puntaje - dificultad - nombre
        print("Se creó la DB")
    except sqlite3.Error as e:
        print(f"Error al crear la DB: {e}")
        

def db_insertar_puntaje(directorio:str, puntaje:int, dificultad:int, nombre:str):
    '''
    Agrega una nueva información a la DB
    '''
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO puntajes VALUES (?, ?, ?)", (puntaje, dificultad, nombre))
        print("Se insertaron los datos correctamente")
    except sqlite3.Error as e:
        print(f"Error al insertar puntaje: {e}")


def db_obtener_puntajes_ordenados(directorio:str) -> tuple[int, int, str]:
    '''
    Abre la DB y retorna una lista de duplas (puntaje, dificultad, nombre) ordenadas descendentemente
    '''
    retorno = []
    try:
        with sqlite3.connect(directorio) as conn:
            c = conn.cursor()
            c.execute("SELECT puntaje, dificultad, nombre FROM puntajes ORDER BY puntaje DESC, dificultad DESC") # ordena los puntajes en forma descendente y secundariamente por dificultad descendente
            puntajes = c.fetchall()
            retorno = puntajes
    except sqlite3.Error as e:
        print(f"Error al obtener puntajes: {e}")
    
    return retorno

def armar_directorio_tetris_pygame(nombre_archivo:str) -> str:
    directorio_trabajo = os.getcwd()
    directorio_archivo = os.path.join(directorio_trabajo, 'lab_1_py', 'tetris_pygame', nombre_archivo)
    print(f'se uso el directorio: {directorio_archivo}')
    return directorio_archivo


def mostrar_top_5(directorio):
    '''
    recibe el directorio de la DB y muestra el top 5
    '''
    
    lista_puntajes = db_obtener_puntajes_ordenados(directorio)
    print("\nscore\t\tdificultad\tnombre")
    for i in range(len(lista_puntajes)):
        if i >= 5:
            break
        print(f'{lista_puntajes[i][0]}\t\t{lista_puntajes[i][1]}\t\t{lista_puntajes[i][2]}')
        
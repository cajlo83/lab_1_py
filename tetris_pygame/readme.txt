la funcion armar_directorio_tetris_pygame() ubicada en tetris_archivos.py esta personalida para mi workspace por defecto.
puedes cambiarlo por esta version para que funcion en otros workspaces


def armar_directorio_tetris_pygame(nombre_archivo:str, directorio_actual:str = None) -> str:
    '''
    crea el directorio para el workspace correspondiente.
    '''

    # workspace generico
    if directorio_actual is None:
        directorio_trabajo = os.getcwd()
        print(f'armar_directorio_tetris_pygame: {directorio_trabajo}')
        directorio_archivo = os.path.join(directorio_trabajo, nombre_archivo)
    else:
        directorio_archivo = os.path.join(directorio_actual, nombre_archivo)


        directorio_archivo = os.path.join(directorio_actual, nombre_archivo)

    return directorio_archivo
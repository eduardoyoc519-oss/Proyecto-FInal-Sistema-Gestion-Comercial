# MODULO DE ARCHIVOS Y PERSISTENCIA (archivos.py)


import os
import json

data_dir = "data"



def asegurar_directorio():
    """verifica si la carpeta data existe si no, la crea."""
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)


def cargar_datos(nombre_archivo):
    """carga los datos desde un archivo JSON."""
    asegurar_directorio()
    ruta = os.path.join(data_dir, nombre_archivo)
    
    if not os.path.exists(ruta):
        return []
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except Exception as e:
        print(f"Error al leer el archivo {nombre_archivo}: {e}")
        return []



def guardar_datos(nombre_archivo, datos):
    """guarda los datos en un archivo JSON con formato legible."""
    asegurar_directorio()
    ruta = os.path.join(data_dir, nombre_archivo)
    
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar el archivo {nombre_archivo}: {e}")
        return False




    
import json

NOMBRE_ARCHIVO = "alumnos.json"


def cargar_alumnos():
    """Lee los alumnos desde el archivo JSON. Si no existe, devuelve un diccionario vacío."""
    try:
        with open(NOMBRE_ARCHIVO, "r") as archivo_json:
            return json.load(archivo_json)
    except FileNotFoundError:
        return {}


def guardar_alumnos(alumnos):
    """Guarda el diccionario de alumnos en el archivo JSON."""
    with open(NOMBRE_ARCHIVO, "w") as archivo_json:
        json.dump(alumnos, archivo_json, indent=4)


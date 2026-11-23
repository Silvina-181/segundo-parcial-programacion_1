from validaciones import pedir_dni_nuevo, pedir_texto, pedir_edad, pedir_nota
from archivos import guardar_alumnos


def registrar_alumno(alumnos):
    """Pide los datos validados, agrega un nuevo alumno y guarda en el archivo."""
    print("\n--- REGISTRAR NUEVO ALUMNO ---")
    dni = pedir_dni_nuevo(alumnos)
    nombre = pedir_texto("Ingrese el nombre: ")
    apellido = pedir_texto("Ingrese el apellido: ")
    edad = pedir_edad()
    nota = pedir_nota()

    alumnos[dni] = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nota": nota
    }

    guardar_alumnos(alumnos)
    print(f"Alumno {nombre} {apellido} registrado y guardado correctamente.")


def listar_alumnos(alumnos):
    """Muestra todos los alumnos registrados de forma ordenada."""
    print("\n--- LISTADO DE ALUMNOS ---")
    if len(alumnos) == 0:
        print("No hay alumnos registrados en el sistema.")
        return

    for dni, datos in alumnos.items():
        print(f"DNI: {dni} | {datos['apellido']}, {datos['nombre']} | Edad: {datos['edad']} | Nota: {datos['nota']}")


def buscar_alumno(alumnos):
    """Busca un alumno por su DNI utilizando la clave directa del diccionario."""
    print("\n--- BUSCAR ALUMNO POR DNI ---")
    dni = input("Ingrese el DNI a buscar: ").strip()

    if dni in alumnos:
        datos = alumnos[dni]
        print(f"Alumno encontrado -> DNI: {dni} | Nombre: {datos['nombre']} {datos['apellido']} | Edad: {datos['edad']} | Nota: {datos['nota']}")
    else:
        print("Error: No se encontró ningún alumno con ese DNI.")


def modificar_alumno(alumnos):
    """Permite modificar edad o nota de un alumno existente y guarda los cambios."""
    print("\n--- MODIFICAR DATOS DE UN ALUMNO ---")
    dni = input("Ingrese el DNI del alumno a modificar: ").strip()

    if dni not in alumnos:
        print("Error: No existe ningún alumno con ese DNI.")
        return

    datos = alumnos[dni]
    print(f"Alumno actual: {datos['nombre']} {datos['apellido']} (Edad: {datos['edad']}, Nota: {datos['nota']})")
    print("¿Qué desea modificar?")
    print("1. Edad")
    print("2. Nota")
    opcion = input("Elija una opción (1 o 2): ").strip()

    if opcion == "1":
        alumnos[dni]["edad"] = pedir_edad()
        guardar_alumnos(alumnos)
        print("Edad actualizada y guardada correctamente.")
    elif opcion == "2":
        alumnos[dni]["nota"] = pedir_nota()
        guardar_alumnos(alumnos)
        print("Nota actualizada y guardada correctamente.")
    else:
        print("Opción no válida. No se realizaron cambios.")


def eliminar_alumno(alumnos):
    """Elimina un alumno del diccionario por su DNI y actualiza el archivo JSON."""
    print("\n--- ELIMINAR ALUMNO ---")
    dni = input("Ingrese el DNI del alumno a eliminar: ").strip()

    if dni in alumnos:
        eliminado = alumnos.pop(dni)
        guardar_alumnos(alumnos)
        print(f"Alumno {eliminado['nombre']} {eliminado['apellido']} eliminado correctamente.")
    else:
        print("Error: No se encontró ningún alumno con ese DNI.")


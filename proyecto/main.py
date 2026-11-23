from archivos import cargar_alumnos
from alumnos import (
    registrar_alumno,
    listar_alumnos,
    buscar_alumno,
    modificar_alumno,
    eliminar_alumno
)
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    """Muestra las opciones disponibles del sistema."""
    print("\n=========================================")
    print("     SISTEMA DE GESTIÓN DE ALUMNOS       ")
    print("=========================================")
    print("1. Registrar nuevo alumno")
    print("2. Listar todos los alumnos")
    print("3. Buscar alumno por DNI")
    print("4. Modificar datos de un alumno")
    print("5. Eliminar alumno")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("=========================================")


def main():
    # Cargamos los datos persistidos al iniciar el programa
    alumnos = cargar_alumnos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            registrar_alumno(alumnos)
        elif opcion == "2":
            listar_alumnos(alumnos)
        elif opcion == "3":
            buscar_alumno(alumnos)
        elif opcion == "4":
            modificar_alumno(alumnos)
        elif opcion == "5":
            eliminar_alumno(alumnos)
        elif opcion == "6":
            mostrar_estadisticas(alumnos)
        elif opcion == "7":
            print("Cerrando el sistema. ¡Hasta luego!")
            break
        else:
            print("Error: Opción inválida. Por favor, elija un número del 1 al 7.")


main()



def mostrar_estadisticas(alumnos):
    """Calcula y muestra el resumen estadístico de los alumnos sin modificar los datos."""
    print("\n--- ESTADÍSTICAS DEL CURSO ---")

    # 1. Validamos si hay alumnos cargados para evitar división por cero
    if len(alumnos) == 0:
        print("No hay alumnos registrados para calcular estadísticas.")
        return

    total_alumnos = len(alumnos)
    suma_notas = 0
    aprobados = 0
    desaprobados = 0

    # Variables para guardar al alumno con la nota más alta
    mejor_nota = -1
    mejor_alumno = ""

    # 2. Recorremos el diccionario usando .items() (visto en clase)
    for dni, datos in alumnos.items():
        nota = datos["nota"]
        suma_notas += nota

        # Contamos aprobados (nota >= 6) y desaprobados (nota < 6)
        if nota >= 6:
            aprobados += 1
        else:
            desaprobados += 1

        # Buscamos la nota más alta
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = f"{datos['nombre']} {datos['apellido']} (DNI: {dni})"

    promedio = suma_notas / total_alumnos

    # 3. Mostramos los resultados
    print(f"Cantidad total de alumnos: {total_alumnos}")
    print(f"Promedio general de notas: {promedio:.2f}")
    print(f"Alumno con mejor nota: {mejor_alumno} -> Nota: {mejor_nota}")
    print(f"Cantidad de aprobados (nota >= 6): {aprobados}")
    print(f"Cantidad de desaprobados (nota < 6): {desaprobados}")


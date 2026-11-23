def pedir_dni_nuevo(alumnos):
    """Pide un DNI válido (solo números, mínimo 7 dígitos) y verifica que no exista."""
    while True:
        dni = input("Ingrese el DNI del alumno (sin puntos): ").strip()
        if not dni.isdigit():
            print("Error: El DNI debe contener solo números.")
        elif len(dni) < 7:
            print("Error: El DNI debe tener al menos 7 dígitos.")
        elif dni in alumnos:
            print("Error: Ya existe un alumno registrado con ese DNI.")
        else:
            return dni


def pedir_texto(mensaje):
    """Pide un texto (nombre o apellido) verificando que no quede vacío."""
    while True:
        texto = input(mensaje).strip()
        if len(texto) == 0:
            print("Error: Este campo no puede quedar vacío.")
        else:
            return texto


def pedir_edad():
    """Pide una edad entera mayor o igual a 0."""
    while True:
        entrada = input("Ingrese la edad del alumno: ").strip()
        try:
            edad = int(entrada)
            if edad >= 0:
                return edad
            else:
                print("Error: La edad no puede ser negativa.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def pedir_nota():
    """Pide una nota numérica entre 0 y 10 inclusive."""
    while True:
        entrada = input("Ingrese la nota del alumno (0 a 10): ").strip()
        try:
            nota = float(entrada)
            if nota >= 0 and nota <= 10:
                return nota
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido para la nota.")


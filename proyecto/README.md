# Segundo Parcial (Programación I) - Prof: Zotti, E.M. - Di Leone A. 

# Sistema de Gestión de Alumnos 

Programa para administrar el registro de alumnos y almacenar la información en archivos.

## Estructura de archivos

* `main.py`: Archivo principal con el menú de opciones para interactuar con el usuario. 
* `alumnos.py`: Funciones para registrar, listar, buscar, modificar y eliminar alumnos.
* `archivos.py`: Funciones para leer y guardar los datos en `alumnos.json`.
* `validaciones.py`: Controles para evitar datos inválidos.
* `estadisticas.py`: Calcula total de alumnos, promedio, mejor nota, aprobados y desaprobados.
* `alumnos.json`: Archivo donde quedan guardados los alumnos entre ejecuciones.


## Cómo ejecutarlo

1. Abrir una terminal en la carpeta `proyecto`.
2. Ejecutar: `python main.py`

## Decisiones de diseño

* **Diccionario anidado:** Usé el DNI como clave principal porque es único y permite buscar, modificar o borrar un alumno directo por su clave sin recorrer toda la colección. Además, se guarda directo en formato JSON.
* **Separación en módulos:** Programa dividido en 5 archivos según la tarea de cada uno para que el código sea ordenado y fácil de mantener.
* **Guardado automático:** Cada vez que se agrega, modifica o elimina un alumno, se actualiza `alumnos.json` automáticamente.

## Video explicativo

* [Ver demostración y explicación completa en Google Drive](https://drive.google.com/file/d/1e3oNBa8RTKLs8iqjfFcbAq2N72xl-J5W/view?usp=drive_link)

from pathlib import Path  # Importa Path para manejar rutas de forma sencilla.


def mostrar_documentacion():  # Define una función que resume la documentación del proyecto.
    print("Proyecto Software FJ")  # Muestra el nombre del proyecto.
    print("Sistema orientado a objetos para clientes, servicios y reservas.")  # Explica el objetivo general.
    print("No utiliza base de datos.")  # Aclara la restricción principal del ejercicio.
    print("Usa objetos, listas internas y archivo de logs.")  # Describe cómo se maneja la información.
    print("Incluye abstracción, herencia, polimorfismo y encapsulación.")  # Resume los principios de POO aplicados.
    print("Incluye manejo avanzado de excepciones.")  # Resume el manejo de errores solicitado.


def crear_estructura_logs():  # Define una función para preparar la carpeta de logs.
    ruta_logs = Path("logs")  # Crea una ruta relativa para la carpeta de logs.
    ruta_logs.mkdir(exist_ok=True)  # Crea la carpeta si todavía no existe.
    return ruta_logs  # Retorna la ruta creada o encontrada.


if __name__ == "__main__":  # Verifica que el archivo se esté ejecutando directamente.
    crear_estructura_logs()  # Prepara la carpeta de logs del proyecto.
    mostrar_documentacion()  # Muestra la documentación básica en consola.

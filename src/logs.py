from datetime import datetime  # Importa datetime para registrar la fecha y hora de cada evento.


class LoggerSoftwareFJ:  # Define una clase sencilla para manejar logs del sistema.
    def __init__(self, ruta_archivo="software_fj.log"):  # Inicializa el logger con una ruta de archivo.
        self.ruta_archivo = ruta_archivo  # Guarda la ruta del archivo de logs.

    def registrar(self, nivel, operacion, mensaje):  # Registra un evento o error en el archivo.
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatea la fecha actual.
        linea = f"{fecha} | {nivel} | {operacion} | {mensaje}\n"  # Construye la línea que se guardará.
        try:  # Protege la escritura del archivo de logs.
            with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:  # Abre el archivo en modo agregar.
                archivo.write(linea)  # Escribe la línea en el archivo.
        except OSError as error:  # Captura errores del sistema de archivos.
            print(f"No se pudo escribir en el log: {error}")  # Informa el problema sin detener todo el sistema.

    def info(self, operacion, mensaje):  # Registra un evento informativo.
        self.registrar("INFO", operacion, mensaje)  # Usa el nivel INFO para operaciones correctas.

    def error(self, operacion, mensaje):  # Registra un evento de error.
        self.registrar("ERROR", operacion, mensaje)  # Usa el nivel ERROR para fallos controlados.

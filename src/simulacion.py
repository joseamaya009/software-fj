def ejecutar(nombre, funcion):  # Define una función auxiliar para ejecutar operaciones controladas.
    try:  # Inicia el bloque que puede fallar.
        funcion()  # Ejecuta la operación recibida.
        print(f"OK: {nombre}")  # Muestra que la operación fue exitosa.
    except Exception as error:  # Captura cualquier error de la operación.
        print(f"ERROR: {nombre} -> {error}")  # Muestra el error sin detener la simulación.


def cliente_valido():  # Simula el registro de un cliente válido.
    return {"documento": "123", "correo": "ana@correo.com"}  # Retorna datos correctos de ejemplo.


def cliente_invalido():  # Simula el registro de un cliente inválido.
    raise ValueError("Correo inválido.")  # Lanza un error controlado de datos inválidos.


def servicio_sala_valido():  # Simula la creación de una sala válida.
    return {"servicio": "Sala ejecutiva", "capacidad": 10}  # Retorna datos correctos del servicio.


def servicio_sala_invalido():  # Simula la creación de una sala inválida.
    raise ValueError("La capacidad debe ser mayor que cero.")  # Lanza error por capacidad inválida.


def reserva_exitosa():  # Simula una reserva correcta.
    return {"estado": "procesada", "costo": 100000}  # Retorna resultado esperado de una reserva procesada.


operaciones = [  # Define la lista de operaciones mínimas para demostrar el sistema.
    ("Registrar cliente válido", cliente_valido),  # Agrega una operación válida de cliente.
    ("Registrar cliente inválido", cliente_invalido),  # Agrega una operación inválida de cliente.
    ("Crear sala válida", servicio_sala_valido),  # Agrega una operación válida de servicio.
    ("Crear sala inválida", servicio_sala_invalido),  # Agrega una operación inválida de servicio.
    ("Crear alquiler válido", lambda: {"equipo": "Portátil"}),  # Agrega una operación válida de alquiler.
    ("Crear alquiler inválido", lambda: (_ for _ in ()).throw(ValueError("Cantidad inválida."))),  # Agrega una operación inválida de alquiler.
    ("Crear asesoría válida", lambda: {"asesoria": "Python"}),  # Agrega una operación válida de asesoría.
    ("Crear asesoría inválida", lambda: (_ for _ in ()).throw(ValueError("Horas inválidas."))),  # Agrega una operación inválida de asesoría.
    ("Procesar reserva exitosa", reserva_exitosa),  # Agrega una reserva exitosa.
    ("Procesar reserva fallida", lambda: (_ for _ in ()).throw(ValueError("Duración inválida."))),  # Agrega una reserva fallida.
]  # Cierra la lista de operaciones.


for nombre, funcion in operaciones:  # Recorre cada operación definida.
    ejecutar(nombre, funcion)  # Ejecuta la operación con manejo de errores.

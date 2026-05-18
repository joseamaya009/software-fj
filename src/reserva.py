class Reserva:  # Define la clase que representa una reserva del sistema.
    def __init__(self, codigo, cliente, servicio, duracion):  # Inicializa una reserva con cliente, servicio y duración.
        self.codigo = codigo  # Guarda el código de la reserva.
        self.cliente = cliente  # Guarda el cliente asociado.
        self.servicio = servicio  # Guarda el servicio asociado.
        self.duracion = duracion  # Guarda la duración de la reserva.
        self.estado = "creada"  # Define el estado inicial de la reserva.
        self.costo = 0  # Inicializa el costo de la reserva en cero.
        self.validar()  # Valida la reserva al momento de crearla.

    def validar(self):  # Valida los datos mínimos de la reserva.
        if self.cliente is None:  # Comprueba que exista un cliente.
            raise ValueError("La reserva debe tener un cliente válido.")  # Lanza error si falta el cliente.
        if self.servicio is None:  # Comprueba que exista un servicio.
            raise ValueError("La reserva debe tener un servicio válido.")  # Lanza error si falta el servicio.
        if self.duracion <= 0:  # Comprueba que la duración sea positiva.
            raise ValueError("La duración de la reserva debe ser mayor que cero.")  # Lanza error si la duración es inválida.

    def confirmar(self):  # Confirma una reserva creada.
        if self.estado == "cancelada":  # Verifica si la reserva ya fue cancelada.
            raise ValueError("No se puede confirmar una reserva cancelada.")  # Lanza error por operación no permitida.
        self.estado = "confirmada"  # Cambia el estado a confirmada.

    def cancelar(self):  # Cancela una reserva si todavía se puede cancelar.
        if self.estado == "procesada":  # Verifica si la reserva ya fue procesada.
            raise ValueError("No se puede cancelar una reserva procesada.")  # Lanza error por operación no permitida.
        self.estado = "cancelada"  # Cambia el estado a cancelada.

    def procesar(self):  # Procesa una reserva y calcula su costo.
        if self.estado != "confirmada":  # Verifica que la reserva esté confirmada.
            raise ValueError("Solo se pueden procesar reservas confirmadas.")  # Lanza error si el estado no permite procesar.
        self.costo = self.servicio.calcular_costo(self.duracion)  # Calcula el costo usando el servicio asociado.
        self.estado = "procesada"  # Cambia el estado a procesada.
        return self.costo  # Retorna el costo calculado.

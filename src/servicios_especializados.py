class ReservaSala:  # Define el servicio especializado para reservar salas.
    def __init__(self, nombre, tarifa_hora, capacidad):  # Inicializa la sala con nombre, tarifa y capacidad.
        self.nombre = nombre  # Guarda el nombre de la sala.
        self.tarifa_hora = tarifa_hora  # Guarda el costo por hora.
        self.capacidad = capacidad  # Guarda la capacidad máxima de personas.
        self.validar_parametros()  # Valida los datos específicos de la sala.

    def validar_parametros(self):  # Valida las reglas propias de la sala.
        if self.capacidad <= 0:  # Comprueba que la capacidad sea positiva.
            raise ValueError("La capacidad de la sala debe ser mayor que cero.")  # Lanza error si la capacidad es inválida.
        if self.tarifa_hora <= 0:  # Comprueba que la tarifa sea positiva.
            raise ValueError("La tarifa por hora debe ser mayor que cero.")  # Lanza error si la tarifa es inválida.

    def calcular_costo(self, horas):  # Calcula el valor de reservar la sala.
        return self.tarifa_hora * horas  # Multiplica tarifa por duración.


class AlquilerEquipo:  # Define el servicio especializado para alquilar equipos.
    def __init__(self, tipo_equipo, tarifa_dia, cantidad):  # Inicializa el alquiler con tipo, tarifa y cantidad.
        self.tipo_equipo = tipo_equipo  # Guarda el tipo de equipo.
        self.tarifa_dia = tarifa_dia  # Guarda el costo diario del equipo.
        self.cantidad = cantidad  # Guarda la cantidad de equipos solicitados.
        self.validar_parametros()  # Valida los datos específicos del alquiler.

    def validar_parametros(self):  # Valida las reglas propias del alquiler.
        if self.cantidad <= 0:  # Comprueba que la cantidad sea positiva.
            raise ValueError("La cantidad de equipos debe ser mayor que cero.")  # Lanza error si la cantidad es inválida.
        if self.tarifa_dia <= 0:  # Comprueba que la tarifa diaria sea positiva.
            raise ValueError("La tarifa diaria debe ser mayor que cero.")  # Lanza error si la tarifa es inválida.

    def calcular_costo(self, dias):  # Calcula el valor del alquiler.
        return self.tarifa_dia * self.cantidad * dias  # Multiplica tarifa, cantidad y días.


class AsesoriaEspecializada:  # Define el servicio especializado para asesorías.
    def __init__(self, especialidad, tarifa_hora, nivel):  # Inicializa la asesoría con especialidad, tarifa y nivel.
        self.especialidad = especialidad  # Guarda el área de asesoría.
        self.tarifa_hora = tarifa_hora  # Guarda el costo por hora.
        self.nivel = nivel  # Guarda el nivel del consultor.
        self.validar_parametros()  # Valida los datos específicos de la asesoría.

    def validar_parametros(self):  # Valida las reglas propias de la asesoría.
        if not str(self.especialidad).strip():  # Comprueba que exista especialidad.
            raise ValueError("La especialidad de la asesoría es obligatoria.")  # Lanza error si falta la especialidad.
        if self.tarifa_hora <= 0:  # Comprueba que la tarifa sea positiva.
            raise ValueError("La tarifa por hora debe ser mayor que cero.")  # Lanza error si la tarifa es inválida.

    def calcular_costo(self, horas):  # Calcula el valor de la asesoría.
        multiplicador = 1.3 if self.nivel == "experto" else 1  # Aumenta el costo si el consultor es experto.
        return self.tarifa_hora * horas * multiplicador  # Retorna el costo ajustado por nivel.

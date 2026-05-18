from abc import ABC, abstractmethod  # Importa herramientas para definir una clase abstracta.


class Servicio(ABC):  # Define la clase abstracta para todos los servicios.
    def __init__(self, codigo, nombre, tarifa_base, disponible=True):  # Inicializa los datos comunes del servicio.
        self._codigo = codigo  # Guarda el código del servicio como atributo protegido.
        self._nombre = nombre  # Guarda el nombre del servicio como atributo protegido.
        self._tarifa_base = tarifa_base  # Guarda la tarifa base como atributo protegido.
        self._disponible = disponible  # Guarda la disponibilidad actual del servicio.
        self.validar_base()  # Valida los datos comunes del servicio.

    @property  # Permite consultar el código del servicio.
    def codigo(self):  # Define el getter del código.
        return self._codigo  # Retorna el código almacenado.

    @property  # Permite consultar la disponibilidad del servicio.
    def disponible(self):  # Define el getter de disponibilidad.
        return self._disponible  # Retorna verdadero o falso según disponibilidad.

    def validar_base(self):  # Valida los atributos comunes de cualquier servicio.
        if not str(self._codigo).strip():  # Verifica que el código no esté vacío.
            raise ValueError("El código del servicio es obligatorio.")  # Lanza error si falta el código.
        if not str(self._nombre).strip():  # Verifica que el nombre no esté vacío.
            raise ValueError("El nombre del servicio es obligatorio.")  # Lanza error si falta el nombre.
        if self._tarifa_base <= 0:  # Verifica que la tarifa sea positiva.
            raise ValueError("La tarifa base debe ser mayor que cero.")  # Lanza error si la tarifa es inválida.

    @abstractmethod  # Obliga a cada servicio hijo a calcular su costo.
    def calcular_costo(self, duracion, impuesto=0, descuento=0):  # Declara el método de cálculo con parámetros opcionales.
        pass  # Deja el cálculo específico para la clase hija.

    @abstractmethod  # Obliga a cada servicio hijo a describirse.
    def describir_servicio(self):  # Declara el método de descripción del servicio.
        pass  # Deja la descripción específica para la clase hija.

    @abstractmethod  # Obliga a cada servicio hijo a validar sus propios parámetros.
    def validar_parametros(self):  # Declara el método de validación especializada.
        pass  # Deja la validación específica para la clase hija.

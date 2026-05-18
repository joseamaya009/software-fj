from abc import ABC, abstractmethod  # Importa herramientas para crear clases abstractas.
from datetime import datetime  # Importa datetime para guardar la fecha de creación.


class EntidadBase(ABC):  # Define una clase abstracta que servirá como base del sistema.
    def __init__(self, identificador, nombre):  # Inicializa los datos comunes de cualquier entidad.
        self._identificador = identificador  # Guarda el identificador como atributo protegido.
        self._nombre = nombre  # Guarda el nombre como atributo protegido.
        self._activo = True  # Marca la entidad como activa por defecto.
        self._fecha_creacion = datetime.now()  # Registra la fecha en que se creó la entidad.
        self.validar_datos_base()  # Ejecuta la validación común al crear la entidad.

    @property  # Permite consultar el identificador de forma controlada.
    def identificador(self):  # Define el getter del identificador.
        return self._identificador  # Retorna el identificador almacenado.

    @property  # Permite consultar el nombre de forma controlada.
    def nombre(self):  # Define el getter del nombre.
        return self._nombre  # Retorna el nombre almacenado.

    @property  # Permite consultar si la entidad está activa.
    def activo(self):  # Define el getter del estado activo.
        return self._activo  # Retorna el estado actual de la entidad.

    def validar_datos_base(self):  # Valida los datos comunes de todas las entidades.
        if not str(self._identificador).strip():  # Verifica que el identificador no esté vacío.
            raise ValueError("El identificador no puede estar vacío.")  # Lanza error si el identificador es inválido.
        if not str(self._nombre).strip():  # Verifica que el nombre no esté vacío.
            raise ValueError("El nombre no puede estar vacío.")  # Lanza error si el nombre es inválido.

    def desactivar(self):  # Cambia el estado de la entidad a inactiva.
        self._activo = False  # Asigna falso al estado activo.

    @abstractmethod  # Obliga a las clases hijas a implementar este método.
    def validar(self):  # Declara el método de validación específico.
        pass  # Deja la implementación pendiente para la clase hija.

    @abstractmethod  # Obliga a las clases hijas a implementar este método.
    def describir(self):  # Declara el método de descripción específica.
        pass  # Deja la implementación pendiente para la clase hija.

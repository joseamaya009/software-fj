import re  # Importa expresiones regulares para validar correo y teléfono.


class Cliente:  # Define la clase encargada de representar clientes.
    def __init__(self, documento, nombres, apellidos, correo, telefono):  # Inicializa un cliente con sus datos personales.
        self.__documento = documento  # Guarda el documento como atributo privado.
        self.__nombres = nombres  # Guarda los nombres como atributo privado.
        self.__apellidos = apellidos  # Guarda los apellidos como atributo privado.
        self.__correo = correo  # Guarda el correo como atributo privado.
        self.__telefono = telefono  # Guarda el teléfono como atributo privado.
        self.validar()  # Valida todos los datos del cliente al crearlo.

    @property  # Permite consultar el documento sin modificarlo directamente.
    def documento(self):  # Define el getter del documento.
        return self.__documento  # Retorna el documento del cliente.

    @property  # Permite consultar el nombre completo.
    def nombre_completo(self):  # Define el getter del nombre completo.
        return f"{self.__nombres} {self.__apellidos}"  # Une nombres y apellidos en una sola cadena.

    @property  # Permite consultar el correo.
    def correo(self):  # Define el getter del correo.
        return self.__correo  # Retorna el correo del cliente.

    def validar(self):  # Valida que los datos personales sean correctos.
        if not str(self.__documento).strip():  # Comprueba que el documento no esté vacío.
            raise ValueError("El documento del cliente es obligatorio.")  # Lanza error cuando falta el documento.
        if not str(self.__nombres).strip():  # Comprueba que los nombres no estén vacíos.
            raise ValueError("Los nombres del cliente son obligatorios.")  # Lanza error cuando faltan los nombres.
        if not str(self.__apellidos).strip():  # Comprueba que los apellidos no estén vacíos.
            raise ValueError("Los apellidos del cliente son obligatorios.")  # Lanza error cuando faltan los apellidos.
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self.__correo):  # Verifica que el correo tenga formato válido.
            raise ValueError("El correo del cliente no tiene un formato válido.")  # Lanza error cuando el correo es inválido.
        if not re.match(r"^\+?\d{7,15}$", str(self.__telefono)):  # Verifica que el teléfono tenga dígitos suficientes.
            raise ValueError("El teléfono del cliente no tiene un formato válido.")  # Lanza error cuando el teléfono es inválido.

    def describir(self):  # Genera una descripción corta del cliente.
        return f"Cliente {self.nombre_completo} con documento {self.__documento}"  # Retorna una descripción legible.

class SistemaSoftwareFJException(Exception):  # Define la excepción base del sistema.
    pass  # Permite heredar un tipo común para errores del proyecto.


class ClienteInvalidoException(SistemaSoftwareFJException):  # Define errores relacionados con clientes inválidos.
    pass  # Mantiene una excepción específica para clientes.


class ServicioInvalidoException(SistemaSoftwareFJException):  # Define errores relacionados con servicios inválidos.
    pass  # Mantiene una excepción específica para servicios.


class ReservaInvalidaException(SistemaSoftwareFJException):  # Define errores relacionados con reservas inválidas.
    pass  # Mantiene una excepción específica para reservas.


class CalculoCostoException(SistemaSoftwareFJException):  # Define errores relacionados con cálculos de costos.
    pass  # Mantiene una excepción específica para costos.


def ejecutar_operacion(nombre_operacion, operacion):  # Ejecuta una operación y controla sus posibles errores.
    try:  # Inicia el bloque protegido de ejecución.
        resultado = operacion()  # Ejecuta la función recibida como parámetro.
    except SistemaSoftwareFJException as error:  # Captura errores personalizados del sistema.
        print(f"Error controlado en {nombre_operacion}: {error}")  # Muestra el error sin detener el programa.
    except Exception as error:  # Captura errores inesperados de Python.
        raise SistemaSoftwareFJException("Ocurrió un error inesperado.") from error  # Encadena la causa original.
    else:  # Ejecuta este bloque solo si no ocurrió ningún error.
        print(f"Operación exitosa: {nombre_operacion}")  # Informa que la operación terminó correctamente.
        return resultado  # Retorna el resultado de la operación exitosa.
    finally:  # Ejecuta este bloque siempre, con error o sin error.
        print(f"Finalizó la operación: {nombre_operacion}")  # Informa que la operación llegó a su cierre.

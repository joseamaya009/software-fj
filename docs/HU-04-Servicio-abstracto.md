# HU-03: Servicio abstracto

Esta historia de usuario define la clase abstracta `Servicio`, que funciona como contrato para todos los servicios que ofrece Software FJ. A partir de esta clase deben nacer servicios concretos como reserva de salas, alquiler de equipos y asesorías.

La HU se enfoca en abstracción y polimorfismo, porque cada servicio debe calcular costos, describirse y validar parámetros de forma diferente, aunque todos compartan una misma estructura.

El resultado esperado es una base clara para que el sistema pueda crecer con nuevos servicios sin romper lo ya construido.

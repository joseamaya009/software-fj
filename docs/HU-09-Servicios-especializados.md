# HU-04: Servicios especializados

Esta historia de usuario implementa los tres servicios concretos que menciona el ejercicio: reserva de salas, alquiler de equipos y asesorías especializadas.

Cada servicio tiene reglas propias. Una sala puede depender de su capacidad, un equipo de la cantidad alquilada y una asesoría de las horas contratadas o nivel del consultor. Esto demuestra herencia y polimorfismo, porque todos son servicios, pero cada uno se comporta distinto.

El resultado esperado es que el sistema pueda crear servicios válidos, rechazar servicios incorrectos y calcular costos según el tipo real de servicio.

# HU-05: Gestión de reservas

Esta historia de usuario conecta clientes con servicios. Su propósito es permitir que Software FJ cree reservas, las confirme, las cancele y las procese sin perder el control del estado.

La reserva debe validar que exista un cliente, que exista un servicio, que la duración sea correcta y que no se realicen operaciones prohibidas, como confirmar una reserva cancelada.

El resultado esperado es una clase `Reserva` que centralice el flujo principal del sistema.

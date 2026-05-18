# HU-01: Entidad base abstracta

Esta historia de usuario define la base común del sistema Software FJ. Su objetivo es crear una clase abstracta que represente cualquier entidad principal del sistema, evitando repetir atributos y validaciones en clientes, servicios o reservas.

La HU trabaja especialmente los principios de abstracción, encapsulación y herencia. Desde esta base se pueden exigir métodos obligatorios como `validar()` y `describir()`, para que las clases hijas tengan una estructura uniforme.

El resultado esperado es una clase que no pueda instanciarse directamente, pero que sirva como punto de partida para las demás clases del proyecto.

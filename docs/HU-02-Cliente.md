# HU-02: Registro y validación de clientes

Esta historia de usuario permite registrar clientes de Software FJ con datos personales protegidos. La idea es que cada cliente tenga información básica como documento, nombre, correo y teléfono, pero que esos datos no se acepten sin validación.

La HU aplica encapsulación porque los atributos no se manipulan directamente. También cubre validaciones robustas para evitar correos inválidos, documentos vacíos o teléfonos mal formados.

El resultado esperado es una clase `Cliente` confiable, lista para asociarse con reservas y servicios.

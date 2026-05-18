# HU-01: Creación de la estructura del proyecto

Esta historia de usuario corresponde a la creación inicial de la estructura de carpetas del proyecto Software FJ.

Su objetivo es organizar el trabajo desde el inicio para que cada historia de usuario tenga su propio espacio, con sus archivos de documentación y, cuando aplique, sus archivos de código.

En esta HU no se desarrolla lógica en Python, porque su propósito no es implementar funcionalidades del sistema, sino preparar la base organizada del proyecto.

La estructura por carpetas permite trabajar de forma ordenada cada parte del ejercicio, separar responsabilidades y facilitar el paso de los cambios por ramas como desarrollo, pruebas y rama principal.

También ayuda a evitar confusiones al momento de revisar qué corresponde a cada historia de usuario, ya que cada carpeta conserva la documentación relacionada con su objetivo.

Como parte de esta HU se incluye un archivo `.gitignore` para evitar subir archivos generados automáticamente, como `__pycache__`, archivos compilados de Python, logs locales o entornos virtuales.

El resultado esperado de esta HU es una estructura inicial clara, limpia y lista para continuar con las siguientes historias de usuario del sistema.

## Criterios de aceptación

- La carpeta de la HU debe existir dentro del proyecto.
- La HU debe contener únicamente documentación y archivos de configuración necesarios.
- No debe incluir archivos `.py`, porque no implementa código funcional.
- Debe explicar el propósito de organizar el proyecto por carpetas.
- Debe incluir reglas para evitar subir archivos generados automáticamente al repositorio.

## Archivos de esta HU

- `HU-01-Creacion-estructura.md`: explica el objetivo general de la historia de usuario.
- `.gitignore`: evita subir archivos innecesarios o generados automáticamente.

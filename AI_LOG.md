# AI_LOG · Team Challenge Hundir la flota

Este registro no cuenta para la nota. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una parte, dejad el nivel en 0: también es un dato útil.

**Grupo:**  Brian Iraizos, Ludmila Campos, Diego Rodríguez y Almudena Mata

**Herramientas usadas:** Gemini

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por módulo

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA

| Módulo | Quién lo ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿Lo podríais repetir sin IA? (sí / en parte / no) |
|---|---|---|---|---|
| `variables.py` | Almudena | 0 | 0 | Sí, lo hice según las indicaciones de mis compañeros|
| `clases.py` | Ludmila | 2 | 15-20 | En parte |
| `funciones.py` | Diego | 2 | 12 | En parte |
| `main.py` | Brian | 3 | 6 | No |
| `README.md` | Almudena | 0 | 0 | Sí, pero no prometo que esté bien|

## Registro de prompts

Copiad este bloque por cada prompt que haya influido en vuestro código.

### Módulo clases.py · Prompt 1

- **Objetivo:** Definir la estructura base de la clase Tablero con id_jugador y organizar la ubicación de los atributos/símbolos y métodos en clases.py.
- **Prompt:** Consulta sobre cómo estructurar Tablero con id_jugador y tamano, dónde ubicar los símbolos del tablero y cómo limpiar métodos vacíos o duplicados.
- **Respuesta relevante:** Se definió incluir id_jugador en _init_, ubicar los símbolos del tablero en la parte superior/atributos y quitar métodos vacíos como recibir_disparos para evitar duplicados o confusión con el trabajo del equipo.
- **Cambios:** Se añadió id_jugador al constructor de Tablero, se ordenaron los atributos/símbolos, se mantuvo mostrar y colocar_barcos dentro de la clase con su indentación correspondiente y se eliminó recibir_disparos vacío.
- **Comprobación:** Se revisó el código en clases.py comprobando que los métodos accedieran a self.tamano y self.matriz sin errores de indentación ni de argumentos al instanciar Tablero.
- **Decisión propia:** Se decidió dejar recibir_disparos fuera de este código para que lo implemente el compañero encargado de esa parte.

### Módulo clases.py · Prompt 2

- **Objetivo:** Organizar el trabajo en ramas de Git (clases_tablero y logica_colocar_barcos), separar el arranque/pruebas y realizar el commit sin conflictos al unir ramas.
- **Prompt:** Preguntas sobre cómo separar la rama base de la rama con la lógica de colocar barcos, cómo unir las ramas sin duplicar código y qué poner al hacer commit en GitHub.
- **Respuesta relevante:** Se acordó mantener clases_tablero como base limpia, desarrollar mostrar y colocar_barcos en logica_colocar_barcos, dejar el mensaje de bienvenida/entrada del nombre en el arranque o pruebas y resolver los conflictos al hacer merge dejando una sola versión limpia.
- **Cambios:** Se ajustó el código de la rama para incluir el mensaje de bienvenida, el id_jugador y la prueba de creación/colocación/visualización del tablero, y se guardó en la rama correspondiente mediante Commit changes.
- **Comprobación:** Se verificó la ejecución del flujo de bienvenida, captura del nombre, creación del tablero, colocación de barcos y visualización en consola, y se confirmó que el commit quedó registrado en la rama.
- **Decisión propia:** Se decidió trabajar cada parte en su rama y coordinar la unión por Pull Requests para evitar pisar el código del resto del equipo.


### Módulo funciones.py · Prompt 1

- **Objetivo:** Implementar las funciones auxiliares del juego (`mostrar_instrucciones`, `pedir_coordenadas`, `disparo_aleatorio_maquina` y `quedan_barcos`).
- **Prompt:** Consultas para crear de forma sencilla y clara las funciones de `funciones.py` usando `random` y `numpy`, validando coordenadas del 0 al 9 y comprobando si quedan barcos.
- **Respuesta relevante:** Se definieron 4 funciones con bucle `while True` y `try/except` para validar entradas del usuario y generar disparos aleatorios no repetidos de la máquina.
- **Cambios:** Se simplificaron los textos, docstrings y validaciones para que el código fuera corto, legible y fácil de explicar.
- **Comprobación:** Se revisó la sintaxis y lógica de cada función en VS Code antes de subirla por Pull Request a `main`.
- **Decisión propia:** Se optó por la versión más simple del código y se añadió `.history/` al `.gitignore` para no subir copias locales de VS Code.





### Módulo X · Prompt 1

- **Objetivo:** qué queríais resolver.
- **Prompt:** copiadlo tal cual.
- **Respuesta relevante:** la parte que usasteis, resumida.
- **Cambios:** qué modificasteis y por qué.
- **Comprobación:** cómo verificasteis que funcionaba.
- **Decisión propia:** qué decidisteis vosotros.

### Módulo X · Prompt 1

- **Objetivo:** qué queríais resolver.
- **Prompt:** copiadlo tal cual.
- **Respuesta relevante:** la parte que usasteis, resumida.
- **Cambios:** qué modificasteis y por qué.
- **Comprobación:** cómo verificasteis que funcionaba.
- **Decisión propia:** qué decidisteis vosotros.


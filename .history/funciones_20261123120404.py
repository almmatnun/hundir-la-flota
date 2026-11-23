"""Módulo con las funciones auxiliares del juego Hundir la Flota."""

import random
import numpy as np

TAMANO_TABLERO = 10


def mostrar_instrucciones() -> None:
    """Muestra por pantalla las reglas básicas del juego Hundir la Flota."""
    print("\n--- INSTRUCCIONES DE HUNDIR LA FLOTA ---")
    print(f"1. El tablero es de {TAMANO_TABLERO}x{TAMANO_TABLERO} (filas y columnas del 0 al {TAMANO_TABLERO - 1}).")
    print("2. En tu turno, introduce una fila y una columna para disparar.")
    print("3. Si aciertas (tocado), vuelves a disparar. Si fallas (agua), pasa el turno.")
    print("4. Gana quien hunda primero todos los barcos del rival.\n")


def pedir_coordenadas(tamano: int = TAMANO_TABLERO) -> tuple[int, int]:
    """Solicita y valida las coordenadas (fila, columna) al jugador.

    Repite la petición hasta que el usuario introduzca dos números enteros
    válidos dentro del rango del tablero [0, tamano - 1].

    Args:
        tamano (int): Dimensión del tablero cuadrado. Por defecto TAMANO_TABLERO.

    Returns:
        tuple[int, int]: Tupla (fila, columna) validada.
    """
    while True:
        try:
            fila = int(input(f"Introduce la fila (0-{tamano - 1}): "))
            columna = int(input(f"Introduce la columna (0-{tamano - 1}): "))

            if 0 <= fila < tamano and 0 <= columna < tamano:
                return fila, columna

            print(f"Error: Las coordenadas deben estar entre 0 y {tamano - 1}.")
        except ValueError:
            print("Error: Entrada no válida. Introduce solo números enteros.")


def disparo_aleatorio_maquina(tablero_jugador, tamano: int = TAMANO_TABLERO) -> tuple[int, int]:
    """Genera una coordenada aleatoria donde la máquina no haya disparado antes.

    Comprueba las casillas ya disparadas en el tablero del jugador para
    garantizar que la máquina nunca repita un disparo.

    Args:
        tablero_jugador (Tablero | np.ndarray): Objeto Tablero del jugador o su matriz.
        tamano (int): Dimensión del tablero cuadrado. Por defecto TAMANO_TABLERO.

    Returns:
        tuple[int, int]: Tupla (fila, columna) libre para disparar.
    """
    matriz = tablero_jugador.matriz if hasattr(tablero_jugador, "matriz") else tablero_jugador

    while True:
        fila = random.randint(0, tamano - 1)
        columna = random.randint(0, tamano - 1)

        if matriz[fila, columna] not in ("X", "-"):
            return fila, columna


def quedan_barcos(tablero) -> bool:
    """Comprueba si todavía quedan casillas de barco sin hundir en el tablero.

    Args:
        tablero (Tablero | np.ndarray): Objeto Tablero a comprobar o su matriz.

    Returns:
        bool: True si queda al menos una casilla con barco ("B" u "O"), False si no.
    """
    matriz = tablero.matriz if hasattr(tablero, "matriz") else tablero
    return bool(np.any((matriz == "B") | (matriz == "O")))
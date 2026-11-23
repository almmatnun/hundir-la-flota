import random
import numpy as np


def mostrar_instrucciones():
    """Muestra las reglas del juego por pantalla."""
    print("HUNDIR LA FLOTA")
    print("Dispara a coordenadas del 0 al 9.")
    print("Si aciertas repites turno. Si fallas le toca a la máquina.")


def pedir_coordenadas():
    """Pide fila y columna al usuario y comprueba que sean válidas."""
    while True:
        try:
            fila = int(input("Fila (0-9): "))
            columna = int(input("Columna (0-9): "))

            if 0 <= fila <= 9 and 0 <= columna <= 9:
                return fila, columna
            else:
                print("Tiene que ser un número entre 0 y 9.")
        except ValueError:
            print("Eso no es un número, prueba otra vez.")


def disparo_aleatorio_maquina(tablero):
    """Elige una casilla al azar donde la máquina no haya disparado."""
    while True:
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)

        if tablero.matriz[fila, columna] != "X" and tablero.matriz[fila, columna] != "-":
            return fila, columna


def quedan_barcos(tablero):
    """Devuelve True si quedan barcos sin hundir en el tablero."""
    return "B" in tablero.matriz or "O" in tablero.matriz
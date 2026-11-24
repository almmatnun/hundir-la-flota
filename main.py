"""Punto de entrada y bucle principal de Hundir la Flota."""

from tablero import Tablero
from funciones import (
    mostrar_instrucciones,
    pedir_coordenadas,
    disparo_aleatorio_maquina,
    quedan_barcos,
    )

def iniciar_partida():
    """Prepara los tableros, coloca la flota y ejecuta el bucle de turnos."""
    print("¡Bienvenidos a Hundir la Flota!")
    mostrar_instrucciones()

    # 1. Preparación inicial
    nombre_jugador = input("Introduce tu nombre: ").strip() or "Jugador"
    tablero_jugador= Tablero(nombre_jugador)
    tablero_maquina= Tablero("Maquina")
    tablero_jugador.colocar_barcos_aleatorio ()
    tablero_maquina.colocar_barcos_aleatorio()
    tablero_jugador.mostrar()


    # 2. Bucle principal de la partida
    while True:
        # Turno del jugador
        print(f"\nTurno de {nombre_jugador}:")
        fila, columna = pedir_coordenadas()

        if tablero_maquina.matriz[fila][columna] == "B":
            tablero_maquina.matriz[fila][columna] = "X"
            print("¡TOCADO!")
        else:
            if tablero_maquina.matriz[fila][columna] == 0:
                tablero_maquina.matriz[fila][columna] = "-"
            print("¡AGUA!")

        if not quedan_barcos(tablero_maquina):
            print(f"\n¡Enhorabuena {nombre_jugador}, has ganado!")
            break

        # Turno de la máquina 
        print("\nTurno de la Máquina:")
        fila_m, col_m = disparo_aleatorio_maquina(tablero_jugador)
        print(f"La Máquina dispara a ({fila_m}, {col_m}):")

        if tablero_jugador.matriz[fila_m][col_m] == "B":
            tablero_jugador.matriz[fila_m][col_m] = "X"
            print("¡La Máquina te ha tocado un barco!")
        else:
            tablero_jugador.matriz[fila_m][col_m] = "-"
            print("¡La Máquina ha fallado (AGUA)!")

        tablero_jugador.mostrar()

        if not quedan_barcos(tablero_jugador):
            print("\nLa Máquina ha hundido todos tus barcos. ¡Has perdido!")
            break
       
if __name__ == "__main__":
    iniciar_partida()
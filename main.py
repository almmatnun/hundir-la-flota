"""Punto de entrada y bucle principal de Hundir la Flota."""

# TODO: Cuando estén listos los demás módulos, importa aquí lo necesario:
# from variables import TAMANO_TABLERO, ...
# from clases import Tablero
# from funciones import pedir_coordenadas, disparo_aleatorio_maquina, ...

def iniciar_partida():
    """Prepara los tableros, coloca la flota y ejecuta el bucle de turnos."""
    print("¡Bienvenidos a Hundir la Flota!")

    # 1. Preparación inicial
    nombre_jugador = input("Introduce tu nombre: ").strip() or "Jugador"
    # TODO: Crear tablero del jugador y tablero de la máquina (Tablero)
    # TODO: Colocar barcos en ambos tableros

    # 2. Bucle principal de la partida
    while True:
        
        # IR PONIENDO AQUI EL CODIGO DE BUCLE. DEBAJO LO QUE DEBERIA HACER.
        
        # --- Turno del jugador ---
        # TODO: Pedir coordenadas válidas al jugador
        # TODO: Aplicar disparo sobre el tablero de la máquina y mostrar resultado
        # TODO: Comprobar si quedan barcos en el tablero de la máquina;
        #       si no quedan, mostrar victoria del jugador y hacer `break`

        # --- Turno de la máquina ---
        # TODO: Ejecutar disparo aleatorio sin repetir sobre el tablero del jugador
        # TODO: Mostrar resultado y estado del tablero del jugador
        # TODO: Comprobar si quedan barcos en el tablero del jugador;
        #       si no quedan, mostrar victoria de la máquina y hacer `break`

if __name__ == "__main__":
    iniciar_partida()

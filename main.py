"""Punto de entrada y bucle principal de Hundir la Flota."""

from tablero import Tablero
from funciones import (
    mostrar_instrucciones,
    pedir_coordenadas,
    disparo_aleatorio_maquina,
    quedan_barcos,
    )
try:
    import pyttsx3
except ImportError:
    pyttsx3= None
    
    
def decir_frase(texto, indice_voz=0, velocidad=175):
  """Lee un texto en voz alta con la voz elegida y un ritmo más natural."""
  if pyttsx3 is None:
    return
  try:
    motor = pyttsx3.init()
    voces = motor.getProperty("voices")
    if voces and 0 <= indice_voz < len(voces):
      motor.setProperty("voice", voces[indice_voz].id)
    motor.setProperty("rate", velocidad)
    motor.say(texto)
    motor.runAndWait()
    motor.stop()
  except Exception:
    pass

def iniciar_partida():
    """Prepara los tableros, coloca la flota y ejecuta el bucle de turnos."""
    print("¡Bienvenidos a Hundir la Flota!")
    decir_frase("¡Hola que tal! Que alegrìa tenerte por aquì,¡Bienvenidos a Hundir la Flota!")
    mostrar_instrucciones()

    # 1. Preparación inicial
    nombre_jugador = input("Introduce tu nombre: ").strip() or "Jugador"
    decir_frase(f"¡vamos allà! {nombre_jugador}! estas listo para comenzar? ¡a jugar!")
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
            decir_frase("¡Boom!! directo al blanco! Barco TOCADO!")
        else:
            if tablero_maquina.matriz[fila][columna] == 0:
                tablero_maquina.matriz[fila][columna] = "-"
            print("¡AGUA!")
            decir_frase("¡Nada de nada! solo agua por esta zona")

        if not quedan_barcos(tablero_maquina):
            print(f"\n¡Enhorabuena {nombre_jugador}, Has ganado!🏆")
            decir_frase(f"WOW!,{nombre_jugador},GANASTE!")
            break

        # Turno de la máquina 
        print("\nTurno de la Máquina:")
        fila_m, col_m = disparo_aleatorio_maquina(tablero_jugador)
        print(f"La Máquina dispara a ({fila_m}, {col_m}):")

        if tablero_jugador.matriz[fila_m][col_m] == "B":
            tablero_jugador.matriz[fila_m][col_m] = "X"
            print("¡La Máquina te ha tocado un barco!")
            decir_frase("LA MAQUINA TE HA TOCADO UN BARCO! mala suerte....")
        else:
            tablero_jugador.matriz[fila_m][col_m] = "-"
            print("¡La Máquina ha fallado (AGUA)!")
            decir_frase("¡LA MAQUINA HA FALLADO (AGUA)!")

        tablero_jugador.mostrar()

        if not quedan_barcos(tablero_jugador):
            print("\nLa Máquina ha hundido todos tus barcos. ¡Has perdido!🙇‍♂️")
            decir_frase("GAME OVER, HAS PERDIDO! gua gua guaaaa")
            break
    while True:
        respuesta = input("\¿Quieres volver a jugar? ('s'/'n'):").strip().lower()
        if respuesta == "s":
            print("¡Reiniciando partida...!\nCargando nuevos tableros...\n")
            break
        elif respuesta == "n":
            print("¡Gracias por jugar! Hasta la proxima.")
            break
        else:
            print("Por Favor , introduce 's' para si o 'n' para no.")
       
if __name__ == "__main__":
    iniciar_partida()

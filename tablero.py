import numpy as np  
import random
class Tablero:
    def __init__(self, id_jugador,  tamano=10):
        self.id_jugador = id_jugador
        self.tamano=tamano
        self.matriz = np.zeros((tamano, tamano), dtype=object)
        
        
    def mostrar(self):
        """muestra el tablero actual por pantalla"""
        print("   " + " ".join([str(i)for i in range(self.tamano)]))
        print("   " + "-" * (self.tamano * 3))
        for i, fila in enumerate(self.matriz):
            elementos_fila =[]
            for celda in fila:
                if celda == 0 or celda == "0":
                    elementos_fila.append("🟦")
                else:
                    elementos_fila.append("🚢")
            fila_formateada = "|".join(elementos_fila)
            print(f"{i} | {fila_formateada}")
    def colocar_barcos_aleatorio(self):
        #logica para posicionar los barcos en el tablero
            #1definimos la flota(tamaño de cada barco)
            # 4 barcos de 1 casilla de eslora 3 barcos de 2 casillas de eslora 2 barcos de 3 casillas de eslora 1 barco de 4 casillas de eslora
        flota= [
            {"nombre": "Portaaviones (eslora 4)", "eslora": 4},
            {"nombre": "Buque 1 (eslora 3)", "eslora": 3},
            {"nombre": "Buque 2 (eslora 3)", "eslora": 3 },
            {"nombre": "Destructor 1 (eslora 2)", "eslora":2},
            {"nombre": "Destructor 2 (eslora 2)", "eslora": 2},
            {"nombre": "Destructor 3 (eslora 2)", "eslora": 2},
            {"nombre": "Lancha 1 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 2 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 3 (eslora 1)","eslora":1 },
            {"nombre": "Lancha 4 (eslora 1)","eslora":1 },
        ]
        
        for barcos in flota:
            eslora = barcos["eslora"]
            colocado = False
            
            while not colocado:
                orientacion = random.choice(["H", "V"])
                fila = random.randint(0, self.tamano -1)
                columna = random.randint(0, self.tamano -1)
                #verificar que no se salga del tablero 
                if orientacion == "H" and columna + eslora > self.tamano:
                    continue
                if orientacion== "V" and fila + eslora > self.tamano:
                    continue
                
                #veridicar que todas las casillas esten libres (0)
                espacio_libre = True
                for j in range(eslora):
                    if orientacion == "H":
                        if self.matriz[fila][columna + j] != 0:
                            espacio_libre = False
                            break
                if not espacio_libre:
                    continue
                #Colocar el barco con "B"
                for j in range(eslora):
                    if orientacion == "H":
                        self.matriz[fila][columna + j] = "B"
                    else:
                        self.matriz[fila + j][columna] = "B"
                        
                colocado = True
print("La maquina ha colocado su flota")
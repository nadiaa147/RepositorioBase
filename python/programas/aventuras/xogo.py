from localizacion import *
from objeto import *
from personaje import *

class Juego:
	def __init__(self):
		self.mapamundi = Mapamundi()
		self.jugador = Personaje("Jugador", self.mapamundi.mapa[(0,0,0)])

	def jugar(self):
		print("¡Bienvenido a la aventura de texto!")
		self.jugador.lugar_actual.mostrar_info()
		while True:
			comando = input("\n¿Qué quieres hacer?")
			if len(comando) == 0:
				continue

			if comando[0] in ["ir","mover"]:
				if len(comando) > 1:
					self.jugador.mover(comando[1], self)
				else:
					print("¿En qué dirección quieres ir?")

			elif comando[0] == "recoger":
				if len(comfando) > 1:
					self.jugador.recoger(" ".join(comando[1:]))
				else:
					print("¿Qué quieres recoger?")

			elif comando[0] == "inventario":
				self.jugador.mostrar_inventario()

			elif comando[0] in ["salir", "exit"]:
				print("¡Gracias por jugar!")
				break

			else:
				print("No entiendo este comando.")

# Iniciando el juego
if __name__ == "__main__":
	juego = Juego()
	juego.jugar()
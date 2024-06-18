from localizacion import *
from personaje import *

class Juego:
	def __init__(self):
		self.mapamundi = Mapamundi()
		self.jugador = Personaje("Jugador", self.mapamundi.mapa[(0,0,0)])

	def jugar(self):
		print("¡Bienvenido a la aventura de texto!")
		self.jugador.lugar_actual.mostrar_info()
		final = False
		while final == False:
			print(final)
			comando = input("\n¿Qué quieres hacer?").lower().split()
			if len(comando) == 0:
				continue

			if comando[0] in ["ir","mover"]:
				if len(comando) > 1:
					self.jugador.mover(comando[1], self.mapamundi)
				else:
					print("¿En qué dirección quieres ir?")

			elif comando[0] == "recoger":
				if len(comando) > 1:
					self.jugador.recoger(" ".join(comando[1:]))
				else:
					print("¿Qué quieres recoger?")
			elif comando[0] == "encender":
				if len(comando) > 1:
					self.jugador.encender(" ".join(comando[1:]))
				else:
					print("Qué quieres encender?")
			elif comando[0] == "buscar":
				self.jugador.buscar()


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
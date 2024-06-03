class Juego:
	def __init__(self):
		self.jugador = None
		self.lugar = ()
		self.crear_mundo()

	def crear_mundo(self, descripcion, coordenadas):
		# Creando los lugares con sus coordenadas correspondientes
		comedor = Lugar("Comedor", "Estás en el comedor, con una puerta al este, oeste y arriba", (0,1,1))
		porche = Lugar("Porche", "Estás en el porche. Tiene una puerta al este y al norte", (0,0,0))
		salon = Lugar("Salón", "Estás en el salón, con puertas al oeste y al norte", (0,0,1))
		cocina = Lugar("Cocina", "Estás en la cocina, con una puerta al oeste y al sur ", (0,1,0))
		habitan = Lugar("Habitación", "Estás en la habitación. Tiene una puerta abajo", (1,1,1))

		# Agregando lugares al diccionario de lugares
		self.lugares[comedor.(0,1,1)] = comedor
		self.lugares[porche.(0,0,0)] = porche
		self.lugares[salon.(0,0,1)] = salon
		self.lugares[cocina.(0,1,0)] = cocina
		self.lugares[habitacion.(1,1,1)] = habitación

		# Creando objetos
		llave = Objeto("Llave", "Una llave plateada.")
		bate = Objeto("Bate", "Un bate de béisbol. Es de madera")
		linterna = Objeto("Linterna", "Una linterna con una luz muy potente.")
		joya = Objeto("Joya", "Es una piedra preciosa de color rojo")
		cuchillo = Objeto()

		# Agregando objetos a lugares
		comedor.append_objeto(cuchillo)
		porche.append_objeto(llave)
		salon.append_objeto(bate)
		cocina.append_objeto(linterna)
		habitacion.append_objeto(joya)

		# Creando jugador
		self.jugador = Personaje("Jugador", porche)

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

			elif comando[0] in ["salir", "exit"]
				print("¡Gracias por jugar!")
				break

			else:
				print("No entiendo este comando.")

# Iniciando el juego
if __name__ == "__main__":
	juego = Juego()
	juego.jugar()
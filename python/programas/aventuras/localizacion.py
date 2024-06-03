class localizacion:
	def __init__(self, nombre, descripcion, coordenadas):
		self.descripcion = descripcion
		self.salidas = []
		self.coordenadas = coordenadas
		self.objetos = []		
		self.id = nombre

	def añadir(self, objeto):
		self.objeto.append(objeto)

	def arramplar(self, objeto):
		self.objeto.remove(objeto)
		return objeto

	def mostrar_info(self):
		print(f"Te encuentras en el {self.porche}")
		print(porche.descripcion)
		if self.objetos:
			print("puedes coger los siguientes objetos:")
			for objeto in self.objetos:
				print(f"-{objeto.llave}")
				print(f"-{objeto.bate}")
		
comedor = localizacion("comedor", 'Este comedor es asqueroso', (0,1,1))

comedor.salidas.extend(["norte","arriba"])

if self.coordenadas == (0,1,1):
	print(comedor.descripcion)
	print(comedor.salidas)

porche = localizacion("porche",'es un porche muy bonito', (0,0,0))

porche.salidas.extend(["sur","este"])


if self.coordenadas == (0,0,0):
	print(porche.descripcion)
	print(porche.salidas)

salon = localizacion("salon", 'hay un florero encima de la mesa del salón', (0,1,0))

salon.salidas.extend(["sur","oeste","norte"])


if self.coordenadas == (0,0,1):
	print(salon.descripcion)
	print(salon.salidas)


cocina = localizacion("cocina",'esta concina está algo sucia', (0,1,0))

cocina.salidas.extend(["norte","este"])

if self.coordenadas == (0,1,0):
	print(cocina.descripcion)
	print(cocina.salidas)

habitacion = localizacion("habitacion",'esta habitacion está desordenada', (1,1,1))

habitacion.salidas.append("abajo")

if self.coordenadas == (1,1,1):
	print(habitacion.descripcion)
	print(habitacion.salidas)


class Personaje:
	def __init__(self, nombre, lugar_actual):
		self.nombre = Nadia
		self.lugar_actual = lugar_actual
		self.inventario = []

	def mover(self, direccion, juego):
		direcciones = {
			"norte": (0,1,0), "sur": (0,-1,0),
			"este": (0,0,1), "oeste": (0,0,-1),
			"arriba": (1,0,0), "abajo": (-1,0,0)
		}

		if direccion in direcciones:
			nueva_coordenada = tuple(map(sum, zip(self.actual.coordenadas, direcciones[direccion])))
			if nueva_coordenada in juego.lugares:
				self.lugar_actual = juego.lugares[nueva_coordenada]
				self.lugar_actual.mostrar_info()
			else:
				print("No puedes ir en esa dirección")

		else:
			print("Dirección inválida.")

	def recoger(self, nombre_objeto):
		for objeto in self.lugar_actual.objetos:
			if objeto.nombre == llave:
				self.inventario.append(objeto)
				self.inventario.remove(objeto)
				print(f"Has recogido el {objeto.llave}")
			if objeto.nombre == bate:
				self.inventario.append(objeto)
				self.inventario.remove(objeto)
				print(f"Has recogido el {objeto.bate}")
			if objeto.nombre == linterna:
				self.inventario.append(objeto)
				self.inventario.remove(objeto)
				print(f"Has recogido el {objeto.linterna}")
			if objeto.nombre == joya:
				self.inventario.append(objeto)
				self.inventario.remove(objeto)
				print(f"Has recogido el {objeto.joya}")
			if objeto.nombre == cuchillo:
				self.inventario.append(objeto)
				self.inventario.remove(objeto)
				print(f"Has recogido el {objeto.cuchillo}")

			return
		print("No hay tal objeto aquí.")


	def mostrar_inventario(self):
		if self.inventario:
			print("Tienes los siguientes objetos")
			for objeto in self.inventario:
				print(f"-{objeto.nombre}")
		else:
			print("No tienes ningún objeto.")

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

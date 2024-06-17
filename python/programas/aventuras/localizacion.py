from objeto import*

class Localizacion:
	def __init__(self, nombre, descripcion, coordenadas):
		self.nombre = nombre
		self.descripcion = descripcion
		self.coordenadas = coordenadas
		self.objetos = []
		self.salidas = []

	def agregar_objetos(self, objetos):
		self.objetos.append(objetos)

	def arramplar_objetos(self, objetos):
		self.objetos.remove(objetos)
		return objeto

	def mostrar_info(self):
		print(f"Te encuentras en el {self.nombre}")
		print(self.descripcion)
		

class Mapamundi:
	def __init__(self):
		self.mapa = {}
		self.cartografiar()

	def cartografiar(self):
		# Creando los lugares con sus coordenadas correspondientes (x, y, z)
		comedor = Localizacion("Comedor", "Estás en el comedor y hay una mesa grande que ocupa bastante espacio. Hay una puerta al este, oeste y arriba", (0,1,1))
		porche = Localizacion("Porche", "Estás en el porche. Es algo moderno y tiene varias macetas. Tiene una puerta al este y al norte", (0,0,0))
		salon = Localizacion("Salón", "Estás en el salón. Hay dos sofás de color azul. Hay puertas al oeste y al norte", (0,0,1))
		cocina = Localizacion("Cocina", "Te encuentras en una cocina un poco sucia. Hay una puerta al oeste y al sur ", (0,1,0))
		habitacion = Localizacion("Habitación", "Estás en una habitación, parece ser de un niño pequeño. Tiene una puerta abajo", (1,1,1))

		# Agregando lugares al diccionario de lugares
		self.mapa[comedor.coordenadas] = comedor
		self.mapa[porche.coordenadas] = porche
		self.mapa[salon.coordenadas] = salon
		self.mapa[cocina.coordenadas] = cocina
		self.mapa[habitacion.coordenadas] = habitacion

		# Creando salidas
		salidas = {}
		salidas [(0,0,0)] = ["este","norte"]
		salidas [(0,0,1)] = ["oeste","norte"]
		salidas [(0,1,0)] = ["oeste","sur"]
		salidas [(0,1,1)] = ["este","oeste", "arriba"]
		salidas [(1,1,1)] = ["abajo"]

		# Creando objetos
		llave = Objeto("Llave", "Una llave plateada.")
		porche.agregar_objetos(llave)

		bate = Objeto("Bate", "Un bate de béisbol. Es de madera.")
		salon.agregar_objetos(bate)

		linterna = Objeto("Linterna", "Una linterna con una luz muy potente.")
		cocina.agregar_objetos(linterna)

		joya = Objeto("Joya", "Es una piedra preciosa de color rojo.")
		habitacion.agregar_objetos(joya)

		cuchillo = Objeto("Cuchillo", "Es un cuchillo con bastante sierra.")
		comedor.agregar_objetos(cuchillo)
from objeto import*

class localizacion:
	def __init__(self, nombre, descripcion, coordenadas):
		self.descripcion = descripcion
		self.salidas = []
		self.coordenadas = coordenadas
		self.objetos = []		
		self.nombre = nombre

	def añadir(self, objetos):
		self.objeto.append(objeto)

	def arramplar(self, objetos):
		self.objeto.remove(objeto)
		return objeto

	def mostrar_info(self):
		print(f"Te encuentras en el {self.nombre}")
		print(self.descripcion)
		if self.objetos:
			print("puedes coger los siguientes objetos:")
			for objeto in self.objetos:
				print(f"-{objeto.nombre}")
				print(f"-{objeto.nombre}")
		

class Mapamundi:
	def __init__(self):
		self.mapa = llave
		self.cartografiar()

	def cartografiar(self):
		# Creando los lugares con sus coordenadas correspondientes (x, y, z)
		comedor = localizacion("Comedor", "Estás en el comedor, con una puerta al este, oeste y arriba", (0,1,1))
		porche = localizacion("Porche", "Estás en el porche. Tiene una puerta al este y al norte", (0,0,0))
		salon = localizacion("Salón", "Estás en el salón, con puertas al oeste y al norte", (0,0,1))
		cocina = localizacion("Cocina", "Estás en la cocina, con una puerta al oeste y al sur ", (0,1,0))
		habitan = localizacion("Habitación", "Estás en la habitación. Tiene una puerta abajo", (1,1,1))

		# Agregando lugares al diccionario de lugares
		self.mapa[comedor.coordenadas] = comedor
		self.mapa[porche.coordenadas] = porche
		self.mapa[salon.coordenadas] = salon
		self.mapa[cocina.coordenadas] = cocina
		self.mapa[habitacion.coordenadas] = habitación

		# Creando objetos
		llave = Objeto("Llave", "Una llave plateada.")
		bate = Objeto("Bate", "Un bate de béisbol. Es de madera.")
		linterna = Objeto("Linterna", "Una linterna con una luz muy potente.")
		joya = Objeto("Joya", "Es una piedra preciosa de color rojo.")
		cuchillo = Objeto("Cuchillo", "Es un cuchillo con bastante sierra.")

		# Agregando objetos a lugares
		comedor.agregar_objeto(cuchillo)
		porche.agregar_objeto(llave)
		salon.agregar_objeto(bate)
		cocina.agregar_objeto(linterna)
		habitacion.agregar_objeto(joya)
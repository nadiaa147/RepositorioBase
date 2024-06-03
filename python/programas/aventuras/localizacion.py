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
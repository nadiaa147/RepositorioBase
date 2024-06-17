# personaje.py
class Personaje:
	def __init__(self, nombre, lugar_actual):
		self.nombre = nombre
		self.lugar_actual = lugar_actual
		self.inventario = []

	def mover(self, direccion, mapamundi):
		direcciones = {
			"norte": (0,1,0), "sur": (0,-1,0),
			"este": (0,0,1), "oeste": (0,0,-1),
			"arriba": (1,0,0), "abajo": (-1,0,0)
		}

		if direccion in direcciones:
			nueva_coordenada = tuple(map(sum, zip(self.lugar_actual.coordenadas, direcciones[direccion])))
			if nueva_coordenada in mapamundi.mapa:
				self.lugar_actual = mapamundi.mapa[nueva_coordenada]
				self.lugar_actual.mostrar_info()
			else:
				print("No puedes ir en esa dirección")

		else:
			print("Dirección inválida.")

	def recoger(self, nombre_objeto):
		for objeto in self.lugar_actual.objetos:
			if objeto.nombre.lower() == nombre_objeto.lower():
				self.inventario.append(objeto)
				self.lugar_actual.objetos.remove(objeto)
				print(f"Has recogido el {objeto.nombre}")
				return
		print("No hay tal objeto aquí.")

	def buscar(self, nombre_objeto):
		for objeto in self.lugar_actual.objetos:
			if objeto.nombre.lower() == nombre_objeto.lower():
				if lugar_actual = [0,0,0]
					print("en este lugar hay una llave.")
				if lugar_actual = [0,1,1]
					print("en este lugar hay un cuchillo.")
				if lugar_actual = [0,0,1]
					print("en este lugar hay un bate")
				if lugar_actual = [0,1,0]
					print("en este lugar hay una linterna")
				if lugar_actual = [1,1,1]
					print("en este lugar hay una joya")

		return

	def mostrar_inventario(self):
		if self.inventario:
			print("Tienes los siguientes objetos")
			for objeto in self.inventario:
				print(f"-{objeto.nombre}")
		else:
			print("No tienes ningún objeto.")

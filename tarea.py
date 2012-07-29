class tarea():

	"""
		Tiempo llegada, Tiempo inicial, Tiempo final, Espacio de memoria
		ID, Tiempo de duración, Estado.

	"""
	tiempoLlegada = 0
	tiempoDuracion = 0
	tiempoInicial = 0
	tiempoFinal = 0
	memoria = 0
	idtar = ""
	estado = ""
	prioridad = ""

	"""
	setters de las tareas

	"""
	def setTiempollegada(self, tiempo):
		global tiempoLlegada
		tiempoLlegada = tiempo

	def setTiempoDuracion(self, tiempo):
		global tiempoDuracion
		tiempoDuracion = tiempo

	def setTiempoInicial(self, tiempo):
		global tiempoInicial
		tiempoInicial = tiempo

	def setTiempoFinal(self, tiempo):
		global tiempoFinal
		tiempoFinal = tiempo

	def setMemoria(self, memoria):
		global memoria
		memoria = self.memoria

	def setID(self, idnombre):
		global idtar
		idtar = idnombre

	def setEstado(self, estado):
		global estado
		estado = self.estado

	def setPrioridad(self, prioridad):
		global prioridad
		prioridad = self.prioridad

	"""
	getters de las tareas

	"""
	def getTiempollegada(self):
		return tiempoLlegada

	def setTiempoDuracion(self):
		return tiempoDuracion

	def setTiempoInicial(self):
		return tiempoInicial

	def setTiempoFinal(self):
		return tiempoFinal

	def setMemoria(self):
		return memoria

	def setID(self):
		return idtar

	def setEstado(self):
		return estado

	def setPrioridad(self):
		return prioridad

	def __init__(self, idtar, memoria, tiempoLlegada, tiempoDuracion):
		setID(idtar)
		setTiempollegada(tiempoLlegada)
		setTiempoDuracion(tiempoDuracion)
		
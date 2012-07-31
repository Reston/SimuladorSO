# -*- coding: utf-8 *-*
class Tarea:
	"""
		Tiempo llegada, Tiempo inicial, Tiempo final, Espacio de memoria
		ID, Tiempo de duración, Estado.
	"""

	#setters de las tareas
	def setTiempollegada(self, tiempo):
		self.tiempoLlegada = tiempo

	def setTiempoDuracion(self, tiempo):
		self.tiempoDuracion = tiempo

	def setTiempoInicial(self, tiempo):
		self.tiempoInicial = tiempo

	def setTiempoFinal(self, tiempo):
		self.tiempoFinal = tiempo

	def setMemoria(self, smemoria):
		self.memoria = smemoria

	def setID(self, idnombre):
		self.idtar = idnombre

	def setEstado(self, sestado):
		self.estado = sestado

	def setPrioridad(self, sprioridad):
		self.prioridad = sprioridad


	#getters de las tareas
	def getTiempollegada(self):
		return self.tiempoLlegada

	def getTiempoDuracion(self):
		return self.tiempoDuracion

	def getTiempoInicial(self):
		return self.tiempoInicial

	def getTiempoFinal(self):
		return self.tiempoFinal

	def getMemoria(self):
		return self.memoria

	def getID(self):
		return int(self.idtar)

	def getEstado(self):
		return self.estado

	def getPrioridad(self):
		return self.prioridad

	def imprimir(self):
		print 'id:'+str(self.idtar)+' memoria:'+str(self.memoria)+' tiempo de llegada:'+str(self.tiempoLlegada)+' duracion:'+str(self.tiempoDuracion)


	def __init__(self, idtar, memoria, tiempoLlegada, tiempoDuracion):
		self.tiempoLlegada = tiempoLlegada
		self.tiempoDuracion = tiempoDuracion
		self.tiempoInicial = 0
		self.tiempoFinal = 0
		self.memoria = memoria
		self.idtar = idtar
		self.estado = ""
		self.prioridad = ""

	def __repr__(self):
		return repr((self.idtar))

# -*- coding: utf-8 *-*
class Listas:

	#getters de las listas
	def getTareasAlta(self):
		for tar in self.proAlta:
			print tar
		return self.proAlta

	def getTareaByIdAlta(self, fId):
		for tar in self.proAlta:
			if(tar.getID()>=fId):
				return tar

	def getTareasMedi(self):
		for tar in self.proMedi:
			print tar
		return self.proMedi

	def getTareasBaja(self):
		for tar in self.proBaja:
			print tar
		return self.proBaja

	#setters de las listas
	def setTareaAlta(self, tar):
		self.proAlta.append(tar)

	def setTareaBaja(self, tar):
		self.proBaja.append(tar)

	def setTareaMedi(self, tar):
		self.proMedi.append(tar)

	def __init__(self):
		self.proAlta = []
		self.proMedi = []
		self.proBaja = []
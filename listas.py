class listas():

	proAlta = []
	proMedi = []
	proBaja = []

	def getTareasAlta(self):

		for tar in proAlta:
			print tar

		return proAlta

	def getTareasMedi(self):

		for tar in proMedi:
			print tar

		return proMedi

	def getTareasBaja(self):
		
		for tar in proBaja:
			print tar

		return proBaja

	def setTareaAlta(self, tar):
		global proAlta
		proAlta.Append(tar)

	def setTareaBaja(self, tar):
		global proBaja
		proBaja.Append(tar)

	def setTareaMedi(self, tar):
		global proMedi
		proMedi.Append(tar)

	def __init__(self):
		pass
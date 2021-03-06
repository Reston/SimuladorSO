# -*- coding: utf-8 *-*

"""
Elaborado por: Chavez, Ordoñez y Saavedra.
Universidad rafael belloso chacin
Intento de commit por programa

Simulador de tareas en un sistema operativo Enunciado:
Generar Tareas:
-Tamaño proceso
-Tiempo de ejecución
-Prioridad ->   -Alta 20%
				-Media 50%
				-BAja 30%

Estados de las tareas:                  Interfaz de entrada:
-En ejecución                           -Número de tareas
-Suspendidas                            -Espacio de memoria
-Bloqueadas                             -Tiempo de ejecución del Simulador
-Terminado

Interfaz de salida:
-Cantidad de tareas ejecutadas
-Estados en el que quedaron las tareas
-tiempo promedio de ejecución por tareas

	Requisitos:
1. Informe técnico.
2. Código.
3. Ejecución.
4. Conclusiones.
5. Recomendaciones.
"""
import operator
import datetime
import wx
import random
from constants import *
from tarea import Tarea

class SisOpe(wx.Frame):

	def __init__(self, parent, title, id):
		wx.Frame.__init__(self, parent,id, title=title, size=(250, 230))
		panel = wx.Panel(self)
		
		#Definir boton iniciar - QUE USAIS PA ACOMODAR LA POSICION?
		boton = wx.Button(panel,label="Iniciar",pos=(55,140),size=(60,30))
		self.Bind(wx.EVT_BUTTON, self.iniciarSimulacion,boton)

		#cajas de texto
		self.text1=wx.StaticText(panel,-1,"Número de tareas:".decode('utf-8'),(10,30))
		self.text2=wx.StaticText(panel,-1,"Espacio de memoria:",(10,52))
		self.text3=wx.StaticText(panel,-1,"Tiempo de ejecución:".decode('utf-8'),(10,74))


		self.ntarea=wx.TextCtrl(panel,-1,'',(120,30),(120,-1))
		self.espacio=wx.TextCtrl(panel,-1,'',(120,50),(120,-1))
		self.tiempo=wx.TextCtrl(panel,-1,'',(120,70),(120,-1))

		# Inicializa un menú
		filemenu = wx.Menu()
		filemenuh = wx.Menu()

		# Crea items del menú
		menu_save = filemenu.Append(wx.ID_SAVE, MENU_GUARDAR, STATUS_GUARDAR)
		menu_exit = filemenu.Append(wx.ID_EXIT, MENU_SALIR, STATUS_SALIR)

		menu_help = filemenuh.Append(wx.ID_HELP, MENU_HELP, STATUS_HELP)
		menu_about = filemenuh.Append(wx.ID_ABOUT, MENU_ABOUT, STATUS_ABOUT)

		# Crea la barra de menú
		menubar = wx.MenuBar()
		menubar.Append(filemenu, MENU_TITLE)  # Titulo del menu1
		menubar.Append(filemenuh, '&Ayuda') # Titulo del menu2
		self.SetMenuBar(menubar)  # Agrega la barra de menu al frame

		# Establece eventos
		self.Bind(wx.EVT_MENU, self.on_save, menu_save)
		self.Bind(wx.EVT_MENU, self.on_about, menu_about)
		self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)

		self.Centre(True)  # Centrar la ventana en pantalla
		self.Show(True)  # Mostrar la ventana

	def iniciarSimulacion(self, event):
		self.listaAlta  = []
		self.listaMedia = []
		self.listaBaja  = []
		self.listaFinal = []
		if self.tiempo.GetValue() != '':
			self.GenerarTareas(int(self.ntarea.GetValue()),int(self.espacio.GetValue()), int(self.tiempo.GetValue()))
			self.SimularSistema(int(self.tiempo.GetValue()),int(self.espacio.GetValue()))
		
		print "\n"
		#VER CUANTAS TAREAS TIENE CADA LISTA
		#print str(len(self.listaAlta))+" + "+str(len(self.listaMedia))+" + "+str(len(self.listaBaja))+" = "+str(len(self.listaAlta)+len(self.listaMedia)+len(self.listaBaja))
		
		
		detalles = "ID\tEstado\t\tMemoria\tTiempo Inicial\tTiempo Final\tDuracion\tTiempo llegada\tPrioridad\n"
		for self.tar in self.listaAlta:
			if (self.tar.getTiempoFinal() >= int(self.tiempo.GetValue())):
				self.tar.setEstado("En ejecucion")
			else:
				if self.tar.getTiempoDuracion()==0:
					self.tar.setEstado("Suspendidas")
				elif self.tar.getTiempoDuracion()!=0:
					self.tar.setEstado("Terminado")
			
			detalles+= str(self.tar.getID())+"\t"+self.tar.getEstado()+"\t"+str(self.tar.getMemoria())+"\t"+str(self.tar.getTiempoInicial())+"\t\t"+str(self.tar.getTiempoFinal())+"\t\t"+str(self.tar.getTiempoDuracion())+"\t"+str(self.tar.getTiempoLlegada())+"\t\tAlta\n"
		
		detalles+= "\n"
		for self.tar in self.listaMedia:
			if (self.tar.getTiempoFinal() >= int(self.tiempo.GetValue())):
				self.tar.setEstado("En ejecucion")
			else:
				if self.tar.getTiempoDuracion()==0:
					self.tar.setEstado("Suspendidas")
				elif self.tar.getTiempoDuracion()!=0:
					self.tar.setEstado("Terminado")

			detalles+= str(self.tar.getID())+"\t"+self.tar.getEstado()+"\t"+str(self.tar.getMemoria())+"\t"+str(self.tar.getTiempoInicial())+"\t\t"+str(self.tar.getTiempoFinal())+"\t\t"+str(self.tar.getTiempoDuracion())+"\t"+str(self.tar.getTiempoLlegada())+"\t\tMedia\n"
		detalles+= "\n"

		for self.tar in self.listaBaja:
			if (self.tar.getTiempoFinal() >= int(self.tiempo.GetValue())):
				self.tar.setEstado("En ejecucion")
			else:
				if self.tar.getTiempoDuracion()==0:
					self.tar.setEstado("Suspendidas")
				elif self.tar.getTiempoDuracion()!=0:
					self.tar.setEstado("Terminado")

			detalles+= str(self.tar.getID())+"\t"+self.tar.getEstado()+"\t"+str(self.tar.getMemoria())+"\t"+str(self.tar.getTiempoInicial())+"\t\t"+str(self.tar.getTiempoFinal())+"\t\t"+str(self.tar.getTiempoDuracion())+"\t"+str(self.tar.getTiempoLlegada())+"\t\tBaja\n"
		 
		resultado = Resultado(self,detalles, self.tiempo.GetValue(), self.ntarea.GetValue())
		resultado.Show(True)
		resultado.MakeModal(True)
	
	def GenerarTareas(self, numTar, espMem, tiempo):
		tareaNum=0
		x=0
		while tareaNum<numTar:			#WHILE PARA QUE SE CREEN TODAS LAS TAREAS
			x+=1
			if x>tiempo:
				x=0
			var=random.randint(1,100)
			if(var<=10):				#10% DE CHANCE DE CREAR UNA TAREA
				tareaNum+=1 			#NUMERO ACTUAL DE TAREAS + 1
				self.tar = Tarea(int(tareaNum), random.randint(5, 30), int(x), random.randint(5, 60)) #CREAR LA TAREA
				prior=random.randint(1,100)  #VARIABLE PARA VER LA PRIORIDAD
				if(prior<=20):
					self.listaAlta.append(self.tar)
				elif(prior>=70):
					self.listaBaja.append(self.tar)
				else:
					self.listaMedia.append(self.tar)
		return None

	def SimularSistema(self, tiempo, memoriaTotal):
		self.listaAlta.sort(key=operator.attrgetter('tiempoLlegada'))
		x = 0
		memoriaUsada = 0
		while x<=tiempo:
			x+=1
			for self.tar in self.listaAlta:
				if self.tar.tiempoLlegada==x:
					if(self.revisar_memoria(memoriaTotal, memoriaUsada, self.tar.memoria)):
						memoriaUsada += self.tar.memoria
						self.set_timers(x, self.tar.tiempoDuracion)
					else:
						self.listaAlta.append(self.tar)
						self.listaAlta.pop(self.listaAlta.index(self.tar))
				if self.tar.tiempoFinal==x:
					memoriaUsada -= self.tar.memoria

			for self.tar in self.listaMedia:
				if self.tar.tiempoLlegada==x:
					if(self.revisar_memoria(memoriaTotal, memoriaUsada, self.tar.memoria)):
						memoriaUsada += self.tar.memoria
						self.set_timers(x, self.tar.tiempoDuracion)
					else:
						self.listaMedia.append(self.tar)
						self.listaMedia.pop(self.listaMedia.index(self.tar))
				if self.tar.tiempoFinal==x:
					memoriaUsada -= self.tar.memoria

			for self.tar in self.listaBaja:
				if self.tar.tiempoLlegada==x:
					if(self.revisar_memoria(memoriaTotal, memoriaUsada, self.tar.memoria)):
						memoriaUsada += self.tar.memoria
						self.set_timers(x, self.tar.tiempoDuracion)
					else:
						self.listaBaja.append(self.tar)
						self.listaBaja.pop(self.listaBaja.index(self.tar))
				if self.tar.tiempoFinal==x:
					memoriaUsada -= self.tar.memoria
		return None

	def set_timers(self,tiempoInicial,tiempoDuracion):
		self.tar.tiempoInicial = tiempoInicial
		self.tar.tiempoFinal = self.tar.tiempoInicial+tiempoDuracion

	def revisar_memoria(self, memoriaTotal, memoriaUsada, memoriaTarea):
		if((memoriaTarea+memoriaUsada)<=memoriaTotal):
			return True
		else:
			return False

	def on_save(self, event):
		#Guardar una carta
		pass

	def confirmar(self, file):
		"""Mostrar mensaje de confirmación al guardar una carta"""
		confirmar = CONFIRMAR + file
		dialog = wx.MessageDialog(self, confirmar, CONFIRM_TITLE, wx.OK)
		dialog.ShowModal()
		dialog.Destroy()

	def on_about(self, event):
		"""Mostrar un diálogo acerca de"""
		dialog = wx.MessageDialog(self, ABOUT_CONTENT, ABOUT_TITLE, wx.OK)
		dialog.ShowModal()  # mostrar diálogo
		dialog.Destroy()  # finalizar diálogo

	def on_exit(self, event):
		"""Salir del programa"""
		self.Close(True)  # Cierra la ventana

class Resultado(wx.Frame):

	def __init__(self, parent, detalles, tiempo, numtareas):
		wx.Frame.__init__(self, parent, wx.NewId(), "Resultados - SimuladorSO",
							pos=(10,140), size=(650,400))
		self.Bind(wx.EVT_CLOSE, self.al_cerrar)

		#panel
		self.panel = wx.Panel(self)
		
		#textos estaticos
		self.cant = wx.StaticText(self.panel, -1, "Cantidad de tareas ejecutadas:"+tiempo,
								  pos=(10,10))
		self.time = wx.StaticText(self.panel, -1, "Tiempo total de ejecucion:"+numtareas, pos=(10,25))
		self.detalles = wx.StaticText(self.panel, -1, "Detalles de las tareas:",pos=(10,60))

		#linea estatica
		self.line = wx.StaticLine(self.panel, pos=(10, 50), size=(500,1))
				
		#caja de texto de los detalles
		self.cajatext = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE, pos=(10,80), size=(600,210))
		self.cajatext.SetValue(detalles)
		#botones
		bVolver = wx.Button(self.panel,label="Volver",pos=(430,300),size=(60,30))
		bImprimir = wx.Button(self.panel,label="Imprimir",pos=(500,300),size=(60,30))
		
		#bindeo de eventos.
		self.Bind(wx.EVT_BUTTON, self.al_cerrar,bVolver)
		self.Bind(wx.EVT_BUTTON, self.imprimir, bImprimir)

	def imprimir(self, evt):
		dialog = wx.MessageDialog(self, 'Imprimiendo pronto', 'Impresion', wx.OK)
		dialog.ShowModal()
		dialog.Destroy()

	def al_cerrar(self, evt):
		self.MakeModal(False)
		self.Show(False)
		evt.Skip()

app = wx.App(False)
frame = SisOpe(None, "SimuladorSO",id=-1)
frame.Centre()
app.MainLoop()
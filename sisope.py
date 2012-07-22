# -*- coding: utf-8 *-*
"""Simulador de tareas en un sistema operativo"""
#HACIENDO COMMITS AL MISMO TIEMPO
import datetime

import wx

from constants import *

class SisOpe(wx.Frame):

    def __init__(self, parent, title, id):
        wx.Frame.__init__(self, parent,id, title=title, size=(500, 400))
        panel = wx.Panel(self)
        
        #boton iniciar
        boton = wx.Button(panel,label="Iniciar",pos=(10,140),size=(60,30))
        self.Bind(wx.EVT_BUTTON, self.iniciarSimulacion,boton)

        #cajas de texto
        text1=wx.StaticText(panel,-1,"Número de tareas".decode('utf-8'),(10,30))
        text2=wx.StaticText(panel,-1,"Espacio de memoria",(10,52))
        text3=wx.StaticText(panel,-1,"Tiempo de ejecución".decode('utf-8'),(10,74))


        self.tama=wx.TextCtrl(panel,-1,'',(120,30),(120,-1))
        self.espacio=wx.TextCtrl(panel,-1,'',(120,50),(120,-1))
        self.tiempo=wx.TextCtrl(panel,-1,'',(120,70),(120,-1))

        # Inicializa un menú
        filemenu = wx.Menu()
        # Crea items del menú
        menu_save = filemenu.Append(wx.ID_SAVE, MENU_GUARDAR, STATUS_GUARDAR)
        menu_about = filemenu.Append(wx.ID_ABOUT, MENU_ABOUT, STATUS_ABOUT)
        menu_exit = filemenu.Append(wx.ID_EXIT, MENU_SALIR, STATUS_SALIR)

        # Crea la barra de menú
        menubar = wx.MenuBar()
        menubar.Append(filemenu, MENU_TITLE)  # Titulo del menu
        self.SetMenuBar(menubar)  # Agrega la barra de menu al frame

        # Establece eventos
        self.Bind(wx.EVT_MENU, self.on_save, menu_save)
        self.Bind(wx.EVT_MENU, self.on_about, menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, menu_exit)

        self.Centre(True)  # Centrar la ventana en pantalla
        self.Show(True)  # Mostrar la ventana

    def iniciarSimulacion(self, event):
        #Inicio de la simulación
        texto="hola"

    def on_save(self, event):
        """Guardar una carta"""
        #nada por ahora

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


app = wx.App(False)
frame = SisOpe(None, "Simulador de tareas",id=-1)
frame.Centre()
app.MainLoop()

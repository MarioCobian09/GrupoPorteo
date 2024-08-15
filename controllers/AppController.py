from views import gui as app
from views.menus import proveedores, serviciocliente, finanzas, recursoshumanos
from controllers import LoginController, LogisticaController, ProveedoresController, ServClientController, RHController, FinanzasController

from includes import globales as gl
import customtkinter as ctk
import os.path

class AppController:
    
    def __init__(self, usuario):
        self.root = ctk.CTk()
        ctk.set_appearance_mode("light")
        
        self.configVentana()
        
        self.model = usuario
        
        self.view = app.gui(self.root, self)
        self.view.menu_inicio()
        
        self.root.mainloop()
        
    def configVentana(self):
        self.root.title("Grupo Porteo")
        self.root.geometry(gl.centrarVentana(self.root, 1024, 600))
        self.root.iconbitmap(os.path.join(gl.RUTA_IMG, 'icono_gp.ico'))
    
    def logout(self):
        self.root.destroy()
        self.model.mantenerSesion(self.model.atributos['usu_id'], 0)
        C = LoginController.LoginController()
        
    # ------------ VISTAS DE MENU ---------------------------------------------
        
    def viewLogistica(self):
        self.view.eliminarFrames()
        LogisticaController.LogisticaController(self.view.contenedor)
    
    def viewProveedores(self):
        self.view.eliminarFrames()
        ProveedoresController.ProveedoresController(self.view.contenedor)
        
    def viewServicioCliente(self):
        self.view.eliminarFrames()
        ServClientController.ServClientController(self.view.contenedor)
        
    def viewFinanzas(self):
        self.view.eliminarFrames()
        FinanzasController.FinanzasController(self.view.contenedor)
        
    def viewRH(self):
        self.view.eliminarFrames()
        RHController.RHController(self.view.contenedor)

    

    
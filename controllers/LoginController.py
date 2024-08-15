from views import login
from models import usuariosModel
from includes import globales as gl
from controllers import AppController

import os.path
import customtkinter as ctk
from tkinter import messagebox


class LoginController:
    
    def __init__(self):
        self.root = ctk.CTk()
        self.model = usuariosModel.usuariosModel()
        
        self.configVentana()
        
        self.view = login.Login(self.root, self)
        
        self.sesionMantener()
        
        self.root.mainloop()
        
    def configVentana(self):
        self.root.title("Grupo Porteo - Login")
        self.root.geometry(gl.centrarVentana(self.root, 950, 550))
        self.root.iconbitmap(os.path.join(gl.RUTA_IMG, 'icono_gp.ico'))
        self.root.resizable(False, False)

    def login(self):
        correo = self.view.entry_correo.get()
        password = self.view.entry_password.get()
        manter_sesion = self.view.mantener_sesion.get()
        
        resultado = self.model.buscarPorCorreo(correo)
        
        if resultado:
            self.model.setDatos(resultado)
            
            if self.model.comprobarPassword(password):
                if manter_sesion == 1:
                    self.model.mantenerSesion(self.model.atributos['usu_id'], 1)
                self.iniciarSesion(self.model)
            else:
                messagebox.showerror(title='Ha ocurrido un error', message="La contraseña es incorrecta.")
        else:
            messagebox.showerror(title='Ha ocurrido un error', message="El correo ingresado no coincide con ningún usuario.")
            
    def iniciarSesion(self, usuario):
        self.root.destroy()
        C = AppController.AppController(usuario)
        
    def sesionMantener(self):
        resultado = self.model.buscarPorSesion()
        if resultado:
            self.model.setDatos(resultado)
            self.iniciarSesion(self.model)
            return
        else:
            return

        
        
        
        
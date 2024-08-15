from tkinter import *
from tkinter import ttk
import customtkinter as ctk

from PIL import ImageTk, Image
import os.path

from includes import globales as gl


class Login:
    def __init__(self, master, controller):
        
        self.root = master
        self.controller = controller
        
        ctk.set_appearance_mode("light")
        
        frame_logo = Frame(self.root, bg="white", width=gl.W_LOGIN/2, height=gl.H_LOGIN)
        frame_logo.pack(side="left")
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(300, 300))
        ctk.CTkLabel(frame_logo, image=img_logo, text='').place(rely=0.2, relx=0.18)
        
        form = Frame(self.root, bg="#1269CD", width=gl.W_LOGIN/2, height=gl.H_LOGIN)
        form.pack(side="right")
        
        Label(form, text="bienvenido!", font=gl.FONT_LOGIN_H1, fg="white", bg="#1269CD").place(x=158, y=100)
        Label(form, text="Si tiene una cuenta, inicie sesión.", font=gl.FONT_LOGIN_H2, fg="white", bg="#1269CD").place(x=110,y=140)
        
        Label(form, text="Email:", font=gl.FONT_LOGIN_H2, fg="white", bg="#1269CD").place(x=90,y=200)
        self.entry_correo = ctk.CTkEntry(form, 
                                       font=gl.FONT_LOGIN_H2, 
                                       fg_color="white", 
                                       width=300, 
                                       height=40, 
                                       border_width=0, 
                                       placeholder_text="Escribe tu Correo...",
                                       )
        self.entry_correo.place(x=93, y=235)
        
        Label(form, text="Password:", font=gl.FONT_LOGIN_H2, fg="white", bg="#1269CD").place(x=90,y=280)
        
        self.entry_password = ctk.CTkEntry(form, 
                                       font=gl.FONT_LOGIN_H2, 
                                       fg_color="white", 
                                       width=300, 
                                       height=40, 
                                       border_width=0, 
                                       placeholder_text="Escribe tu Contraseña...",
                                       )
        self.entry_password.configure(show='*')
        self.entry_password.place(x=93, y=315)
        
        icono_show = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'icono_show.png'))), size=((25,25)))
        ver_contraseña = ctk.CTkButton(form, image=icono_show, text='', width=25, height=25, command=self.mostrarPassword, fg_color=gl.COLOR_AZUL_PRIMARIO, hover_color=gl.COLOR_AZUL_PRIMARIO)
        ver_contraseña.place(x=400, y=320)
        
        valorBoleano = BooleanVar(self.root)
        self.mantener_sesion = ctk.CTkCheckBox(form, 
                                          text="Mantener la sesion iniciada", 
                                          variable=valorBoleano,
                                          checkbox_width=18,
                                          checkbox_height=18,
                                          text_color='white',
                                          checkmark_color='black',
                                          fg_color='white',
                                          border_width=1,
                                          border_color='white',
                                         )
        self.mantener_sesion.place(x=93, y=370)
        
        form_button = ctk.CTkButton(form, 
                                    text="Login", 
                                    border_width=0, 
                                    text_color="white", 
                                    font=("Poppins Medium", 18), 
                                    width=300, 
                                    height=50,
                                    fg_color="#7B96D4",
                                    command=self.controller.login
                                    )
        form_button.place(x=93, y=420)
        
    def mostrarPassword(self):
        if self.entry_password.cget('show'):
            self.entry_password.configure(show='')
        else:
            self.entry_password.configure(show='*')
    

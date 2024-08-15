import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class gui:
    def __init__(self, master, controller):
        self.root = master
        self.controller = controller
        
        self.paneles()
        
        self.widgetsMenu()
        
    def paneles(self):
        self.menu = tk.Frame(self.root, bg=gl.COLOR_AZUL_PRIMARIO, width=260)
        self.menu.pack(side=tk.LEFT, fill='both', expand=False)
        
        self.contenedor = tk.Frame(self.root, bg='white')
        self.contenedor.pack(fill='both', expand=True)
        
    def widgetsMenu(self):
        usuario_menu = tk.Frame(self.menu, bg=gl.COLOR_AZUL_PRIMARIO, width=210, height=50)
        usuario_menu.pack(side=tk.TOP, pady=40, padx=25, fill='x')
        
        if os.path.exists(os.path.join(gl.RUTA_IMG_USUARIOS, self.controller.model.getImg())):
            usu_img = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG_USUARIOS, self.controller.model.getImg()))), size=(50, 50))
        else:
            usu_img = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'usuario_icono.png'))), size=(50, 50))
        ctk.CTkLabel(usuario_menu, image=usu_img, text='').place(x=10, y=0)
        tk.Label(usuario_menu, text=self.controller.model.getNombre(), font=("Helvetica", 13, 'bold'), fg='white', bg=gl.COLOR_AZUL_PRIMARIO).place(x=65, y=6)
        tk.Label(usuario_menu, text=self.controller.model.getPuesto(), font=("Helvetica", 10), fg='white', bg=gl.COLOR_AZUL_PRIMARIO).place(x=65, y=24)
        
        botones_menu = tk.Frame(self.menu, bg=gl.COLOR_AZUL_PRIMARIO, width=230)
        botones_menu.pack(side=tk.TOP, padx=15, fill='x')
        
        self.boton_logistica = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.iluminarBoton(self.boton_logistica, self.controller.viewLogistica))
        self.boton_proveedores = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.iluminarBoton(self.boton_proveedores, self.controller.viewProveedores))
        self.boton_serviciocliente = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.iluminarBoton(self.boton_serviciocliente, self.controller.viewServicioCliente))
        self.boton_finanzas = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.iluminarBoton(self.boton_finanzas, self.controller.viewFinanzas))
        self.boton_rh = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.iluminarBoton(self.boton_rh, self.controller.viewRH))
        
        if self.controller.model.getPuesto() == 'Admin':
            botones = [
                ('Logística', "icono_logistica.png", self.boton_logistica),
                ('Proveedores', "icono_prov.png", self.boton_proveedores),
                ('Servicio al Cliente', "icono_servicioclient.png", self.boton_serviciocliente),
                ('Finanzas', "icono_finanzas.png", self.boton_finanzas),
                ('Recursos Humanos', "icono_rh.png", self.boton_rh),
            ]
        elif self.controller.model.getPuesto() == 'Logistica':
            botones = [
                ('Logística', "icono_logistica.png", self.boton_logistica)
            ]
        elif self.controller.model.getPuesto() == 'Proveedores':
            botones = [
                ('Proveedores', "icono_prov.png", self.boton_proveedores)
            ]
        elif self.controller.model.getPuesto() == 'ServicioCliente':
            botones = [
                ('Servicio al Cliente', "icono_servicioclient.png", self.boton_serviciocliente)
            ]
        elif self.controller.model.getPuesto() == 'Finanzas':
            botones = [
                ('Finanzas', "icono_finanzas.png", self.boton_finanzas)
            ]
        elif self.controller.model.getPuesto() == 'RH':
            botones = [
                ('Recursos Humanos', "icono_rh.png", self.boton_rh)
            ]
        
        for text, icon, button in botones:
            button.configure(text=f" {text}", 
                            image=ctk.CTkImage(Image.open(os.path.join(gl.RUTA_IMG, icon)), size=(30,30)),
                            font=("Helvetica",15),
                            fg_color=gl.COLOR_AZUL_PRIMARIO,
                            hover_color=gl.COLOR_ROJO_PRIMARIO,
                            anchor="w",
                            corner_radius=20,
                            )
            button.pack(side=tk.TOP, pady=1)
            
        
        self.boton_config = ctk.CTkButton(botones_menu, width=230, height=50)
        self.boton_config.configure(text=" Configuración", 
                                    image=ctk.CTkImage(Image.open(os.path.join(gl.RUTA_IMG, 'icono_config.png')), size=(30,30)),
                                    font=("Helvetica",15),
                                    fg_color=gl.COLOR_AZUL_PRIMARIO,
                                    hover_color=gl.COLOR_ROJO_PRIMARIO,
                                    anchor="w",
                                    corner_radius=20
                                    )
        self.boton_config.pack(side=tk.TOP, pady=30)
        self.boton_logout = ctk.CTkButton(botones_menu, width=230, height=50, command=lambda: self.controller.logout())
        self.boton_logout.configure(text=" Logout", 
                                    image=ctk.CTkImage(Image.open(os.path.join(gl.RUTA_IMG, 'icono_logout.png')), size=(30,30)),
                                    font=("Helvetica",15),
                                    fg_color=gl.COLOR_AZUL_PRIMARIO,
                                    hover_color=gl.COLOR_ROJO_PRIMARIO,
                                    anchor="w",
                                    corner_radius=20
                                    )
        self.boton_logout.pack(side=tk.TOP, pady=10)
        
    def iluminarBoton(self, button, funcion):
        self.desiluminarBoton()
        button.configure(fg_color=gl.COLOR_ROJO_PRIMARIO)
        funcion()
        
    def desiluminarBoton(self):
        self.boton_logistica.configure(fg_color=gl.COLOR_AZUL_PRIMARIO)
        self.boton_proveedores.configure(fg_color=gl.COLOR_AZUL_PRIMARIO)
        self.boton_serviciocliente.configure(fg_color=gl.COLOR_AZUL_PRIMARIO)
        self.boton_finanzas.configure(fg_color=gl.COLOR_AZUL_PRIMARIO)
        self.boton_rh.configure(fg_color=gl.COLOR_AZUL_PRIMARIO)
        
    def eliminarFrames(self):
        for frame in self.contenedor.winfo_children():
            frame.destroy()
        
    def menu_inicio(self):
        self.eliminarFrames()
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(300, 300))
        imagen = ctk.CTkLabel(self.contenedor, image=img_logo, fg_color='white', text='')
        imagen.place(x=0, y=0, relwidth=1, relheight=1)
        
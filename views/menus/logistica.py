import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewLogistica:
    
    def __init__(self, contenedor, controller):
        self.root = contenedor
        self.controller = controller
        
        self.menu_logistica()
    
    def menu_logistica(self):
        self.logistica = tk.Frame(self.root, bg='white')
        self.logistica.pack(fill='both', expand=True)
        
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(80, 80))
        imagen = ctk.CTkLabel(self.logistica, image=img_logo, fg_color='white', text='', bg_color='white')
        imagen.pack(side="right", anchor='n', padx=20, pady=1)
    
        tk.Label(self.logistica,text="Logística", font=gl.FONT_APP_H1, bg='white').place(relx=0.04, rely=0.05)
        self.submenu = tk.Frame(self.logistica, bg='white')
        self.submenu.place(relwidth=0.92, relheight=1, y=100, relx=0.5, anchor='center', rely=0.5)
        
        self.widgetsMenu()
        
    def widgetsMenu(self):
        
        contenedorBotones = tk.Frame(self.submenu, bg='white')
        contenedorBotones.place(relx=0.5, rely=0.4, anchor='center')
        
        btn_gestiontrans = ctk.CTkButton(contenedorBotones, command=self.controller.viewGestionTransportes)
        btn_gestionalma = ctk.CTkButton(contenedorBotones, command=self.controller.viewGestionAlmacenes)
        btn_gestionpedidos = ctk.CTkButton(contenedorBotones, command=self.controller.viewGestionPedidos)
        btn_analisisreportes = ctk.CTkButton(contenedorBotones, command=self.controller.viewAnalisisReportes)
        
        btn_menus = [
            ('Gestión de Transporte', 'icono_gestiontrans.png', gl.COLOR_AZUL_1, btn_gestiontrans),
            ('Gestión de Almacenes', 'icono_gestionalma.png', gl.COLOR_AZUL_2, btn_gestionalma),
            ('Gestión de Pedidos', 'icono_gestionped.png', gl.COLOR_ROJO_1, btn_gestionpedidos),
            ('Analisis y Reportes', 'icono_analisisreportes.png', gl.COLOR_ROJO_2, btn_analisisreportes)
        ]
        
        contadorx = 0
        contadory = 0
        
        for nombre, icono, color, boton in btn_menus:
            
            boton.configure(text_color='white',
                            fg_color=color,
                            image=ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, icono))), size=(80,80)),
                            font=('Helvetica', 20, "bold"),
                            corner_radius=0,
                            cursor='hand2',
                            compound='top',
                            text=nombre,
                            width=self.submenu.winfo_screenwidth()/6,
                            height=self.submenu.winfo_screenheight()/6,
                            )
            boton.grid(row=contadorx, column=contadory, padx=30, pady=30)
            
            if contadorx == 0:
                boton.configure(hover_color='#003D84')
            if contadorx == 1:
                boton.configure(hover_color='#7C0A02')
            
            contadorx = 1 if contadory == 1 or contadorx == 1 else 0
            contadory = 1 if contadorx == 0 or contadory != 1  else 0

        
    def eliminarFramesSubmenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        
    def regresarAlMenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        self.widgetsMenu()
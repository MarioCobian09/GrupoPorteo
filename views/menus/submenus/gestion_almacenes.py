import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl


class viewGA:
    
    def __init__(self, submenu, controller):
        self.submenu = submenu
        self.controller = controller
        
        self.initView()
        self.configTablaGA()
        
    def initView(self):
        self.contenedorGA = tk.Frame(self.submenu, bg='white')
        self.contenedorGA.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedorGA, text="Gestión de Almacenes", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorGA)
        contenedorBackFor.pack(side='right', anchor='n')
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.controller.view.regresarAlMenu
                                )
        btnBack.pack(side=tk.LEFT)
        btnFor = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'siguiente.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF'
                                )
        btnFor.pack(side=tk.RIGHT)
    
    def configTablaGA(self):
        contenedorTabla = tk.Frame(self.contenedorGA, bg='white')
        contenedorTabla.place(rely=0.1, relheight=0.7, relwidth=1)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedorTabla, columns=('Nombre', 'Ciudad', 'Estado', 'Pais', 'Capacidad Total', 'Capacidad Actual', 'Costo'), show='headings', height=4)
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.heading('#0', text='\n\n')
        tabla.column('Nombre', width=100, anchor='w')
        tabla.column('Ciudad', width=60, anchor='w')
        tabla.column('Estado', width=60, anchor='w')
        tabla.column('Pais', width=20, anchor='w')
        tabla.column('Capacidad Total', width=40, anchor='w')
        tabla.column('Capacidad Actual', width=40, anchor='w')
        tabla.column('Costo', width=20, anchor='w')
        
        tabla.heading('Nombre', text='Nombre', anchor='w')
        tabla.heading('Ciudad', text='Ciudad', anchor='w')
        tabla.heading('Estado', text='Estado', anchor='w')
        tabla.heading('Pais', text='Pais', anchor='w')
        tabla.heading('Capacidad Total', text='Capacidad\nTotal', anchor='w')
        tabla.heading('Capacidad Actual', text='Capacidad\nActual', anchor='w')
        tabla.heading('Costo', text='Costo', anchor='w')
        
        Almacenes = self.controller.almacenesModel.allAlmacenes()
        
        for a in Almacenes:
            tabla.insert('', tk.END, text='', 
                         values=(a.atributos['alm_nombre'], 
                                 a.atributos['alm_ciudad'], 
                                 a.atributos['alm_estado'], 
                                 a.atributos['alm_pais'],
                                 a.atributos['alm_capacidad_total'],
                                 a.atributos['alm_capacidad_actual'],
                                 a.atributos['alm_costo']
                        ))
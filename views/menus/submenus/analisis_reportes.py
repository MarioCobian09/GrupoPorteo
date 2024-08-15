import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl


class viewAR:
    
    def __init__(self, submenu, controller):
        self.submenu = submenu
        self.controller = controller
        
        self.initView()
        self.configTablaAR()
        
    def initView(self):
        self.contenedorAR = tk.Frame(self.submenu, bg='white')
        self.contenedorAR.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedorAR, text="Análisis y Reportes", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorAR)
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
    
    def configTablaAR(self):
        contenedorTabla = tk.Frame(self.contenedorAR, bg='white')
        contenedorTabla.place(rely=0.1, relheight=0.7, relwidth=1)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedorTabla, columns=('Asunto', 'Estado', 'Cliente', 'Destino'), show='headings', height=4)
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column('Asunto', width=50, anchor='w')
        tabla.column('Estado', width=10, anchor='w')
        tabla.column('Cliente', width=30, anchor='w')
        tabla.column('Destino', width=150, anchor='w')
        
        tabla.heading('Asunto', text='Asunto', anchor='w')
        tabla.heading('Estado', text='Estado', anchor='w')
        tabla.heading('Cliente', text='Cliente', anchor='w')
        tabla.heading('Destino', text='Destino', anchor='w')
        
        Reportes = self.controller.reportesModel.allReportes()
        
        for a in Reportes:
            pedido = self.controller.pedidosModel.findPedidoPorId(a.atributos['rep_ped_id'])
            tabla.insert('', tk.END, text='', 
                         values=(a.atributos['rep_asunto'], 
                                 a.atributos['rep_estado'], 
                                 pedido.atributos['ped_cliente'], 
                                 pedido.atributos['ped_destino'],
                        ))
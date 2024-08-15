import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewServicioCliente:
    
    def __init__(self, contenedor, controller):
        self.root = contenedor
        
        self.controller = controller
        
        self.menu_serviciocliente()
        
    
    def menu_serviciocliente(self):
        self.serviciocliente = tk.Frame(self.root, bg='white')
        self.serviciocliente.pack(fill='both', expand=True)
        
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(100, 100))
        imagen = ctk.CTkLabel(self.serviciocliente, image=img_logo, fg_color='white', text='')
        imagen.pack(side="right", anchor='n', padx=20, pady=1)
        
        tk.Label(self.serviciocliente, text="Servicio al Cliente", font=gl.FONT_APP_H1, bg='white').place(relx=0.04, rely=0.05)

        self.submenu = tk.Frame(self.serviciocliente, bg='white')
        self.submenu.place(relwidth=0.92, relheight=1, y=100, relx=0.5, anchor='center', rely=0.5)
        
        self.configView()
        
    def configView(self):
        contenedorBotones = tk.Frame(self.submenu, bg='white')
        contenedorBotones.place(relheight=0.8, relwidth=0.4,)
        
        self.registrarPedidos = ctk.CTkButton(contenedorBotones, 
                                                text='Quejas y Solicitudes', 
                                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                                text_color='white', 
                                                hover_color='#003D84', 
                                                corner_radius=0, 
                                                font=('Helvetica', 18, "bold"),
                                                command=self.controller.viewQuejasySugerencias
                                            )
        self.registrarPedidos.place(rely=0.1, relwidth=1, relheight=0.35)
        
        self.registrarPedidos = ctk.CTkButton(contenedorBotones, 
                                                text='Analizar Reseñas', 
                                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                                text_color='white', 
                                                hover_color='#003D84', 
                                                corner_radius=0, 
                                                font=('Helvetica', 18, "bold"),
                                                command=self.controller.viewAnalizarReseñas
                                            )
        self.registrarPedidos.place(rely=0.55, relwidth=1, relheight=0.35)
        
        contenedorReseñas = ctk.CTkFrame(self.submenu, fg_color=gl.COLOR_ROJO_OSCURO,
                                                        border_color=gl.COLOR_ROJO_OSCURO,
                                                        corner_radius=10
                                        )
        contenedorReseñas.place(relx=0.5, relwidth=0.49, relheight=0.8)
        
        tk.Label(contenedorReseñas, text='Reseñas', font=("Poppins Medium", 15), bg=gl.COLOR_ROJO_OSCURO, fg='white').pack(side='left', anchor='n',padx=25, pady=25)
        
        contenedor = tk.Frame(contenedorReseñas, bg='green')
        contenedor.place(anchor='center', rely=0.52, relx=0.5, relwidth=0.83, relheight=0.8)
        
        reseñas = self.controller.reseñasModel.someReseñas(4)
        
        posiciony = 0
        for r in reseñas:
            reseña = tk.Frame(contenedor, bg=gl.COLOR_ROJO_OSCURO)
            reseña.place(relwidth=1, relheight=0.25, rely=posiciony)

            usuarioIcono = ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'usuario_icono.png')), size=(35,35))
            ctk.CTkLabel(reseña, image=usuarioIcono, text='').place(relheight=0.5, y=10)
            
            tk.Label(reseña, text=r.atributos['res_cliente'], bg=gl.COLOR_ROJO_OSCURO, fg='white', font=("Poppins Medium", 12)).place(relheight=0.4, x=50, y=15)
            tk.Label(reseña, text=r.atributos['res_fecha'], bg=gl.COLOR_ROJO_OSCURO, fg='white', font=("Poppins Medium", 7)).place(relx=0.8, y=15)
            tk.Label(reseña, text=r.atributos['res_comentario'], 
                            bg=gl.COLOR_ROJO_OSCURO, 
                            fg='white', 
                            font=("Poppins Medium", 8), 
                            anchor='nw'
                    ).place(rely=0.6, relwidth=1, relheight=0.6)
            
            tk.Frame(reseña, height=1).pack(anchor='center', side='bottom', fill='x')
            posiciony += 0.25
            
    def viewReseñas(self):
        self.contenedor = tk.Frame(self.submenu, bg='white')
        self.contenedor.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedor, text="Todas las Reseñas", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedor)
        contenedorBackFor.pack(side='right', anchor='n')
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.regresarAlMenu
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
        
        contenedorTabla = tk.Frame(self.contenedor, bg='white')
        contenedorTabla.place(rely=0.1, relheight=0.7, relwidth=1)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedorTabla, columns=('Cliente', 'Comentario', 'Fecha'), show='headings', height=4)
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column('Cliente', width=200, anchor='w', minwidth=150)
        tabla.column('Comentario', width=350, anchor='w')
        tabla.column('Cliente', width=10, anchor='w')
        
        tabla.heading('Cliente', text='Cliente', anchor='w')
        tabla.heading('Comentario', text='Comentario', anchor='w')
        tabla.heading('Fecha', text='Fecha', anchor='w')
        
        allReseñas = self.controller.reseñasModel.allReseñas()
        
        for a in allReseñas:
            tabla.insert('', tk.END, text='', 
                         values=(a.atributos['res_cliente'], 
                                 a.atributos['res_comentario'], 
                                 a.atributos['res_fecha']
                        ))
            
    def viewQuejas(self):
        self.contenedor = tk.Frame(self.submenu, bg='white')
        self.contenedor.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedor, text="Quejas y Solicitudes", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedor)
        contenedorBackFor.pack(side='right', anchor='n')
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.regresarAlMenu
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
        
        contenedorTabla = tk.Frame(self.contenedor, bg='white')
        contenedorTabla.place(rely=0.1, relheight=0.7, relwidth=1)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedorTabla, columns=('Cliente', 'Asunto', 'Mensaje', 'Fecha'), show='headings', height=4)
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column('Cliente', width=80, anchor='w', minwidth=80)
        tabla.column('Asunto', width=100, anchor='w', minwidth=100)
        tabla.column('Mensaje', width=300, anchor='w', minwidth=200)
        tabla.column('Fecha', width=10, anchor='w')
        
        tabla.heading('Cliente', text='Cliente', anchor='w')
        tabla.heading('Asunto', text='Asunto', anchor='w')
        tabla.heading('Mensaje', text='Mensaje', anchor='w')
        tabla.heading('Fecha', text='Fecha', anchor='w')
        
        allQuejas = self.controller.quejasysugerenciasModel.allQuejas()
        
        for a in allQuejas:
            tabla.insert('', tk.END, text='', 
                         values=(a.atributos['que_cliente'], 
                                 a.atributos['que_asunto'], 
                                 a.atributos['que_mensaje'],
                                 a.atributos['que_fecha'],
                        ))
            
    def eliminarFramesSubmenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        
    def regresarAlMenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        self.configView()
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewFinanzas:
    
    def __init__(self, contenedor, controller):
        self.root = contenedor
        
        self.controller = controller
        
        self.menu_finanzas()
        self.configView()
        
    def menu_finanzas(self):
        self.finanzas = tk.Frame(self.root, bg='white')
        self.finanzas.pack(fill='both', expand=True)
        
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(100, 100))
        imagen = ctk.CTkLabel(self.finanzas, image=img_logo, fg_color='white', text='')
        imagen.pack(side="right", anchor='n', padx=20, pady=1)
        
        tk.Label(self.finanzas, text="Finanzas", font=gl.FONT_APP_H1).place(relx=0.04, rely=0.05)
        
        self.submenu = tk.Frame(self.finanzas, bg='white')
        self.submenu.place(relwidth=0.92, relheight=1, y=100, relx=0.5, anchor='center', rely=0.5)
        
    def configView(self):
        self.configTabla()
        self.configGrafica()
        self.configInfo()
    
    def configTabla(self):
        contenedorTabla = tk.Frame(self.submenu, bg='white')
        contenedorTabla.place(relwidth=0.6, relheight=0.55)
        
        tk.Label(contenedorTabla, text="Todos los Productos", font=('Helvetica', 10, "bold"), bg='white').place(x=0, y=0, relheight=0.1)
        
        contenedor = tk.Frame(contenedorTabla, bg='purple')
        contenedor.place(rely=0.1, relwidth=0.95, relheight=0.8)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedor, columns=('Nombre', 'Costo', 'Peso', 'Cantidad'), show='headings')
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(tabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column("Nombre", width=100, anchor='w')
        tabla.column('Costo', width=20, anchor='w')
        tabla.column("Peso", width=10, anchor='w')
        tabla.column("Cantidad", width=20, anchor='w')
        
        tabla.heading('Nombre', text='Nombre', anchor='w')
        tabla.heading('Costo', text='Costo', anchor='w')
        tabla.heading('Peso', text='Peso', anchor='w')
        tabla.heading('Cantidad', text='Cant.', anchor='w')
        
        productos = self.controller.productosModel.allProductos()
        
        for p in productos:
            nombre = p.atributos['prod_nombre']
            costo = f"${p.atributos['prod_costo']}.00 MXN"
            peso = f"{p.atributos['prod_peso']} kg"
            cantidad = f"{p.atributos['prod_cantidad']} unidades"
            tabla.insert('', tk.END, text='', 
                         values=(nombre, costo, peso, cantidad))
        
    def configGrafica(self):
        contenedorGrafico = tk.Frame(self.submenu, bg='white')
        contenedorGrafico.place(relwidth=0.4, relheight=0.55, relx=0.6)
        
        tk.Label(contenedorGrafico, text="Productos que generan mayor ganancia", font=('Helvetica', 10, "bold"), bg='white').place(x=0, y=0, relheight=0.1)
        
        contenedor = tk.Frame(contenedorGrafico, bg='purple')
        contenedor.place(relx=0.025, rely=0.1, relwidth=0.9, relheight=0.8)
        
        productos = self.controller.productosModel.allProductosMasVendidos()
        nombreProductos = list()
        self.costoProductos = list()
        colores = ['blue', 'red', 'green', 'magenta']
        for p in productos:
            nombreProductos.append(p.atributos['prod_nombre'])
            self.costoProductos.append(p.atributos['prod_costo'])
        
        fig, axs = plt.subplots(figsize=(10, 20), sharey=True, dpi=60)
        plt.xticks(rotation=15)
        
        axs.bar(nombreProductos, self.costoProductos, color=colores)
        
        canvas = FigureCanvasTkAgg(fig, master=contenedor)
        canvas.draw()
        canvas.get_tk_widget().place(relwidth=1, relheight=1)
        
        plt.close()
        
    def configInfo(self):
        contenedorInfo = tk.Frame(self.submenu, bg='white')
        contenedorInfo.place(relwidth=1, relheight=0.25, rely=0.55)
        
        contenedorInfo.grid_columnconfigure(0, weight=1)
        contenedorInfo.grid_columnconfigure(1, weight=1)
        contenedorInfo.grid_columnconfigure(2, weight=1)
        contenedorInfo.grid_rowconfigure(0, weight=1)
        
        facturaciones = ctk.CTkButton(contenedorInfo, 
                                            text='Facturacion y Pagos', 
                                            fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                            text_color='white', 
                                            hover_color='#003D84', 
                                            corner_radius=0, 
                                            font=('Helvetica', 18, "bold"),
                                            )
        facturaciones.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=20)
        facturaciones.propagate(0)
        
        gestionrecursos = ctk.CTkButton(contenedorInfo, 
                                            text='Gestion de recursos', 
                                            fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                            text_color='white', 
                                            hover_color='#003D84', 
                                            corner_radius=0, 
                                            font=('Helvetica', 18, "bold"),
                                            )
        gestionrecursos.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=20)
        gestionrecursos.propagate(0)
        
        ventas = tk.Frame(contenedorInfo, bg=gl.COLOR_ROJO_OSCURO)
        ventas.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=20)
        contenedor = tk.Frame(ventas, bg=gl.COLOR_ROJO_OSCURO)
        contenedor.pack(anchor='center', side='right')
        tk.Label(contenedor, text='El producto con mas ventas\ndio la ganancia de', font=('Helvetica', 10), fg='white', bg=gl.COLOR_ROJO_OSCURO, justify='right').pack(side='top', anchor='e')
        tk.Label(contenedor, text=f'${self.costoProductos[0]}', font=('Helvetica', 28, "bold"), fg='white', bg=gl.COLOR_ROJO_OSCURO).pack(side='top', anchor='e')
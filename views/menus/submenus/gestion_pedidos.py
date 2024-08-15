import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os.path
import string
import random

from includes import globales as gl

class viewGP:
    
    def __init__(self, submenu, controller):
        self.submenu = submenu
        self.controller = controller
        
        self.initView()
        
        self.configPedidos()
        self.configBotonesEspeciales()
        
    def initView(self):
        self.contenedorGP = tk.Frame(self.submenu, bg='white')
        self.contenedorGP.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedorGP, text="Gestión de pedidos", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorGP)
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
        
    def configBotonesEspeciales(self):
        # ------------------- BOTONES --------------------------------------
        
        contenedorBotones = tk.Frame(self.contenedorGP, bg='white')
        contenedorBotones.place(relheight=0.8, relwidth=0.3, y=40, relx=0.65)
        
        self.registrarPedidos = ctk.CTkButton(contenedorBotones, 
                                                text='Nuevo Pedido', 
                                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                                text_color='white', 
                                                hover_color='#003D84', 
                                                corner_radius=0, 
                                                font=('Helvetica', 18, "bold"),
                                                command=self.controller.viewNewPedido
                                            )
        self.registrarPedidos.place(rely=0.1, relwidth=1, relheight=0.2)
        
        self.registrarPedidos = ctk.CTkButton(contenedorBotones, 
                                                text='Marcar un pedido\ncomo entregado', 
                                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                                text_color='white', 
                                                hover_color='#003D84', 
                                                corner_radius=0, 
                                                font=('Helvetica', 18, "bold"),
                                                command=self.controller.viewTablaEntregar
                                            )
        self.registrarPedidos.place(rely=0.4, relwidth=1, relheight=0.2)
        
        
    def configPedidos(self):
        contenedorPedidos = tk.Frame(self.contenedorGP, bg='white')
        contenedorPedidos.place(relwidth=0.6, relheight=1, y=40)

        # ----------------------------- BUSQUEDA -----------------------------------
        
        contenedorBusqueda = tk.Frame(contenedorPedidos, bg='white')
        contenedorBusqueda.place(relwidth=1, height=52)
        
        btnBuscar = ctk.CTkButton(contenedorBusqueda, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'busqueda.png')), size=(40,40)),
                                            bg_color='white',
                                            fg_color='white',
                                            cursor='hand2',
                                            text='',
                                            width=0,
                                            height=0,
                                            hover_color='#EFEFEF'
                                )
        btnBuscar.pack(side=tk.LEFT, anchor='n')
        
        self.entry_buscar = ctk.CTkEntry(contenedorBusqueda, placeholder_text='Explorar pedidos por numero de guia...',
                                                            corner_radius=10,
                                                            border_color='#BDBDBD',
                                                            height=45,
                                                            fg_color='white'
                                        )
        self.entry_buscar.place(x=50, rely=0.05, relwidth=0.6)
        
        contenedorMostrar = tk.Frame(contenedorBusqueda, bg='white')
        contenedorMostrar.place(relx=0.73)
        
        tk.Label(contenedorMostrar, text='Mostrar:', font=gl.FONT_APP_P, background='white').pack(side='top', anchor='w')
        self.estado = ctk.CTkComboBox(contenedorMostrar, 
                                        values=['Todos', 'Entregados', 'Por Entregar'],
                                        width=110,
                                        border_color='#BDBDBD',
                                        button_color=gl.COLOR_AZUL_PRIMARIO,
                                        command=self.filtroBusquedaEstado
                                    )
        self.estado.pack(side=tk.BOTTOM, anchor='w')
        
        # ------------------------------ RESULTADOS ----------------------------------------------
        
        self.contenedorResultados = ctk.CTkScrollableFrame(contenedorPedidos, fg_color='#CFCFCF', corner_radius=0)
        self.contenedorResultados.place(relwidth=1, relheight=0.7, y=60)
        
        allPedidos = self.controller.pedidosModel.allPedidoswithAlamacen()
        self.printPedidos(allPedidos)
        
    def viewTabla(self):
        self.contenedor = tk.Frame(self.submenu, bg='white')
        self.contenedor.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedor, text="Pedidos sin entregar", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
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
                                                    command=self.controller.viewGestionPedidos
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
        
        self.tabla = ttk.Treeview(contenedorTabla, columns=('Guia', 'Destino', 'Producto', 'Cliente'), show='headings', height=4)
        self.tabla.place(relwidth=1, relheight=1)
        
        self.tabla.bind("<<TreeviewSelect>>", self.itemSeleccionado)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=self.tabla.yview)
        self.tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        self.tabla.column('Guia', width=50, anchor='w', minwidth=50)
        self.tabla.column('Destino', width=120, anchor='w', minwidth=120)
        self.tabla.column('Producto', width=80, anchor='w', minwidth=80)
        self.tabla.column('Cliente', width=80, anchor='w', minwidth=80)
        
        self.tabla.heading('Guia', text='Guia', anchor='w')
        self.tabla.heading('Destino', text='Destino', anchor='w')
        self.tabla.heading('Producto', text='Producto', anchor='w')
        self.tabla.heading('Cliente', text='Cliente', anchor='w')
        
        allPedidosSinEntregar = self.controller.pedidosModel.allPedidoswithAlamacenEntregados(0)
        
        for ent in allPedidosSinEntregar:
            if ent[3]:
                producto = self.controller.productosModel.findProductoPorId(ent[2])
                self.tabla.insert('', tk.END, text='', 
                            values=(ent[9], 
                                    ent[1], 
                                    producto.atributos['prod_nombre'],
                                    ent[5]
                                    ),
                            tags=ent[0]
                            )
            
    def itemSeleccionado(self, event):
        item = self.tabla.focus()
        
        data = self.tabla.item(item)
        id = data['tags'][0]
        
        self.controller.marcarPedidoEntregado(id)
        
        messagebox.showinfo('Pedido Entregado', 'El pedido seleccionado se marco como entregado')
        
        self.controller.viewGestionPedidos()
        
        
    
    def printPedidos(self, allPedidos):
        for ped in allPedidos:
            widgetPedido(ped, self.contenedorResultados, self.controller)

        pedido = ctk.CTkFrame(self.contenedorResultados,
                                        border_color='white',
                                        border_width=3,
                                        corner_radius=50,
                                        fg_color='white',
                                        width=400,
                                        height=180
                                        )
        pedido.pack(side=tk.TOP, anchor='center', pady=5, padx=10)
        pedido.pack_propagate(0)
        
    def filtroBusquedaEstado(self, choice=None):
        for widget in self.contenedorResultados.winfo_children():
            widget.destroy()
            
        if choice == 'Entregados':
            allPedidos = self.controller.pedidosModel.allPedidoswithAlamacenEntregados(1)
            self.printPedidos(allPedidos)
            
        if choice == 'Por Entregar':
            allPedidos = self.controller.pedidosModel.allPedidoswithAlamacenEntregados(0)
            self.printPedidos(allPedidos)
            
        if choice == 'Todos':
            allPedidos = self.controller.pedidosModel.allPedidoswithAlamacen()
            self.printPedidos(allPedidos)
            
        
class widgetPedido:
    
    def __init__(self, ped, contenedorResultados, controller):
        self.idpedido = ped[0]
        
        pedido = ctk.CTkFrame(contenedorResultados,
                                        border_color=gl.COLOR_AZUL_PRIMARIO,
                                        border_width=3,
                                        corner_radius=50,
                                        fg_color='white',
                                        width=400,
                                        height=180
                                        )
        pedido.pack(side=tk.TOP, anchor='center', pady=5, padx=10)
        pedido.pack_propagate(0)
        
        tk.Label(pedido, text='Numero de guía del pedido:', font=('Helvetica', 9), fg='#727171', bg='white').place(x=40, y=15)
        
        numguiaLabel = tk.Label(pedido, text=ped[9], font=('Helvetica', 12, 'bold'), bg='white')
        numguiaLabel.place(x=40, y=35)
        
        ctk.CTkLabel(pedido, text='' ,image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'almacen.png')), size=(25,25))).place(x=30, y=80)
        almacenLabel = tk.Label(pedido, text=ped[10], font=('Helvetica', 12, 'bold'), bg='white')
        almacenLabel.place(x=60, y=75)
        ubicacionalmacenLabel = tk.Label(pedido, text=f"{ped[11]}, {ped[12]}", font=('Helvetica', 9), fg='#727171', bg='white')
        ubicacionalmacenLabel.place(x=60, y=95)
        
        
        ctk.CTkLabel(pedido, text='' ,image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'ubicacion.png')), size=(25,25))).place(x=30, y=130)
        destinoLabel = tk.Label(pedido, text=ped[5], font=('Helvetica', 12, 'bold'), bg='white')
        destinoLabel.place(x=60, y=125)
        ubicaciondestinoLabel = tk.Label(pedido, text=ped[1], font=('Helvetica', 9), fg='#727171', bg='white')
        ubicaciondestinoLabel.place(x=62, y=145)
        
        tk.Label(pedido, text='Estado:', font=('Helvetica', 9), fg='#727171', bg='white').place(x=270, y=15)
        tk.Label(pedido, text='Entregado' if ped[7] == 1 else 'Por Entregar', font=('Helvetica', 10, 'bold'), bg='white').place(x=270, y=30)
        
        ctk.CTkButton(pedido, text='Gestionar', 
                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                text_color='white', 
                                width=100, height=30, 
                                corner_radius=50, 
                                hover_color='#003D84',
                                cursor='hand2',
                                command=lambda: controller.viewPedido(self.idpedido)
                    ).place(x=260, y=135)
    
        
class viewGPFormulario:
    
    def __init__(self, submenu, controller, accion, id=None):
        self.submenu = submenu
        self.controller = controller
        self.accion = accion
        self.id = id
        self.initView()
        self.configFormulario()
        
    def initView(self):
        self.contenedorGP = tk.Frame(self.submenu, bg='white')
        self.contenedorGP.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedorGP, text="Gestión de pedidos", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorGP)
        contenedorBackFor.pack(side='right', anchor='n')
        
        
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.controller.viewGestionPedidos
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
    
    def configFormulario(self):
        contenedorFormulario = tk.Frame(self.contenedorGP, bg='white')
        contenedorFormulario.place(relwidth=1, relheight=0.7, rely=0.1)
        
        if self.accion == 'registrar': 
            tk.Label(contenedorFormulario, text="Nuevo Pedido", font=gl.FONT_APP_H3, bg='white').pack(side="left", anchor='n')
            
            self.guia = ''
            caracteres = string.ascii_uppercase + string.ascii_lowercase + '0123456789'
            for _ in range(10):
                self.guia += random.SystemRandom().choice(caracteres)
                
        if self.accion == 'actualizar':
            tk.Label(contenedorFormulario, text="Actualizar Pedido", font=gl.FONT_APP_H3, bg='white').pack(side="left", anchor='n')
            
            pedido = self.controller.pedidosModel.findPedidoPorId(self.id)
            self.guia = pedido.atributos['ped_guia']
            
                
        # ------------------- FRAME DESTINO --------------------------------------------------------------
            
        destinoFrame = tk.LabelFrame(contenedorFormulario, text='Destino', font=gl.FONT_APP_H4, bg='white')
        destinoFrame.place(relheight=0.2, relwidth=0.9, anchor='center', relx=0.5, rely=0.2)
        
        tk.Label(destinoFrame, text='Ciudad', font=gl.FONT_APP_H4, bg='white').place(relx=0.05, rely=0.05)
        tk.Label(destinoFrame, text='Estado', font=gl.FONT_APP_H4, bg='white').place(relx=0.48, rely=0.05)
        tk.Label(destinoFrame, text='Pais', font=gl.FONT_APP_H4, bg='white').place(relx=0.75, rely=0.05)
        
        self.CiudadEntry = ctk.CTkEntry(destinoFrame, border_width=1, font=gl.FONT_APP_H4)
        self.CiudadEntry.place(relx=0.05, rely=0.4, relwidth=0.4)
        self.EstadoEntry = ctk.CTkEntry(destinoFrame, border_width=1, font=gl.FONT_APP_H4)
        self.EstadoEntry.place(relx=0.48, rely=0.4, relwidth=0.25)
        self.PaisEntry = ctk.CTkEntry(destinoFrame, border_width=1, font=gl.FONT_APP_H4)
        self.PaisEntry.place(relx=0.75, rely=0.4, relwidth=0.2)
        
        # ------------------- FRAME DETALLES  --------------------------------------------------------------
            
        detallesFrame = tk.LabelFrame(contenedorFormulario, text='Detalles del Pedido', font=gl.FONT_APP_H4, bg='white')
        detallesFrame.place(relheight=0.55, relwidth=0.4, anchor='center', relx=0.25, rely=0.65)
        
        tk.Label(detallesFrame, text='Cliente:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.07, anchor='center')
        tk.Label(detallesFrame, text='Producto:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.37, anchor='center')
        tk.Label(detallesFrame, text='Num. Guia:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.7, anchor='center')
        
        listProductos = list()
        listProductos.append('')
        AllProductos = self.controller.productosModel.allProductos()
        for p in AllProductos:
            nombre = p.atributos['prod_nombre']
            listProductos.append(f'{nombre}')
        
        self.ClienteEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.ClienteEntry.place(relx=0.5, rely=0.21, anchor='center', relwidth=0.8)
        self.Producto = ctk.CTkComboBox(detallesFrame, font=gl.FONT_APP_H4, height=30,
                                                    values=listProductos,
                                                    command=self.calcularPrecio,
                                                    state="readonly"
                                )
        self.Producto.place(relx=0.5, rely=0.51, anchor='center', relwidth=0.8, )
            
        tk.Label(detallesFrame, text=self.guia, font=gl.FONT_APP_H3, bg='white').place(relx=0.5, rely=0.85, anchor='center')
        
        # ------------------- ENVIO --------------------------------------------------------------
        
        envioFrame = tk.LabelFrame(contenedorFormulario, text='Finalizar', font=gl.FONT_APP_H4, bg='white')
        envioFrame.place(relheight=0.55, relwidth=0.45, anchor='center', relx=0.725, rely=0.65)
        
        
        tk.Label(envioFrame, text='Costo sin transporte:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.2, anchor='center')
        self.costo = tk.Label(envioFrame, text='$0.00 MXN', font=gl.FONT_APP_H3, bg='white')
        self.costo.place(relx=0.5, rely=0.35, anchor='center')
        
        ctk.CTkButton(envioFrame, text='Confirmar Pedido',
                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                corner_radius=20,
                                height=50,
                                font=gl.FONT_APP_H1,
                                hover_color='#003D84',
                                command=self.resolverAccion
                    ).place(relx=0.5, rely=0.7, anchor='center', relwidth=0.8)
        
        if self.accion == 'actualizar':
            destino = pedido.atributos['ped_destino'].split(', ')
            self.CiudadEntry.insert(0, destino[0])
            self.EstadoEntry.insert(0, destino[1])
            self.PaisEntry.insert(0, destino[2])
            
            self.ClienteEntry.insert(0, pedido.atributos['ped_cliente'])
            
            producto = self.controller.productosModel.findProductoPorId(pedido.atributos['ped_prod_id'])
            self.Producto.set(producto.atributos['prod_nombre'])
            self.sumaPrecios = pedido.atributos['ped_costo_total']
            precioFinal = f'${self.sumaPrecios}.00 MXN'
            self.costo.config(text=precioFinal)
            

    def calcularPrecio(self, choice=None):
        if not choice == '':
            selected = choice
            producto = self.controller.productosModel.findProductoPorNombre(selected)
            
            almacen = self.controller.almacenesModel.findAlmacenPorID(producto.atributos['prod_alm_id'])

            precioProducto = producto.atributos['prod_costo']
            precioAlmacen = almacen.atributos['alm_costo']
            self.sumaPrecios = precioAlmacen + precioProducto
            
            precioFinal = f'${self.sumaPrecios}.00 MXN'
            
            self.costo.config(text=precioFinal)
        else:
            precioFinal = '$0.00 MXN'
            self.costo.config(text=precioFinal)

    def mostrarErrores(self, errores):
        
        stringErrores = 'Los siguientes datos son necesarios: \n'
        
        for e in errores:
            stringErrores += e      
            stringErrores += '\n'      

        messagebox.showwarning('Datos faltantes', stringErrores)
        
    def resolverAccion(self):
        if self.accion == 'registrar':
            self.controller.newPedido()
        if self.accion == 'actualizar':
            self.controller.actualizarPedido(self.id)
                    
    def mostrarMensajeConfirmacion(self):
        if self.accion == 'registrar':
            messagebox.showinfo('Pedido Realizado', 'El pedido se ha registrado correctamente. :)')
            self.controller.viewGestionPedidos()
        if self.accion == 'actualizar':
            messagebox.showinfo('Pedido Realizado', 'El pedido se ha actualizado correctamente. :)')
            self.controller.viewGestionPedidos()
        
    
        
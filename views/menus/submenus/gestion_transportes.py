import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewGT:
    def __init__(self, submenu, controller):
        self.submenu = submenu
        self.controller = controller
        
        self.initView()
        self.configTrans()
        self.configTransAsig()
    
    def initView(self):
        self.contenedorGT = tk.Frame(self.submenu, bg='white')
        self.contenedorGT.place(x=0, y=0, relwidth=1, relheight=1)
        
        tk.Label(self.contenedorGT, text="Gestión de transportes", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorGT)
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
        
        
    def configTrans(self):
        self.transportes = tk.Frame(self.contenedorGT, bg='white')
        self.transportes.place(relx=0, rely=0.08, relwidth=1, relheight=0.35)
        
        tk.Label(self.transportes, text="Transportes Disponibles", font=('Helvetica', 10, "bold"), bg='white').place(x=0, y=0, relheight=0.1)
        
        # ------------------- TABLA --------------------------------------
        
        contenedortabla = tk.Frame(self.transportes, bg='white')
        contenedortabla.place(relx=0, rely=0.1, relheight=0.9, relwidth=0.6)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedortabla, columns=('Transporte', 'Tipo', 'Cantidad', 'Disponible'), show='headings')
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(tabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column("Transporte", width=120, anchor='w')
        tabla.column('Tipo', width=40, anchor='w')
        tabla.column("Cantidad", width=20, anchor='w')
        tabla.column("Disponible", width=20, anchor='w')
        
        tabla.heading('Transporte', text='Transporte', anchor='w')
        tabla.heading('Tipo', text='Tipo', anchor='w')
        tabla.heading('Cantidad', text='Cant.', anchor='w')
        tabla.heading('Disponible', text='Disp.', anchor='w')
        
        transportes = self.controller.transportesModel.allTransportes()
        
        for t in transportes:
            tabla.insert('', tk.END, text='', 
                         values=(t.atributos['tra_nombre'], t.atributos['tra_tipo'], t.atributos['tra_cantidad'], t.atributos['tra_disponible']))
            
        # ------------------- BOTONES --------------------------------------
        
        contenedorBotones = tk.Frame(self.transportes, bg='white')
        contenedorBotones.place(relx=0.625, rely=0.1, relheight=0.8, relwidth=0.35)
        
        self.gestionarTrans = ctk.CTkButton(contenedorBotones, text='Gestionar Transportes', fg_color=gl.COLOR_AZUL_PRIMARIO, text_color='white', hover_color='#003D84', corner_radius=0, font=('Helvetica', 18, "bold"))
        self.gestionarTrans.place(rely=0, relwidth=1, relheight=0.8)
    
    def configTransAsig(self):
        self.transportesAsig = tk.Frame(self.contenedorGT, bg='white')
        self.transportesAsig.place(relx=0, rely=0.45, relwidth=1, relheight=0.35)
        
        tk.Label(self.transportesAsig, text="Transportes por asignar", font=('Helvetica', 10, "bold"), bg='white').pack(side="left", anchor='n')
        
        # ------------------- TABLA --------------------------------------
        
        contenedortabla = tk.Frame(self.transportesAsig, bg='white')
        contenedortabla.place(relx=0, rely=0.1, relheight=0.9, relwidth=0.6)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        self.tablaAsig = ttk.Treeview(contenedortabla, columns=('Proveedor', 'Mercancia', 'Caducidad', 'Destino'), show='headings')
        self.tablaAsig.place(relwidth=1, relheight=1)
        
        self.tablaAsig.bind("<<TreeviewSelect>>", self.itemSeleccionado)
        
        scrollbar_vertical = tk.Scrollbar(self.tablaAsig)
        scrollbar_vertical.pack(side='right', fill='y')
        scrollbar_vertical.config(command=self.tablaAsig.yview)
        self.tablaAsig.config(yscrollcommand=scrollbar_vertical.set)
        
        self.tablaAsig.column("Proveedor", width=60, anchor='w')
        self.tablaAsig.column('Mercancia', width=40, anchor='w')
        self.tablaAsig.column("Caducidad", width=30, anchor='w')
        self.tablaAsig.column("Destino", width=120, anchor='w')
        
        self.tablaAsig.heading('Proveedor', text='Proveedor', anchor='w')
        self.tablaAsig.heading('Mercancia', text='Mercancia', anchor='w')
        self.tablaAsig.heading('Caducidad', text='Caducidad', anchor='w')
        self.tablaAsig.heading('Destino', text='Destino', anchor='w')
        
        porAsignar = self.controller.transportesModel.transportesPorAsignar()
        
        for p in porAsignar:
            self.tablaAsig.insert('', tk.END, values=(p[0], p[1], p[2] if p[2] != None else 'NO', p[3]), tags=p[4])
            
        # ------------------- BOTONES --------------------------------------
        
        self.id = None
        
        contenedorBotones = tk.Frame(self.transportesAsig, bg='white')
        contenedorBotones.place(relx=0.625, rely=0.1, relheight=0.8, relwidth=0.35)
        
        self.asignarPedidos = ctk.CTkButton(contenedorBotones, 
                                            text='Asignar un transporte\na un pedido', 
                                            fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                            text_color='white', 
                                            hover_color='#003D84', 
                                            corner_radius=0, 
                                            font=('Helvetica', 18, "bold"),
                                            command=self.accionAlAsignar
                                            )
        self.asignarPedidos.place(rely=0.1, relwidth=1, relheight=0.8)
    
    def accionAlAsignar(self):
        if self.id:
            self.controller.viewTransporteAsignar(self.id)
            self.id = None
        else:
            messagebox.showinfo('Importante', 'Selecciona un registro de la tabla para asignarle un pedido.')
    
    def itemSeleccionado(self, event):
        item = self.tablaAsig.focus()
        
        data = self.tablaAsig.item(item)
        self.id = data['tags'][0]
        
    def eliminarFramesContenedor(self):
        for frame in self.contenedorGT.winfo_children():
            frame.destroy()
            
            
            
class viewTransporteAsignar:
    def __init__(self, submenu, controller, id):
        self.submenu = submenu
        self.controller = controller
        self.id = id
        
        self.initView()
        self.configView()
    
    def initView(self):
        self.contenedorGT = tk.Frame(self.submenu, bg='white')
        self.contenedorGT.place(x=0, y=0, relwidth=1, relheight=1)
        
        tk.Label(self.contenedorGT, text="Gestión de transportes", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorGT)
        contenedorBackFor.pack(side='right', anchor='n')
        
        
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.controller.viewGestionTransportes
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
        
    def configView(self):
        contenedorFormulario = tk.Frame(self.contenedorGT, bg='white')
        contenedorFormulario.place(relwidth=1, relheight=0.7, rely=0.1)
        
        # ------------------------- FRAME PEDIDO -----------------------------------------
        
        pedidoFrame = tk.LabelFrame(contenedorFormulario, text='Detalles del pedido', font=gl.FONT_APP_H4, bg='white')
        pedidoFrame.place(relheight=0.3, relwidth=0.9, anchor='center', relx=0.5, rely=0.2)
        
        pedido = self.controller.pedidosModel.findPedidoPorId(self.id)
        producto = self.controller.productosModel.findProductoPorId(pedido.atributos['ped_prod_id'])
        
        tk.Label(pedidoFrame, text='Destino:', font=gl.FONT_APP_H5, bg='white').place(relx=0.05, rely=0.05)
        tk.Label(pedidoFrame, text=pedido.atributos['ped_destino'], font=gl.FONT_APP_P, bg='white').place(relx=0.05, rely=0.2)
        
        tk.Label(pedidoFrame, text='Producto:', font=gl.FONT_APP_H5, bg='white').place(relx=0.05, rely=0.5)
        tk.Label(pedidoFrame, text=producto.atributos['prod_nombre'], font=gl.FONT_APP_P, bg='white').place(relx=0.05, rely=0.65)
        
        tk.Label(pedidoFrame, text='Cliente:', font=gl.FONT_APP_H5, bg='white').place(relx=0.5, rely=0.5)
        tk.Label(pedidoFrame, text=pedido.atributos['ped_cliente'], font=gl.FONT_APP_P, bg='white').place(relx=0.5, rely=0.65)
        
        tk.Label(pedidoFrame, text='Costo Total:', font=gl.FONT_APP_H5, bg='white').place(relx=0.62, rely=0.05)
        tk.Label(pedidoFrame, text=f"${pedido.atributos['ped_costo_total']}.00 MXN", font=gl.FONT_APP_P, bg='white').place(relx=0.75, rely=0.05)
        
        tk.Label(pedidoFrame, text='Guia:', font=gl.FONT_APP_H5, bg='white').place(relx=0.62, rely=0.22)
        tk.Label(pedidoFrame, text=pedido.atributos['ped_guia'], font=gl.FONT_APP_P, bg='white').place(relx=0.75, rely=0.22)
        
        # ------------------------- FRAME SELECCION TRANSPORTE -----------------------------------------
        
        detallesFrame = tk.LabelFrame(contenedorFormulario, text='Detalles del transporte', font=gl.FONT_APP_H4, bg='white')
        detallesFrame.place(relheight=0.55, relwidth=0.4, anchor='center', relx=0.25, rely=0.65)
        
        listaTransportes = list()
        transportes = self.controller.transportesModel.allTransportes()
        
        for tranporte in transportes:
            if not tranporte.atributos['tra_cantidad'] == tranporte.atributos['tra_disponible']:
                listaTransportes.append(tranporte.atributos['tra_nombre'])
        
        tk.Label(detallesFrame, text='Transporte:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.17, anchor='center')
        self.transporte = ctk.CTkComboBox(detallesFrame, font=gl.FONT_APP_H4, 
                                                        height=30,
                                                        state="readonly",
                                                        values=listaTransportes
                                            )
        self.transporte.place(relx=0.5, rely=0.31, anchor='center', relwidth=0.8, )
        ctk.CTkButton(detallesFrame, text='Confirmar Asignación',
                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                corner_radius=20,
                                height=50,
                                font=gl.FONT_APP_H1,
                                hover_color='#003D84',
                                command=self.controller.asignarTransporte
                    ).place(relx=0.5, rely=0.7, anchor='center', relwidth=0.8)
        
        # ------------------------- FRAME MOSTRAR TRANSPORTES -----------------------------------------
        
        transportesFrame = tk.LabelFrame(contenedorFormulario, text='Transportes Disponibles', font=gl.FONT_APP_H4, bg='white')
        transportesFrame.place(relheight=0.55, relwidth=0.45, anchor='center', relx=0.725, rely=0.65)
        
        contenedortabla = tk.Frame(transportesFrame, bg='white')
        contenedortabla.place(relx=0, rely=0.05, relheight=0.9, relwidth=1)
        
        estilo_tabla = ttk.Style()
        estilo_tabla.theme_use("clam")
        estilo_tabla.configure("Treeview", font=('Helvetica', 10), background='white', fieldbackground='white', rowheight=25, bordercolor="white")
        estilo_tabla.configure("Treeview.Heading", font=('Helvetica', 12), background=gl.COLOR_AZUL_PRIMARIO, foreground='white', relief='flat')
        estilo_tabla.map("Treeview.Heading", background=[('selected', gl.COLOR_AZUL_PRIMARIO)])
        estilo_tabla.map("Treeview", background=[('selected', gl.COLOR_AZUL_2)])
        
        tabla = ttk.Treeview(contenedortabla, columns=('Transporte', 'Tipo', 'Cantidad', 'Disponible'), show='headings')
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(tabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column("Transporte", width=100, anchor='w')
        tabla.column('Tipo', width=40, anchor='w')
        tabla.column("Cantidad", width=20, anchor='w')
        tabla.column("Disponible", width=20, anchor='w')
        
        tabla.heading('Transporte', text='Transporte', anchor='w')
        tabla.heading('Tipo', text='Tipo', anchor='w')
        tabla.heading('Cantidad', text='Cant.', anchor='w')
        tabla.heading('Disponible', text='Disp.', anchor='w')
        
        for t in transportes:
            tabla.insert('', tk.END, text='', 
                         values=(t.atributos['tra_nombre'], t.atributos['tra_tipo'], t.atributos['tra_cantidad'], t.atributos['tra_disponible']))
    
    
    def mostrarErrores(self, errores):
        
        stringErrores = 'Los siguientes datos son necesarios: \n'
        
        for e in errores:
            stringErrores += e      
            stringErrores += '\n'      

        messagebox.showwarning('Datos faltantes', stringErrores)
    
    def mostrarMensajeConfirmacion(self):
        messagebox.showinfo('Transporte asignado', 'El pedido se le ha asignado un transporte correctamente. :)')
        self.controller.viewGestionTransportes()
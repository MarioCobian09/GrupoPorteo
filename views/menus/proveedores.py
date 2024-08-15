import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewProveedores:
    
    def __init__(self, contenedor, controller):
        self.root = contenedor
        
        self.controller = controller
        
        self.menu_proovedores()
        self.configProveedores()
    
    def menu_proovedores(self):
        self.proovedores = tk.Frame(self.root, bg='white')
        self.proovedores.pack(fill='both', expand=True)
        
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(100, 100))
        imagen = ctk.CTkLabel(self.proovedores, image=img_logo, fg_color='white', text='')
        imagen.pack(side="right", anchor='n', padx=20, pady=1)
        
        tk.Label(self.proovedores, text="Proveedores", font=gl.FONT_APP_H1, bg='white').place(relx=0.04, rely=0.05)
        
        self.submenu = tk.Frame(self.proovedores, bg='white')
        self.submenu.place(relwidth=0.92, relheight=1, y=100, relx=0.5, anchor='center', rely=0.5)
        
    def configProveedores(self):
        
        contenedorProv = ctk.CTkScrollableFrame(self.submenu, fg_color='#CFCFCF')
        contenedorProv.place(relwidth=1, relheight=0.75)
        
        allProveedores = self.controller.proveedoresModel.allProveedores()
        row = 0
        column = 0
        for proveedor in allProveedores:       
            cardProv = ctk.CTkFrame(contenedorProv, fg_color='white', 
                                                    height=100,
                                                    border_color=gl.COLOR_AZUL_PRIMARIO,
                                                    border_width=3,
                                                    corner_radius=50,
                                                    )
            cardProv.grid(row=row, column=column, sticky=tk.NSEW, padx=10, pady=10)
            
            imgEmpresa = ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'empresa.png')), size=(60,60))
            ctk.CTkLabel(cardProv, image=imgEmpresa, text='', fg_color='white').pack(anchor='center', pady=20)
            
            tk.Label(cardProv, text=proveedor.atributos['prov_nombre'], font=gl.FONT_APP_H3, bg='white').pack()
            tk.Label(cardProv, text=proveedor.atributos['prov_correo'], font=gl.FONT_APP_P, bg='white').pack()
            tk.Label(cardProv, text=proveedor.atributos['prov_telefono'], font=gl.FONT_APP_H5, bg='white').pack()
            
            string = proveedor.atributos['prov_direccion']
            string = string.split(', ')
            string = '\n'.join(string)
            tk.Label(cardProv, text=string, font=gl.FONT_APP_P, bg='white').pack()
            
            column += 1
            
            if column == 3:
                row += 1
                column = 0
                
        for i in range(row+1):
            contenedorProv.grid_rowconfigure(i, weight=1, pad=30)
            
        contenedorProv.grid_columnconfigure(0, weight=1)
        contenedorProv.grid_columnconfigure(1, weight=1)
        contenedorProv.grid_columnconfigure(2, weight=1)
        
        self.nuevoProveedor = ctk.CTkButton(self.submenu, 
                                                text='Nuevo Proovedor', 
                                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                                text_color='white', 
                                                hover_color='#003D84', 
                                                corner_radius=0, 
                                                font=('Helvetica', 15, "bold"),
                                                command=self.controller.viewProvForm
                                            )
        self.nuevoProveedor.place(relx=0.75, rely=0.76, relwidth=0.2, relheight=0.05)

    def viewFormProv(self):
        self.contenedor = tk.Frame(self.submenu, bg='white')
        self.contenedor.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedor, text="Nuevo Proveedor", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
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
        
        contenedorFormulario = tk.Frame(self.contenedor, bg='white')
        contenedorFormulario.place(relwidth=1, relheight=0.7, rely=0.1)
            
                
        # ------------------- FRAME DATOS  --------------------------------------------------------------
            
        personalesFrame = tk.LabelFrame(contenedorFormulario, text='Datos del Proveedor', font=gl.FONT_APP_H4, bg='white')
        personalesFrame.place(relheight=0.2, relwidth=0.9, anchor='center', relx=0.5, rely=0.2)
        
        tk.Label(personalesFrame, text='Nombre del Proveedor:', font=gl.FONT_APP_H4, bg='white').place(relx=0.05, rely=0.05)
        tk.Label(personalesFrame, text='Dirección:', font=gl.FONT_APP_H4, bg='white').place(relx=0.48, rely=0.05)
        
        self.nombreEntry = ctk.CTkEntry(personalesFrame, border_width=1, font=gl.FONT_APP_H4)
        self.nombreEntry.place(relx=0.05, rely=0.4, relwidth=0.4)
        self.direccionEntry = ctk.CTkEntry(personalesFrame, border_width=1, font=gl.FONT_APP_H4)
        self.direccionEntry.place(relx=0.48, rely=0.4, relwidth=0.5)
        
        # ------------------- FRAME DATOS COMUNICARSE  --------------------------------------------------------------
            
        detallesFrame = tk.LabelFrame(contenedorFormulario, text='Datos de Contacto', font=gl.FONT_APP_H4, bg='white')
        detallesFrame.place(relheight=0.55, relwidth=0.4, anchor='center', relx=0.25, rely=0.65)
        
        tk.Label(detallesFrame, text='Telefono:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.07, anchor='center')
        self.telefonoEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.telefonoEntry.place(relx=0.5, rely=0.21, anchor='center', relwidth=0.8)
        
        tk.Label(detallesFrame, text='Correo:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.37, anchor='center')
        self.correoEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.correoEntry.place(relx=0.5, rely=0.51, anchor='center', relwidth=0.8)
        
        
        # ------------------- CONFIMACION  --------------------------------------------------------------
        
        confirmacionFrame = tk.LabelFrame(contenedorFormulario, text='Finalizar', font=gl.FONT_APP_H4, bg='white')
        confirmacionFrame.place(relheight=0.55, relwidth=0.45, anchor='center', relx=0.725, rely=0.65)
        
        ctk.CTkButton(confirmacionFrame, text='Confirmar Proveedor',
                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                corner_radius=20,
                                height=50,
                                font=gl.FONT_APP_H1,
                                hover_color='#003D84',
                                command=self.sendData
                    ).place(relx=0.5, rely=0.5, anchor='center', relwidth=0.8)
        
        
    def sendData(self):
        errores = list()
        data = {
            'Nombre': self.nombreEntry.get(),
            'Dirección': self.direccionEntry.get(),
            'Telefono': f"+52 {self.telefonoEntry.get()}",
            'Correo': self.correoEntry.get()
        }
        
        for key in data.keys():
            if not data[key]:
                errores.append(f'El {key} es Obligatorio')
            
        if len(errores) != 0:
            return self.mostrarErrores(errores)
             
        if not self.telefonoEntry.get().isdecimal():
             errores.append(f'El Telefono debe tener numeros')
             
        if data['Correo'].find('@') == -1:
            errores.append(f'El correo no tiene un formato valido')
            
        if len(errores) != 0:
            return self.mostrarErrores(errores)
            
        self.controller.registrarProveedor(**data)
        self.mostrarMensajeConfirmacion()
        
    def mostrarErrores(self, errores):
        
        stringErrores = 'Los siguientes datos son necesarios: \n'
        
        for e in errores:
            stringErrores += e      
            stringErrores += '\n'      

        messagebox.showwarning('Datos faltantes', stringErrores)
    
    def mostrarMensajeConfirmacion(self):
        messagebox.showinfo('Proveedor registrado', 'El Proveedor se agrego a la base de datos correctamente. :)')
        self.controller.viewMenu()
                
    def eliminarFramesSubmenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        
    def regresarAlMenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        self.configProveedores()
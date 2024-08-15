import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import os.path

from includes import globales as gl

class viewRH:
    
    def __init__(self, contenedor, controller):
        self.root = contenedor
        
        self.controller = controller
        
        self.menu_rh()
        self.configView()
        
    def menu_rh(self):
        self.rh = tk.Frame(self.root, bg='white')
        self.rh.pack(fill='both', expand=True)
        
        img_logo = ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, 'Logo-Grupo-Porteo.png'))), size=(100, 100))
        imagen = ctk.CTkLabel(self.rh, image=img_logo, fg_color='white', text='')
        imagen.pack(side="right", anchor='n', padx=20, pady=1)
        
        tk.Label(self.rh, text="Recursos Humanos", font=gl.FONT_APP_H1, bg='white').place(relx=0.04, rely=0.05)
        
        self.submenu = tk.Frame(self.rh, bg='white')
        self.submenu.place(relwidth=0.92, relheight=1, y=100, relx=0.5, anchor='center', rely=0.5)
        
        
    def configView(self):
        contenedorInfo = tk.Frame(self.submenu, bg='white')
        contenedorInfo.place(relwidth=1, relheight=0.25)
        
        contenedorInfo.grid_columnconfigure(0, weight=1)
        contenedorInfo.grid_columnconfigure(1, weight=1)
        contenedorInfo.grid_columnconfigure(2, weight=1)
        contenedorInfo.grid_rowconfigure(0, weight=1)
        
        numUsuarios = len(self.controller.usuariosModel.allUsuarios())
        
        personalActual = tk.Frame(contenedorInfo, bg=gl.COLOR_AZUL_OSCURO)
        personalActual.grid(row=0, column=0, sticky=tk.NSEW, padx=10, pady=20)
        personalActual.propagate(0)
        contenedor = tk.Frame(personalActual, bg=gl.COLOR_AZUL_OSCURO)
        contenedor.pack(anchor='center', side='right')
        tk.Label(contenedor, text=numUsuarios, font=('Helvetica', 30, "bold"), fg='white', bg=gl.COLOR_AZUL_OSCURO).pack(side='top', anchor='e')
        tk.Label(contenedor, text='Personal Actual', font=('Helvetica', 12), fg='white', bg=gl.COLOR_AZUL_OSCURO).pack(side='top', anchor='e')
        
        numdepartamentos = len(self.controller.usuariosModel.obtenerDepartamentos())
        departamentos = tk.Frame(contenedorInfo, bg=gl.COLOR_ROJO_OSCURO)
        departamentos.grid(row=0, column=1, sticky=tk.NSEW, padx=10, pady=20)
        departamentos.propagate(0)
        contenedor = tk.Frame(departamentos, bg=gl.COLOR_ROJO_OSCURO)
        contenedor.pack(anchor='center', side='right')
        tk.Label(contenedor, text=numdepartamentos, font=('Helvetica', 30, "bold"), fg='white', bg=gl.COLOR_ROJO_OSCURO).pack(side='top', anchor='e')
        tk.Label(contenedor, text='Departamentos Actuales', font=('Helvetica', 12), fg='white', bg=gl.COLOR_ROJO_OSCURO).pack(side='top', anchor='e')
        
        vacantes = tk.Frame(contenedorInfo, bg=gl.COLOR_AZUL_OSCURO)
        vacantes.grid(row=0, column=2, sticky=tk.NSEW, padx=10, pady=20)
        vacantes.propagate(0)
        contenedor = tk.Frame(vacantes, bg=gl.COLOR_AZUL_OSCURO)
        contenedor.pack(anchor='center', side='right')
        tk.Label(contenedor, text='12', font=('Helvetica', 30, "bold"), fg='white', bg=gl.COLOR_AZUL_OSCURO).pack(side='top', anchor='e')
        tk.Label(contenedor, text='Vacantes nuevas', font=('Helvetica', 12), fg='white', bg=gl.COLOR_AZUL_OSCURO).pack(side='top', anchor='e')
        
        contenedorBotones = tk.Frame(self.submenu, bg='white')
        contenedorBotones.place(relwidth=0.8, relheight=0.55, rely=0.25, relx=0.1)
        
        contenedorBotones.grid_columnconfigure(0, weight=1)
        contenedorBotones.grid_columnconfigure(1, weight=1)
        contenedorBotones.grid_rowconfigure(0, weight=1)
        contenedorBotones.grid_rowconfigure(1, weight=1)
        
        btn_nominas = ctk.CTkButton(contenedorBotones, command=self.controller.viewTabla)
        btn_vacaciones = ctk.CTkButton(contenedorBotones)
        btn_evaluaciones = ctk.CTkButton(contenedorBotones, command=self.controller.viewTabla)
        btn_nuevopersonal = ctk.CTkButton(contenedorBotones, command=self.controller.viewRHForm)
        
        btn_menus = [
            ('Gestión de Nominas', 'icono_nomina.png', btn_nominas),
            ('Solicitud y planificación\nde Vacaciones', 'icono_vacaciones.png', btn_vacaciones),
            ('Evaluación a Empleados', 'icono_evaluacion.png', btn_evaluaciones),
            ('Agregar Personal', 'usuario_icono.png', btn_nuevopersonal)
        ]
        
        contadorx = 0
        contadory = 0
        
        for nombre, icono, boton in btn_menus:
            
            boton.configure(text_color='white',
                            fg_color=gl.COLOR_AZUL_OSCURO,
                            image=ctk.CTkImage(light_image=(Image.open(os.path.join(gl.RUTA_IMG, icono))), size=(70,70)),
                            font=('Helvetica', 18, "bold"),
                            corner_radius=0,
                            cursor='hand2',
                            compound='top',
                            text=nombre,
                            hover_color='#003D84',
                            )
            boton.grid(row=contadorx, column=contadory, sticky=tk.NSEW, padx=10, pady=10)
            
            contadorx = 1 if contadory == 1 or contadorx == 1 else 0
            contadory = 1 if contadorx == 0 or contadory != 1  else 0
            
    def viewTabla(self):
        self.contenedor = tk.Frame(self.submenu, bg='white')
        self.contenedor.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedor, text="Personal Actual", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
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
        
        tabla = ttk.Treeview(contenedorTabla, columns=('Nombre', 'ApPaterno', 'ApMaterno', 'Correo', 'Telefono', 'Puesto'), show='headings', height=4)
        tabla.place(relwidth=1, relheight=1)
        
        scrollbar_vertical = tk.Scrollbar(contenedorTabla)
        scrollbar_vertical.pack(side='right', fill='y')
        
        scrollbar_vertical.config(command=tabla.yview)
        tabla.config(yscrollcommand=scrollbar_vertical.set)
        
        tabla.column('Nombre', width=50, anchor='w', minwidth=50)
        tabla.column('ApPaterno', width=80, anchor='w', minwidth=50)
        tabla.column('ApMaterno', width=80, anchor='w', minwidth=50)
        tabla.column('Correo', width=120, anchor='w', minwidth=120)
        tabla.column('Telefono', width=100, anchor='w', minwidth=100)
        tabla.column('Puesto', width=100, anchor='w', minwidth=100)
        
        tabla.heading('Nombre', text='Nombre', anchor='w')
        tabla.heading('ApPaterno', text='Ap. Paterno', anchor='w')
        tabla.heading('ApMaterno', text='Ap. Materno', anchor='w')
        tabla.heading('Correo', text='Correo', anchor='w')
        tabla.heading('Telefono', text='Telefono', anchor='w')
        tabla.heading('Puesto', text='Puesto', anchor='w')
        
        allUsuarios = self.controller.usuariosModel.allUsuarios()
        
        for a in allUsuarios:
            tabla.insert('', tk.END, text='', 
                         values=(a.atributos['usu_nombre'], 
                                 a.atributos['usu_ap_paterno'], 
                                 a.atributos['usu_ap_materno'],
                                 a.atributos['usu_correo'],
                                 a.atributos['usu_telefono'],
                                 a.atributos['usu_puesto']
                        ))
    
    def eliminarFramesSubmenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        
    def regresarAlMenu(self):
        for frame in self.submenu.winfo_children():
            frame.destroy()
        self.configView()
        
        
        
            
class viewPersonalForm:
    def __init__(self, submenu, controller):
        self.submenu = submenu
        self.controller = controller

        self.initView()
        self.configFormulario()
        
    def initView(self):
        self.contenedorForm = tk.Frame(self.submenu, bg='white')
        self.contenedorForm.place(relwidth=1, relheight=1)
        
        tk.Label(self.contenedorForm, text="Nuevo Personal", font=gl.FONT_APP_H2, bg='white').pack(side="left", anchor='n')
        
        contenedorBackFor = tk.Frame(self.contenedorForm)
        contenedorBackFor.pack(side='right', anchor='n')
        
        
        btnBack = ctk.CTkButton(contenedorBackFor, image=ctk.CTkImage(light_image=Image.open(os.path.join(gl.RUTA_IMG, 'anterior.png')), size=(35,35)),
                                                    bg_color='white',
                                                    fg_color='white',
                                                    cursor='hand2',
                                                    text='',
                                                    width=0,
                                                    height=0,
                                                    hover_color='#EFEFEF',
                                                    command=self.controller.viewMenu
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
        contenedorFormulario = tk.Frame(self.contenedorForm, bg='white')
        contenedorFormulario.place(relwidth=1, relheight=0.7, rely=0.1)
            
                
        # ------------------- FRAME DATOS PERSONALES --------------------------------------------------------------
            
        personalesFrame = tk.LabelFrame(contenedorFormulario, text='Datos del Usuario', font=gl.FONT_APP_H4, bg='white')
        personalesFrame.place(relheight=0.2, relwidth=0.9, anchor='center', relx=0.5, rely=0.2)
        
        tk.Label(personalesFrame, text='Nombre:', font=gl.FONT_APP_H4, bg='white').place(relx=0.05, rely=0.05)
        tk.Label(personalesFrame, text='Ap. Paterno:', font=gl.FONT_APP_H4, bg='white').place(relx=0.48, rely=0.05)
        tk.Label(personalesFrame, text='Ap. Materno:', font=gl.FONT_APP_H4, bg='white').place(relx=0.75, rely=0.05)
        
        self.nombreEntry = ctk.CTkEntry(personalesFrame, border_width=1, font=gl.FONT_APP_H4)
        self.nombreEntry.place(relx=0.05, rely=0.4, relwidth=0.4)
        self.apPaternoEntry = ctk.CTkEntry(personalesFrame, border_width=1, font=gl.FONT_APP_H4)
        self.apPaternoEntry.place(relx=0.48, rely=0.4, relwidth=0.25)
        self.apMaternoEntry = ctk.CTkEntry(personalesFrame, border_width=1, font=gl.FONT_APP_H4)
        self.apMaternoEntry.place(relx=0.75, rely=0.4, relwidth=0.2)
        
        # ------------------- FRAME DATOS ACCESO  --------------------------------------------------------------
            
        detallesFrame = tk.LabelFrame(contenedorFormulario, text='Datos de Acceso', font=gl.FONT_APP_H4, bg='white')
        detallesFrame.place(relheight=0.55, relwidth=0.4, anchor='center', relx=0.25, rely=0.65)
        
        tk.Label(detallesFrame, text='Telefono:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.07, anchor='center')
        self.telefonoEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.telefonoEntry.place(relx=0.5, rely=0.21, anchor='center', relwidth=0.8)
        
        tk.Label(detallesFrame, text='Correo:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.37, anchor='center')
        self.correoEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.correoEntry.place(relx=0.5, rely=0.51, anchor='center', relwidth=0.8)
        
        tk.Label(detallesFrame, text='Contraseña:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.7, anchor='center')
        self.passwordEntry = ctk.CTkEntry(detallesFrame, border_width=1, font=gl.FONT_APP_H4, height=30)
        self.passwordEntry.place(relx=0.5, rely=0.85, anchor='center', relwidth=0.8)
            
        
        # ------------------- CONFIMACION  --------------------------------------------------------------
        
        confirmacionFrame = tk.LabelFrame(contenedorFormulario, text='Finalizar', font=gl.FONT_APP_H4, bg='white')
        confirmacionFrame.place(relheight=0.55, relwidth=0.45, anchor='center', relx=0.725, rely=0.65)
        
        departamentos = self.controller.usuariosModel.obtenerDepartamentos()
        
        tk.Label(confirmacionFrame, text='Puesto del Usuario:', font=gl.FONT_APP_H4, bg='white').place(relx=0.5, rely=0.2, anchor='center')
        self.puesto = ctk.CTkComboBox(confirmacionFrame, font=gl.FONT_APP_H4, 
                                                        height=30,
                                                        state="readonly",
                                                        values=departamentos
                                            )
        self.puesto.place(relx=0.5, rely=0.35, anchor='center', relwidth=0.8, )
        
        ctk.CTkButton(confirmacionFrame, text='Confirmar Usuario',
                                fg_color=gl.COLOR_AZUL_PRIMARIO, 
                                corner_radius=20,
                                height=50,
                                font=gl.FONT_APP_H1,
                                hover_color='#003D84',
                                command=self.sendData
                    ).place(relx=0.5, rely=0.7, anchor='center', relwidth=0.8)
        
    def sendData(self):
        errores = list()
        data = {
            'Nombre': self.nombreEntry.get(),
            'ApPaterno': self.apPaternoEntry.get(),
            'ApMaterno': self.apMaternoEntry.get(),
            'Telefono': self.telefonoEntry.get(),
            'Correo': self.correoEntry.get(),
            'Password': self.passwordEntry.get(),
            'Puesto': self.puesto.get()
        }
        
        for key in data.keys():
            if not data[key]:
                errores.append(f'El {key} es Obligatorio')
            
        if len(errores) != 0:
            return self.mostrarErrores(errores)
        
        if not len(data['Telefono']) == 10:
             errores.append(f'El Telefono debe tener 10 numeros')
             
        if not data['Telefono'].isdecimal():
             errores.append(f'El Telefono debe tener numeros')
             
        if data['Correo'].find('@') == -1:
            errores.append(f'El correo no tiene un formato valido')
            
        if len(errores) != 0:
            return self.mostrarErrores(errores)

        data['img'] = f'{data["Nombre"]+data["ApPaterno"]+data["ApMaterno"]}.png'
            
        self.controller.registrarUsuario(**data)
        self.mostrarMensajeConfirmacion()
        
    def mostrarErrores(self, errores):
        
        stringErrores = 'Los siguientes datos son necesarios: \n'
        
        for e in errores:
            stringErrores += e      
            stringErrores += '\n'      

        messagebox.showwarning('Datos faltantes', stringErrores)
    
    def mostrarMensajeConfirmacion(self):
        messagebox.showinfo('Usuario registrado', 'El usuario se agrego a la base de datos correctamente. :)')
        self.controller.viewMenu()
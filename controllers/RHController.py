from views.menus import recursoshumanos

from models import usuariosModel

class RHController:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        self.usuariosModel = usuariosModel.usuariosModel()
        
        self.view = recursoshumanos.viewRH(contenedor, self)
        
    def viewMenu(self):
        self.view.eliminarFramesSubmenu()
        self.view.configView()
        
    def viewTabla(self):
        self.view.eliminarFramesSubmenu()
        self.view.viewTabla()
        
    def viewRHForm(self):
        self.view.eliminarFramesSubmenu()
        recursoshumanos.viewPersonalForm(self.view.submenu, self)
        
    def registrarUsuario(self, **kw):
        
        usuario = usuariosModel.usuariosModel(None, 
                                                kw['Nombre'],
                                                kw['ApPaterno'],
                                                kw['ApMaterno'],
                                                kw['Correo'],
                                                kw['Telefono'],
                                                kw['Password'],
                                                kw['Puesto'],
                                                kw['img']
                                            )
        usuario.insertarDatos()
        
        
        
    
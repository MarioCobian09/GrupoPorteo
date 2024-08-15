from views.menus import proveedores

from models import proveedoresModel

class ProveedoresController:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        self.proveedoresModel = proveedoresModel.proveedoresModel()
        
        self.view = proveedores.viewProveedores(self.contenedor, self)
        
    def viewMenu(self):
        self.view.eliminarFramesSubmenu()
        self.view.configProveedores()
        
    def viewProvForm(self):
        self.view.eliminarFramesSubmenu()
        self.view.viewFormProv()
        
    def registrarProveedor(self, **kw):
        
        proveedor = proveedoresModel.proveedoresModel(None,
                                                      kw['Nombre'],
                                                      kw['Correo'],
                                                      kw['Telefono'],
                                                      kw['Dirección']
                                                      )
        
        proveedor.insertarDatos()
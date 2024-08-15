from views.menus import serviciocliente

from models import reseñasModel, quejasysugerenciasModel

class ServClientController:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        self.reseñasModel = reseñasModel.reseñasModel()
        self.quejasysugerenciasModel = quejasysugerenciasModel.quejasysugerenciasModel()
        
        self.view = serviciocliente.viewServicioCliente(contenedor, self)
        
    def viewAnalizarReseñas(self):
        self.view.eliminarFramesSubmenu()
        self.view.viewReseñas()
        
    def viewQuejasySugerencias(self):
        self.view.eliminarFramesSubmenu()
        self.view.viewQuejas()
from views.menus import finanzas

from models import productosModel

class FinanzasController:
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        self.productosModel = productosModel.productosModel()
        
        self.view = finanzas.viewFinanzas(self.contenedor, self)
        
        
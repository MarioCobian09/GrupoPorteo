from views.menus import logistica
from views.menus.submenus import gestion_pedidos as gp, gestion_transportes as gt, gestion_almacenes as ga, analisis_reportes as ar

from models import transportesModel as transportes
from models import pedidosModel as pedidos
from models import almacenesModel as almacenes
from models import reportesModel as reportes
from models import productosModel as productos

from datetime import datetime

class LogisticaController:
    
    def __init__(self, contenedor):
        self.contenedor = contenedor
        
        self.view = logistica.viewLogistica(self.contenedor, self)
        
        self.transportesModel = transportes.transporteModel()
        self.pedidosModel = pedidos.pedidosModel()
        self.almacenesModel = almacenes.almacenesModel()
        self.reportesModel = reportes.reportesModel()
        self.productosModel = productos.productosModel()
    
    # ------------ VISTAS DE TRANSPORTES --------------------------
    
    def viewGestionTransportes(self):
        self.view.eliminarFramesSubmenu()
        gt.viewGT(self.view.submenu, self)
        
    def viewTransporteAsignar(self, id):
        self.view.eliminarFramesSubmenu()
        self.viewAsignar = gt.viewTransporteAsignar(self.view.submenu, self, id)
        
    def asignarTransporte(self):
        errores = list()
        
        transporteSelect = self.viewAsignar.transporte.get()
        
        if not transporteSelect:
            errores.append('Transporte Faltante')
            
        if len(errores) != 0:
            return self.viewAsignar.mostrarErrores(errores)
        
        transporte = self.transportesModel.findPedidoPorNombre(transporteSelect)
        transporte.printTransporte()
        
        now = datetime.now()
        fecha = now.date()
        
        id = self.viewAsignar.id
        
        self.pedidosModel.asignarTransporte(transporte.atributos['tra_id'], fecha, id)
        self.transportesModel.actualizarDisponibleTransporte(transporte.atributos['tra_id'], transporte.atributos['tra_disponible'])
        
        self.viewAsignar.mostrarMensajeConfirmacion()
    # ------------ VISTAS DE PEDIDOS --------------------------
    
    def viewGestionPedidos(self):
        self.view.eliminarFramesSubmenu()
        self.viewGP = gp.viewGP(self.view.submenu, self)
        
    def viewNewPedido(self):
        self.view.eliminarFramesSubmenu()
        self.formNew = gp.viewGPFormulario(self.view.submenu, self, 'registrar')
        
    def viewPedido(self, idpedido):
        self.view.eliminarFramesSubmenu()
        self.formNew = gp.viewGPFormulario(self.view.submenu, self, 'actualizar', idpedido)
    
    def viewTablaEntregar(self):
        self.view.eliminarFramesSubmenu()
        self.viewGP.viewTabla()
        
    def marcarPedidoEntregado(self, id):
        now = datetime.now()
        fechaentrega = now.date()
        
        self.pedidosModel.marcarEntregado(id, fechaentrega)
        
    def newPedido(self):
        errores = list()
        
        ciudad = self.formNew.CiudadEntry.get()
        estado = self.formNew.EstadoEntry.get()
        pais = self.formNew.PaisEntry.get()
        
        producto = self.formNew.Producto.get()
        
        cliente = self.formNew.ClienteEntry.get()
        
        if not ciudad:
            errores.append('Ciudad Faltante')
        if not estado:
            errores.append('Estado Faltante')
        if not pais:
            errores.append('Pais Faltante')
        if not producto:
            errores.append('Producto Faltante')
        if not cliente:
            errores.append('Cliente Faltante')
   
        
        if len(errores) != 0:
            return self.formNew.mostrarErrores(errores)
            
        Destino = f'{ciudad}, {estado}, {pais}' 
        idproducto = self.productosModel.findProductoPorNombre(producto).atributos['prod_id']
        costoTotal = self.formNew.sumaPrecios
        guia = self.formNew.guia

        pedido = pedidos.pedidosModel(None, Destino, idproducto, None, costoTotal, cliente, None, 0, None, guia)
        pedido.insertarDatos()
        self.formNew.mostrarMensajeConfirmacion()
    
    def actualizarPedido(self, id):
        pedido = self.pedidosModel.findPedidoPorId(id)
       
        errores = list()
        
        ciudad = self.formNew.CiudadEntry.get()
        estado = self.formNew.EstadoEntry.get()
        pais = self.formNew.PaisEntry.get()
        
        producto = self.formNew.Producto.get()
        
        cliente = self.formNew.ClienteEntry.get()
        
        if not ciudad:
            errores.append('Ciudad Faltante')
        if not estado:
            errores.append('Estado Faltante')
        if not pais:
            errores.append('Pais Faltante')
        if not producto:
            errores.append('Producto Faltante')
        if not cliente:
            errores.append('Cliente Faltante')
   
        
        if len(errores) != 0:
            return self.formNew.mostrarErrores(errores)
            
        Destino = f'{ciudad}, {estado}, {pais}' 
        idproducto = self.productosModel.findProductoPorNombre(producto).atributos['prod_id']
        costoTotal = self.formNew.sumaPrecios
        
        pedido.setDatosEspecificos(Destino, idproducto, costoTotal, cliente)
        pedido.actualizarDatos()
        self.formNew.mostrarMensajeConfirmacion()
        
    # ------------ VISTAS DE ALMACENES --------------------------
        
    def viewGestionAlmacenes(self):
        self.view.eliminarFramesSubmenu()
        ga.viewGA(self.view.submenu, self)
        
    # ------------ VISTAS DE REPORTES --------------------------
    
    def viewAnalisisReportes(self):
        self.view.eliminarFramesSubmenu()
        ar.viewAR(self.view.submenu, self)
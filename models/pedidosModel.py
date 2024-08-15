from includes import database

class pedidosModel:
    
    tabla_db = 'pedidos'
    columnas_db = 'ped_destino', 'ped_prod_id', 'ped_tra_id', 'ped_costo_total', 'ped_cliente', 'ped_salida', 'ped_entregado', 'ped_entrega', 'ped_guia'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, 
                 id=None, 
                 destino=None, 
                 idproducto=None, 
                 idtransporte=None, 
                 costototal=None, 
                 cliente=None, 
                 fechasalida=None, 
                 entregado=None, 
                 fechaentrega=None, 
                 numguia=None
                ):
        self.atributos = {
            'ped_id': id,
            'ped_destino': destino,
            'ped_prod_id': idproducto,
            'ped_tra_id': idtransporte,
            'ped_costo_total': costototal,
            'ped_cliente': cliente,
            'ped_salida': fechasalida,
            'ped_entregado': entregado,
            'ped_entrega': fechaentrega,
            'ped_guia': numguia,
        }
        
    def setDatosEspecificos(self, destino, idproducto, costototal, cliente):
        self.atributos['ped_destino'] = destino
        self.atributos['ped_prod_id'] = idproducto
        self.atributos['ped_costo_total'] = costototal
        self.atributos['ped_cliente'] = cliente
        
    def printPedido(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        
    def insertarDatos(self):
        query = 'INSERT INTO pedidos (ped_destino,ped_prod_id,ped_costo_total,ped_cliente,ped_entregado,ped_guia) VALUES ('
        query += f"'{self.atributos['ped_destino']}',"
        query += f"{self.atributos['ped_prod_id']},"
        query += f"{self.atributos['ped_costo_total']},"
        query += f"'{self.atributos['ped_cliente']}',"
        query += f"{0},"
        query += f"'{self.atributos['ped_guia']}')"
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
    
    def actualizarDatos(self):
        query = f'UPDATE {self.tabla_db} SET '
        query += f"ped_destino = '{self.atributos['ped_destino']}',"
        query += f"ped_prod_id = {self.atributos['ped_prod_id']},"
        query += f"ped_costo_total = {self.atributos['ped_costo_total']},"
        query += f"ped_cliente = '{self.atributos['ped_cliente']}' "
        query += f"WHERE ped_id = {self.atributos['ped_id']}"
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
        
    def asignarTransporte(self, idtransporte, fechasalida, id):
        query = f'UPDATE {self.tabla_db} SET '
        query += f"ped_tra_id = {idtransporte},"
        query += f"ped_salida = '{fechasalida}' "
        query += f"WHERE ped_id = {id}"
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
        
    def marcarEntregado(self, id, fechaentrega):
        query = f'UPDATE {self.tabla_db} SET '
        query += f"ped_entregado = 1,"
        query += f"ped_entrega = '{fechaentrega}' "
        query += f"WHERE ped_id = {id}"
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
        
    def allPedidoswithAlamacen(self):
        query = 'SELECT pedidos.*, alm_nombre, alm_ciudad, alm_estado FROM pedidos INNER JOIN productos ON ped_prod_id = prod_id INNER JOIN almacenes ON prod_alm_id = alm_id'
        self.cursor.execute(query)
        allPedidos = self.cursor.fetchall()
        return allPedidos
        
    def allPedidoswithAlamacenEntregados(self, condicion):
        query = f'SELECT pedidos.*, alm_nombre, alm_ciudad, alm_estado FROM pedidos INNER JOIN productos ON ped_prod_id = prod_id INNER JOIN almacenes ON prod_alm_id = alm_id WHERE ped_entregado = {condicion}'
        self.cursor.execute(query)
        allPedidos = self.cursor.fetchall()
        return allPedidos
    
    def findPedidoPorId(self, id):
        query = f'SELECT * FROM pedidos WHERE ped_id = {id}'
        pedido = self.consultaSQL(query)
        return pedido
    
    def allPedidos(self):
        query = 'SELECT * FROM pedidos'
        
        allPedidos = self.consultaSQL(query)
        
        for pedido in allPedidos:
            pedido.printPedido()
        
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                pedido = pedidosModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6],
                                        registro[7],
                                        registro[8],
                                        registro[9]
                                        )
                registros.append(pedido)
            
            return registros
        else:
            registro = resultado[0]
            pedido = pedidosModel(registro[0],
                                    registro[1],
                                    registro[2],
                                    registro[3],
                                    registro[4],
                                    registro[5],
                                    registro[6],
                                    registro[7],
                                    registro[8],
                                    registro[9]
                                    )
            return pedido
        
            
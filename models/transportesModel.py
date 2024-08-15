from includes import database

class transporteModel:
    
    tabla_db = 'transportes'
    columnas_db = 'tra_nombre', 'tra_cantidad', 'tra_disponible', 'tra_costo', 'tra_tipo'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, nombre=None, cantidad=None, disponible=None, costo=None, tipo=None):
        self.atributos = {'tra_id': id,
                          'tra_nombre': nombre,
                          'tra_cantidad': cantidad,
                          'tra_disponible': disponible,
                          'tra_costo': costo,
                          'tra_tipo': tipo
                         }
        
    def printTransporte(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        
    def actualizarDisponibleTransporte(self, id, disponibleActual):
        query = f'UPDATE {self.tabla_db} SET '
        query += f"tra_disponible = {disponibleActual+1} "
        query += f"WHERE tra_id = {id}"
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
        
    def findPedidoPorNombre(self, nombre):
        query = f"SELECT * FROM transportes WHERE tra_nombre = '{nombre}'"
        transporte = self.consultaSQL(query)
        return transporte
    
    def someTransportes(self, limit):
        query = f'SELECT * FROM {self.tabla_db} LIMIT {limit}'
        transportes = self.consultaSQL(query)
        
        return transportes
    
    def allTransportes(self):
        query = f'SELECT * FROM {self.tabla_db}'
        transportes = self.consultaSQL(query)
        
        return transportes
    
    def transportesPorAsignar(self):
        query = 'SELECT prov_nombre, prod_nombre, prod_caducidad, ped_destino, ped_id FROM proveedores ' + 'INNER JOIN productos ON prov_id = prod_prov_id ' + 'INNER JOIN pedidos ON prod_id = ped_prod_id ' + 'WHERE pedidos.ped_tra_id IS NULL'
        
        self.cursor.execute(query)
        
        resultados = self.cursor.fetchall()
        
        return resultados
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                transporte = transporteModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5]
                                        )
                registros.append(transporte)
            return registros
        else:
            registro = resultado[0]
            transporte = transporteModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5]
                                        )
            registros.append(transporte)
            return transporte
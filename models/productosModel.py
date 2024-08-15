from includes import database

class productosModel:
    
    tabla_db = 'productos'
    columnas_db = 'prod_nombre', 'prod_costo', 'prod_peso', 'prod_cantidad', 'prod_caducidad', 'prod_alm_id', 'prod_prov_id'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, 
                        nombre=None,
                        costo=None,
                        peso=None,
                        cantidad=None,
                        caducidad=None,
                        idAlmacen=None,
                        idProveedor=None
                ):
        self.atributos = {
            'prod_id': id,
            'prod_nombre': nombre,
            'prod_costo': costo,
            'prod_peso': peso,
            'prod_cantidad': cantidad,
            'prod_caducidad': caducidad,
            'prod_alm_id': idAlmacen,
            'prod_prov_id': idProveedor
        }
    
    def printProducto(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        return
    
    def findProductoPorNombre(self, nombre):
        query = f"SELECT * FROM productos WHERE prod_nombre = '{nombre}'"
        
        producto = self.consultaSQL(query)
        if producto:
            return producto
        else:
            return False
        
    def findProductoPorId(self, id):
        query = f"SELECT * FROM productos WHERE prod_id = '{id}'"
        
        producto = self.consultaSQL(query)
        if producto:
            return producto
        else:
            return False
        
    def allProductosMasVendidos(self):
        query = 'SELECT productos.* FROM pedidos INNER JOIN productos ON ped_prod_id = prod_id GROUP BY prod_id ORDER BY prod_id ASC, prod_costo DESC LIMIT 4'
        allProductos = self.consultaSQL(query)
        
        return allProductos
        
    def allProductos(self):
        query = 'SELECT * FROM productos'
        
        allProductos = self.consultaSQL(query)
        
        return allProductos
        
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                producto = productosModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6],
                                        registro[7]
                                        )
                registros.append(producto)
            return registros
        else:
            registro = resultado[0]
            producto = productosModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6],
                                        registro[7]
                                        )
            return producto
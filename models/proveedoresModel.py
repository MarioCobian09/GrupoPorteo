from includes import database

class proveedoresModel:
    
    tabla_db = 'proveedores'
    columnas_db = 'prov_nombre', 'prov_correo', 'prov_telefono', 'prov_direccion'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, nombre=None, correo=None, telefono=None, direccion=None):
        self.atributos = {
            'prov_id': id,
            'prov_nombre': nombre,
            'prov_correo': correo,
            'prov_telefono': telefono,
            'prov_direccion': direccion,
        }
    
    def printProveedor(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        return
    
    def insertarDatos(self):
        query = f"INSERT INTO {self.tabla_db} ("
        query += ",".join(self.columnas_db)
        query += ") VALUES ("
        for columna in self.columnas_db:
            if self.columnas_db[-1] == columna:
                query += f"'{self.atributos[columna]}') "
            else:
                query += f"'{self.atributos[columna]}', "
        self.cursor.execute(query)
        self.db.commit() # Lo hace efectivo
        
    def allProveedores(self):
        query = 'SELECT * FROM proveedores'
        
        allProveedores = self.consultaSQL(query)
        
        return allProveedores
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                proveedor = proveedoresModel(registro[0],
                                            registro[1],
                                            registro[2],
                                            registro[3],
                                            registro[4]
                                            )
                registros.append(proveedor)
            return registros
        else:
            registro = resultado[0]
            proveedor = proveedoresModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4]
                                        )
            return proveedor
       
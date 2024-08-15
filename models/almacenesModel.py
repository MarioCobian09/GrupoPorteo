from includes import database

class almacenesModel:
    tabla_db = 'almacenes'
    columnas_db = 'alm_nombre', 'alm_ciudad', 'alm_estado', 'alm_pais', 'alm_capacidad_total', 'alm_capacidad_actual', 'alm_costo'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None,
                    nombre=None,
                    ciudad=None,
                    estado=None,
                    pais=None,
                    capacidadtotal=None,
                    capacidadactual=None,
                    costo=None
                ):
        self.atributos = {
            'alm_id': id,
            'alm_nombre': nombre,
            'alm_ciudad': ciudad,
            'alm_estado': estado,
            'alm_pais': pais,
            'alm_capacidad_total': capacidadtotal,
            'alm_capacidad_actual': capacidadactual,
            'alm_costo': costo,
        }
    
    def printAlmacen(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        
    def findAlmacenPorID(self, id):
        query = f'SELECT * FROM Almacenes WHERE alm_id = {id}'
        almacen = self.consultaSQL(query)
        return almacen
    
    def allAlmacenes(self):
        query = 'SELECT * FROM Almacenes'
        allAlmacenes = self.consultaSQL(query)
        
        return allAlmacenes

        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()
        
        if len(resultado) > 1:
            for registro in resultado:
                almacen = almacenesModel(registro[0],
                                    registro[1],
                                    registro[2],
                                    registro[3],
                                    registro[4],
                                    registro[5],
                                    registro[6],
                                    registro[7]
                                    )
                registros.append(almacen)
            return registros
        else:
            registro = resultado[0]
            almacen = almacenesModel(registro[0],
                                    registro[1],
                                    registro[2],
                                    registro[3],
                                    registro[4],
                                    registro[5],
                                    registro[6],
                                    registro[7]
                                    )
            return almacen
       
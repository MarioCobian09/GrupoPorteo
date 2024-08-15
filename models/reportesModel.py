from includes import database

class reportesModel:
    
    tabla_db = 'reportes'
    columnas_db = 'rep_asunto', 'rep_descripcion', 'rep_telefono', 'rep_correo', 'rep_estado', 'rep_ped_id'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, asunto=None, descripcion=None, telefono=None, correo=None, estado=None, idPedido=None):
        self.atributos = {
            'rep_id': id,
            'rep_asunto': asunto,
            'rep_descripcion': descripcion,
            'rep_telefono': telefono,
            'rep_correo': correo,
            'rep_estado': estado,
            'rep_ped_id': idPedido,
        }
    
    def printReporte(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        return
        
    def allReportes(self):
        query = 'SELECT * FROM reportes'
        
        allReportes = self.consultaSQL(query)
        
        return allReportes
        
    def someReportes(self, limit):
        query = f'SELECT * FROM reportes LIMIT {limit}'
        
        allReportes = self.consultaSQL(query)
        
        return allReportes
        
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                reporte = reportesModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6]
                                        )
                registros.append(reporte)
            return registros
        else:
            registro = resultado[0]
            reporte = reportesModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6]
                                        )
            return reporte
       
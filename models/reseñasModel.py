from includes import database

class reseñasModel:
    
    tabla_db = 'reseñas'
    columnas_db = 'res_cliente', 'res_comentario', 'res_fecha'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, cliente=None, comentario=None, fecha=None):
        self.atributos = {
            'res_id': id,
            'res_cliente': cliente,
            'res_comentario': comentario,
            'res_fecha': fecha,
        }
    
    def printReseña(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        return
        
    def allReseñas(self):
        query = f'SELECT * FROM {self.tabla_db}'
        
        allReseñas = self.consultaSQL(query)
        
        return allReseñas
        
    def someReseñas(self, limit):
        query = f'SELECT * FROM {self.tabla_db} LIMIT {limit}'
        
        allReseñas = self.consultaSQL(query)
        
        return allReseñas
        
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                reseña = reseñasModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3]
                                        )
                registros.append(reseña)
            return registros
        else:
            registro = resultado[0]
            reseña = reseñasModel(registro[0],
                                    registro[1],
                                    registro[2],
                                    registro[3]
                                    )
            return reseña
       
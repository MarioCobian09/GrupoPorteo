from includes import database

class quejasysugerenciasModel:
    
    tabla_db = 'quejasysugerencias'
    columnas_db = 'que_cliente', 'que_fecha', 'que_asunto', 'que_mensaje'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, cliente=None, fecha=None, asunto=None, mensaje=None):
        self.atributos = {
            'que_id': id,
            'que_cliente': cliente,
            'que_fecha': fecha,
            'que_asunto': asunto,
            'que_mensaje': mensaje
        }
    
    def printQueja(self):
        for atributo, valor in self.atributos.items():
            print(f'{atributo}-> {valor}')
        print('\n')
        return
        
    def allQuejas(self):
        query = f'SELECT * FROM {self.tabla_db}'
        
        allQueja = self.consultaSQL(query)
        
        return allQueja
        
    def someQuejas(self, limit):
        query = f'SELECT * FROM {self.tabla_db} LIMIT {limit}'
        
        allQueja = self.consultaSQL(query)
        
        return allQueja
        
        
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                queja = quejasysugerenciasModel(registro[0],
                                                registro[1],
                                                registro[2],
                                                registro[3],
                                                registro[4]
                                                )
                registros.append(queja)
            return registros
        else:
            registro = resultado[0]
            queja = quejasysugerenciasModel(registro[0],
                                            registro[1],
                                            registro[2],
                                            registro[3],
                                            registro[4]
                                            )
            return queja
       
from includes import database

class usuariosModel:
    
    tabla_db = 'usuarios'
    columnas_db = 'usu_nombre', 'usu_ap_paterno', 'usu_ap_materno', 'usu_correo', 'usu_telefono', 'usu_password', 'usu_puesto', 'usu_img', 'usu_mantenersesion'
    
    db = database.conexion_db()
    cursor = db.cursor()
    
    def __init__(self, id=None, nombre=None, ap_paterno=None, ap_materno=None, correo=None, telefono=None, password=None, puesto=None, img=None):
        self.atributos = {
            'usu_id': id,
            'usu_nombre': nombre,
            'usu_ap_paterno': ap_paterno,
            'usu_ap_materno': ap_materno,
            'usu_correo': correo,
            'usu_telefono': telefono,
            'usu_password': password,
            'usu_puesto': puesto,
            'usu_img': img,
            'usu_mantenersesion': 0,
        }
        
    def getNombre(self):
        return f"{self.atributos['usu_nombre']} {self.atributos['usu_ap_paterno']}"
        
    def getPuesto(self):
        return f"{self.atributos['usu_puesto']}"
    
    def getImg(self):
        return f"{self.atributos['usu_img']}"

        
    def setDatos(self, usuario):
        i = 0
        for atributo in self.atributos:
            self.atributos[atributo] = usuario[i]
            i += 1
        
    def mostrarDatos(self):
        for key, value in self.atributos.items():
            print(f"{key} -> {value}")
        print('\n')
    
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
        print(query)
        
    def obtenerDepartamentos(self):
        query = "SELECT SUBSTRING(COLUMN_TYPE,6) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA='grupoporteo_db' AND TABLE_NAME='usuarios' AND COLUMN_NAME='usu_puesto'"
        self.cursor.execute(query)
        resultado = self.cursor.fetchone()
        resultado = resultado[0].split(')')
        resultado = resultado[0].split(',')
        
        listaDepartamentos = list()
        
        for r in resultado:
            palabra = r.replace('"', '', 1)
            palabra = palabra.replace("'", '', 1)
            palabra = palabra.replace("'", '', 1)
            listaDepartamentos.append(palabra)
        listaDepartamentos.pop(0)
        
        return listaDepartamentos
    
    def buscarPorCorreo(self, correo):
        query = f"SELECT * FROM {self.tabla_db} WHERE usu_correo = '{correo}' "
        self.cursor.execute(query)
        resultado = self.cursor.fetchone()
        
        if not resultado:
            return False
        return resultado
    
    def comprobarPassword(self, password):
        if self.atributos['usu_password'] == password:
            return True
        else:
            return False
        
    def mantenerSesion(self, id, valor):
        query = f"UPDATE {self.tabla_db} SET usu_mantenersesion = {valor} WHERE usu_id = {id}"
        self.cursor.execute(query)
        self.db.commit()
    
    def buscarPorSesion(self):
        query = f"SELECT * FROM {self.tabla_db} WHERE usu_mantenersesion = 1 "
        self.cursor.execute(query)
        resultado = self.cursor.fetchone()
        
        if not resultado:
            return False
        
        return resultado
    
    def allUsuarios(self):
        query = f'SELECT * FROM {self.tabla_db}'
        
        allUsuarios = self.consultaSQL(query)
        
        return allUsuarios
    
    def consultaSQL(self, query):
        
        registros = list()
                
        self.cursor.execute(query)
        
        resultado = self.cursor.fetchall()

        if len(resultado) > 1:
            for registro in resultado:
                usuario = usuariosModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6],
                                        registro[7],
                                        registro[8]
                                        )
                registros.append(usuario)
            return registros
        else:
            registro = resultado[0]
            usuario = usuariosModel(registro[0],
                                        registro[1],
                                        registro[2],
                                        registro[3],
                                        registro[4],
                                        registro[5],
                                        registro[6],
                                        registro[7],
                                        registro[8]
                                        )
            return usuario
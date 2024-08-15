import mysql.connector

def conexion_db():
    
    try:
        conexion = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='spartan1177',
                                            database='grupoporteo_db'
                                            )
        return conexion
    except mysql.connector.Error as e:
        print(f"No se pudo conectar: {e}")
        return conexion
        
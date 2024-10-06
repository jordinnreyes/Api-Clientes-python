import time
import mysql.connector
from mysql.connector import Error

def create_db_and_table():
    while True:
        try:
            conn = mysql.connector.connect(
                host="mysql",  
                user="root",
                password="1234",
                port=3306
            )
            if conn.is_connected():
                print("Conectado a MySQL")
                break
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            print("Reintentando en 5 segundos...")
            time.sleep(5)  

    cursor = conn.cursor()

    # Crear base de datos
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventory")
    
    # Seleccionar la base de datos creada
    conn.database = "inventory"
    
    # Crear tabla dentro de la base de datos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(50) NOT NULL,
            apellido VARCHAR(50) NOT NULL,
            edad INT NOT NULL,
            numero VARCHAR(15),
            correo VARCHAR(100)
        )
    """)
    
    conn.commit()
    cursor.close()  # Cerrar cursor
    conn.close()    # Cerrar conexión
    print("Base de datos y tabla creadas correctamente")

# Llama a la función
create_db_and_table()

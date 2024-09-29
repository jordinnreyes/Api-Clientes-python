import mysql.connector

def create_db_and_table():
    conn = mysql.connector.connect(
        host="mysql",  # Cambia esto si estás usando Docker (puede ser 'mysql')
        user="root",       # Cambia por tu usuario MySQL
        password="1234", # Cambia por tu contraseña MySQL
    )
    
    cursor = conn.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventory")
    
    # Seleccionar la base de datos
    conn.database = "inventory"
    
    # Crear la tabla clientes si no existe
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
    conn.close()

if __name__ == '__main__':
    create_db_and_table()

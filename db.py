import time
import mysql.connector
from mysql.connector import Error

def create_db_and_table():
    while True:
        try:
            conn = mysql.connector.connect(
                host="mysql",  # Mantén 'mysql' ya que coincide con el nombre del servicio en docker-compose
                user="root",
                password="1234",
                database='inventory'
            )
            if conn.is_connected():
                print("Conectado a MySQL")
                break
        except Error as e:
            print(f"Error al conectar con MySQL: {e}")
            print("Reintentando en 5 segundos...")
            time.sleep(5)  # Esperar 5 segundos antes de volver a intentar

    cursor = conn.cursor()
    
    # Crear base de datos y tabla
    cursor.execute("CREATE DATABASE IF NOT EXISTS inventory")
    conn.database = "inventory"
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

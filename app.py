from flask import Flask, request,jsonify, render_template
import  json
import mysql.connector
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Permite CORS para todos los orígenes


def get_db_connection():
    conn = mysql.connector.connect(
        host="mysql",  # Puede ser 'localhost' o la IP de tu servidor mysql
        user="root",
        password="1234",
        database="inventory",
        port=3306
    )
    return conn



# GET /clientes
@app.route('/clientes', methods=['GET'])
def get_all_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    
    return jsonify(clientes)

# GET /clientes/{id}
@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def get_cliente(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
    cliente = cursor.fetchone()
    conn.close()
    
    if cliente:
        return jsonify(cliente)
    else:
        return jsonify({'message': 'Cliente no encontrado'}), 404

# POST /clientes
@app.route('/clientes', methods=['POST'])
def create_cliente():
    new_cliente = request.get_json()
    nombre = new_cliente['nombre']
    apellido = new_cliente['apellido']
    edad = new_cliente['edad']
    numero = new_cliente.get('numero')
    correo = new_cliente.get('correo')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, apellido, edad, numero, correo) VALUES (%s, %s, %s, %s, %s)",
                   (nombre, apellido, edad, numero, correo))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Cliente creado correctamente'}), 201

# PUT /clientes/{id}
@app.route('/clientes/<int:id_cliente>', methods=['PUT'])
def update_cliente(id_cliente):
    update_data = request.get_json()
    nombre = update_data.get('nombre')
    apellido = update_data.get('apellido')
    edad = update_data.get('edad')
    numero = update_data.get('numero')
    correo = update_data.get('correo')
    
    conn = get_db_connection()
    cursor = conn.cursor()


    # Actualiza solo los campos que han sido proporcionados en la solicitud
    cursor.execute("""
        UPDATE clientes
        SET nombre = %s, apellido = %s, edad = %s, numero = %s, correo = %s
        WHERE id_cliente = %s
    """, (nombre, apellido, edad, numero, correo, id_cliente))
    
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    else:
        return jsonify({'message': 'Cliente actualizado correctamente'})


# DELETE /clientes/{id_cliente}
@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def delete_cliente(id_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Cliente no encontrado'}), 404
    else:
        return jsonify({'message': 'Cliente eliminado correctamente'})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)

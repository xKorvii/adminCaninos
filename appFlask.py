from flask import Flask, jsonify, request
import mysql.connector
import re

app = Flask(__name__)

# Configuración de la conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'c03ly!Or53$P',
    'database': 'caninos'
}

#---------------------------------------Dueño---------------------------------------

#Visualizar Tabla Dueño
@app.route('/dueno', methods=['GET'])
def get_dueno():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM dueno")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify(results)

#Insertar Tabla Dueño
@app.route('/dueno', methods=['POST'])
def insertar_dueno():
    data = request.get_json()
    telefono = data.get('TELEFONO')

    #Validar que el teléfono sea un número de 9 dígitos
    if not re.match(r'^\d{9}$', telefono):
        return jsonify({'error': 'El teléfono debe ser un número de 9 dígitos'}), 400

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "INSERT INTO dueno (NOMBRE, APELLIDO, TELEFONO) VALUES (%s, %s, %s)"
        values = (data['NOMBRE'], data['APELLIDO'], telefono)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro creado exitosamente'}), 201

#Actualizar Tabla Dueño
@app.route('/dueno/<int:id>', methods=['PUT'])
def actualizar_dueno(id):
    data = request.get_json()
    telefono = data.get('TELEFONO')

    #Validar que el teléfono sea un número de 9 dígitos
    if not re.match(r'^\d{9}$', telefono):
        return jsonify({'error': 'El teléfono debe ser un número de 9 dígitos'}), 400

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "UPDATE dueno SET NOMBRE = %s, APELLIDO = %s, TELEFONO = %s WHERE ID_DUENO = %s"
        values = (data['NOMBRE'], data['APELLIDO'], telefono, id)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro actualizado exitosamente'}), 200

#Eliminar Tabla Dueño
@app.route('/dueno/<int:id>', methods=['DELETE'])
def eliminar_dueno(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "DELETE FROM dueno WHERE ID_DUENO = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro eliminado exitosamente'}), 200

#---------------------------------------Perro---------------------------------------

#Visualizar Tabla Perro
@app.route('/perro', methods=['GET'])
def get_perro():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM perro")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify(results)

#Insertar Tabla Perro
@app.route('/perro', methods=['POST'])
def insertar_perro():
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "INSERT INTO perro (NOMBRE, RAZA, EDAD, PESO, ID_DUENO) VALUES (%s, %s, %s, %s, %s)"
        values = (data['NOMBRE'], data['RAZA'], data['EDAD'], data['PESO'], data['ID_DUENO'])
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro creado exitosamente'}), 201

#Actualizar Tabla Perro
@app.route('/perro/<int:id>', methods=['PUT'])
def actualizar_perro(id):
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "UPDATE perro SET NOMBRE = %s, RAZA = %s, EDAD = %s, PESO = %s, ID_DUENO = %s WHERE ID_PERRO = %s"
        values = (data['NOMBRE'], data['RAZA'], data['EDAD'], data['PESO'], data['ID_DUENO'], id)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro actualizado exitosamente'}), 200

#Eliminar Tabla Perro
@app.route('/perro/<int:id>', methods=['DELETE'])
def eliminar_perro(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "DELETE FROM perro WHERE ID_PERRO = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro eliminado exitosamente'}), 200

#---------------------------------------Servicio---------------------------------------

#Visualizar Tabla Servicio
@app.route('/servicio', methods=['GET'])
def get_servicio():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM servicio")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify(results)

#Insertar Tabla Servicio
@app.route('/servicio', methods=['POST'])
def insertar_servicio():
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "INSERT INTO servicio (ID_SERVICIO, NOMBRE, PRECIO, DESCRIPCION) VALUES (%s, %s, %s, %s)"
        values = (data['ID_SERVICIO'], data['NOMBRE'], data['PRECIO'], data['DESCRIPCION'])
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro creado exitosamente'}), 201

#Actualizar Tabla Servicio
@app.route('/servicio/<int:id>', methods=['PUT'])
def actualizar_servicio(id):
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "UPDATE servicio SET ID_SERVICIO = %s, NOMBRE = %s, PRECIO = %s, DESCRIPCION = %s WHERE ID_SERVICIO = %s"
        values = (data['ID_SERVICIO'], data['NOMBRE'], data['PRECIO'], data['DESCRIPCION'], id)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro actualizado exitosamente'}), 200

#Eliminar Tabla Servicio
@app.route('/servicio/<int:id>', methods=['DELETE'])
def eliminar_servicio(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "DELETE FROM servicio WHERE ID_SERVICIO = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro eliminado exitosamente'}), 200

#---------------------------------------Cita---------------------------------------

#Visualizar Tabla Cita
@app.route('/cita', methods=['GET'])
def get_cita():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cita")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify(results)

#Insertar Tabla Cita
@app.route('/cita', methods=['POST'])
def insertar_cita():
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "INSERT INTO cita (FECHA, ESTADO, ID_PERRO, ID_SERVICIO) VALUES (%s, %s, %s, %s)"
        values = (data['FECHA'], data['ESTADO'], data['ID_PERRO'], data['ID_SERVICIO'])
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro creado exitosamente'}), 201

#Actualizar Tabla Cita
@app.route('/cita/<int:id>', methods=['PUT'])
def actualizar_cita(id):
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "UPDATE cita SET FECHA = %s, ESTADO = %s, ID_PERRO = %s, ID_SERVICIO = %s WHERE ID_CITA = %s"
        values = (data['FECHA'], data['ESTADO'], data['ID_PERRO'], data['ID_SERVICIO'], id)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro actualizado exitosamente'}), 200

#Eliminar Tabla Cita
@app.route('/cita/<int:id>', methods=['DELETE'])
def eliminar_cita(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "DELETE FROM cita WHERE ID_CITA = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro eliminado exitosamente'}), 200

#---------------------------------------Historial De Salud---------------------------------------

#Visualizar Tabla Historial de Salud
@app.route('/historial', methods=['GET'])
def get_historial():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM historial_de_salud")
        results = cursor.fetchall()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify(results)

#Insertar Tabla Historial de Salud
@app.route('/historial', methods=['POST'])
def insertar_historial():
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "INSERT INTO historial_de_salud (FECHA, DESCRIPCION, ID_PERRO) VALUES (%s, %s, %s)"
        values = (data['FECHA'], data['DESCRIPCION'], data['ID_PERRO'])
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro creado exitosamente'}), 201

#Actualizar Tabla Historial de Salud
@app.route('/historial/<int:id>', methods=['PUT'])
def actualizar_historial(id):
    data = request.get_json()
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "UPDATE historial_de_salud SET FECHA = %s, DESCRIPCION = %s, ID_PERRO = %s WHERE ID_HISTORIAL = %s"
        values = (data['FECHA'], data['DESCRIPCION'], data['ID_PERRO'], id)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro actualizado exitosamente'}), 200

#Eliminar Tabla Historial de Salud
@app.route('/historial/<int:id>', methods=['DELETE'])
def eliminar_historial(id):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        sql = "DELETE FROM historial_de_salud WHERE ID_HISTORIAL = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500
    finally:
        cursor.close()
        connection.close()
    return jsonify({'message': 'Registro eliminado exitosamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)
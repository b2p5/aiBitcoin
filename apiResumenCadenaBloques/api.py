#
# API de Consulta de Transacciones de Blockchain
# 
# Esta API implementada con Flask proporciona un endpoint para obtener el total de transacciones entre dos alturas de bloque específicas en una blockchain.
# Se utiliza SQLite para la consulta a la base de datos.
# El script incluye también un endpoint para servir un archivo de política de privacidad.
#
# Endpoint principal: http://localhost:5000/transactions?start_height=821610&end_height=821624
#

from flask import Flask, jsonify, send_from_directory  # Importaciones de Flask y utilidades
import sqlite3  # Importación de SQLite para la gestión de la base de datos
import os  # Importación del módulo os para interactuar con el sistema de archivos

app = Flask(__name__)  # Creación de la instancia de la aplicación Flask

# Obtiene el resumen de la cadena de bloques entre dos alturas de bloque
def get_total_transactions(start_height, end_height):
    try:
        conn = sqlite3.connect('./BBDD/bcResumen.db')  # Conexión a la base de datos SQLite
        cursor = conn.cursor()  # Creación de un cursor para ejecutar consultas

        # Consulta SQL para obtener el total, mínimo y máximo de transacciones entre dos alturas de bloque
        query = '''
            SELECT SUM(nTx) as total, MIN(nTx) as min, MAX(nTx) as max
            FROM resumenBlock
            WHERE height BETWEEN ? AND ?
        '''
        cursor.execute(query, (start_height, end_height))  # Ejecución de la consulta
        row = cursor.fetchone()  # Recuperación del resultado

        # Verificación y retorno de los resultados de la consulta
        if row:
            return {"total_transactions": row[0], "min_transaction": row[1], "max_transaction": row[2]}
        else:
            return {"total_transactions": 0, "min_transaction": 0, "max_transaction": 0}
    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")  # Manejo de errores de la base de datos
        return None
    finally:
        conn.close()  # Cierre de la conexión a la base de datos

# Llamada a la ruta transactions con parámetros start_height y end_height
@app.route('/transactions', methods=['GET'])
def transactions():
    # Obtención de parámetros 'start_height' y 'end_height' de la solicitud GET
    start_height = request.args.get('start_height', type=int)
    end_height = request.args.get('end_height', type=int)

    # Validación de los parámetros
    if start_height is None or end_height is None:
        return jsonify({"error": "Se requieren start_height y end_height"}), 400

    result = get_total_transactions(start_height, end_height)  # Obtención del resultado de la consulta
    if result is not None:
        return jsonify(result)  # Devolución de los resultados como JSON
    else:
        return jsonify({"error": "Error al procesar la solicitud"}), 500  # Manejo de errores

# Llamada a la ruta privacy_policy
@app.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    try:
        # Servicio de un archivo de política de privacidad
        policy_file_name = 'PrivacyPolicy.html'
        if os.path.isfile(policy_file_name):
            return send_from_directory(directory='.', filename=policy_file_name)
        else:
            return jsonify({"error": "Archivo de política de privacidad no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al leer el archivo: {str(e)}"}), 500  # Manejo de excepciones

if __name__ == '__main__':
    app.run(debug=True)  # Inicio de la aplicación con modo de depuración activado



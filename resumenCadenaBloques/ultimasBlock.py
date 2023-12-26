#
# Script para Sincronizar y Almacenar Datos de Bloques de Bitcoin en SQLite: bcResumen.db
#
# Este script en Python se conecta a un nodo de Bitcoin Core mediante JSON-RPC y sincroniza los datos de bloques con una base de datos SQLite.
# Funcionalidades Principales:
# 1. Conexión con un nodo de Bitcoin Core usando JSON-RPC para acceso a datos de bloques.
# 2. Consulta a SQLite para determinar el último bloque registrado en la base de datos.
# 3. Extracción de información de bloques recientes desde el último bloque registrado hasta el más reciente en la blockchain.
# 4. Generación de comandos SQL para cada bloque extraído, incluyendo datos como altura, número de transacciones, tamaño, peso y tiempo.
# 5. Almacenamiento de comandos SQL en un archivo para posterior ejecución.
# 6. Ejecución de los comandos SQL generados para insertar los datos en la base de datos SQLite.
# 7. Seguimiento del progreso y manejo de errores durante el proceso de extracción y almacenamiento.
# 8. Registro del tiempo de inicio y finalización del script, junto con el tiempo total de ejecución.
#
# Nota: Este script es útil para mantener una base de datos local actualizada con los últimos datos de bloques de Bitcoin, facilitando análisis y consultas offline.
#

# 
# Para ejecutar el script, debes tener instalado Python 3 y el paquete
# python-bitcoinrpc. Para instalarlo, ejecuta:
# pip install python-bitcoinrpc
#######################################################################


from bitcoinrpc.authproxy import AuthServiceProxy
import time
import sqlite3
import os

def get_max_height():
    # Devuelve la altura del último bloque grabado en la base de datos.
    try:
        conn = sqlite3.connect('./BBDD/bcResumen.db')
        #conn = sqlite3.connect('/home/franAPI/apiBcResumen/BBDD/bcResumen.db')
        cursor = conn.cursor()

        query = '''
            SELECT MAX(height) as maxheight
            FROM resumenBlock
        '''
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            return row[0]
        else:
            return 999999999
        
    except sqlite3.Error as e:
        print(f"Error de base de datos: {e}")
        return None
    finally:
        conn.close()

# Función para conectarse al nodo Bitcoin Core vía JSON-RPC
def connect_rpc():
    """Conexión al nodo Bitcoin Core vía JSON-RPC."""
    rpc_user = 'userX'
    rpc_password = 'wsx'
    rpc_host = 'localhost'
    rpc_port = '8332'
    return AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

# Función para generar el comando SQL
def generar_comando_sql(block_data):
    return f"INSERT OR REPLACE INTO resumenBlock (height, nTx, size, weight, time) VALUES ({block_data['height']}, {block_data['nTx']}, {block_data['size']}, {block_data['weight']}, {block_data['time']});\n"

# Función para obtener los datos del bloque
def obtener_datos_bloque(block_number, rpc_client):
    # Devuelve un diccionario con los campos: height, nTx, size, weight, time.
    block_hash = rpc_client.getblockhash(block_number);
    block_data = rpc_client.getblock(block_hash);
    return block_data

# Función principal
def main():
    # Hora a la que comienza el script
    hora_inicio = time.time()
    print("Inicio del script " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(hora_inicio)))
    
    #Inicializa el nombre del archivo SQL y el buffer de comandos
    nombre_archivo_sql = "./sql2BBDD/ultimosBlock.sql"
    buffer_comandos = ""

    # Elimina el archivo nombre_archivo_sql si existe 
    try:
        with open(nombre_archivo_sql, "r") as file:
            pass
    except FileNotFoundError:
        pass
    else:
        print(f"Eliminando el archivo {nombre_archivo_sql}...")
        os.remove(nombre_archivo_sql)
        
    # Crea el fichero nombre_archivo_sql = ultimosBlock.sql
    with open(nombre_archivo_sql, "w") as file:
        file.write("")


    rpc_client = connect_rpc()

    # Obtén el número del último bloque
    best_block_height = rpc_client.getblockcount()

    # Obtén el número del último bloque grabado en la base de datos
    last_block_height = get_max_height() - 1

    #for height in range(best_block_height, 821613, -1):
    for block_number in range(best_block_height, last_block_height, -1):
        # Aquí deberías obtener los datos del bloque. Esto es solo un ejemplo.
        block_data = obtener_datos_bloque(block_number, rpc_client)

        # Generar y acumular el comando SQL
        buffer_comandos += generar_comando_sql(block_data)

        # Guardar cada 100 bloques
        if block_number % 10 == 0:
            with open(nombre_archivo_sql, "a") as file:
                file.write(buffer_comandos)
            buffer_comandos = ""
            ahora = time.time()
            print(f"Guardados los bloques {block_number} a {block_number-9} . A las {time.strftime('%H:%M:%S', time.localtime(ahora))}")

    # Guardar los comandos restantes si los hay
    if buffer_comandos:
        with open(nombre_archivo_sql, "a") as file:
            file.write(buffer_comandos)


    # Recorremos nombre_archivo_sql y vamos ejecutando los comandos SQL en la base de datos
    conn = sqlite3.connect('./BBDD/bcResumen.db')

    with open(nombre_archivo_sql, "r") as file:
        contador = 0
        for line in file:
            conn.execute(line)
            contador += 1
            if contador % 10 == 0:
                print(f"{contador} registros cargados.")
                conn.commit()
        conn.commit()
        file.close()    

    # Hora a la que termina el script
    hora_fin = time.time()
    print("Fin del script " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(hora_fin)))
    print(f"Tiempo de ejecución: {hora_fin - hora_inicio} segundos.")
    

if __name__ == "__main__":
    main()


#
# Script de Extracción de Datos de Bloques de Bitcoin y Generación de Comandos SQL
#
# Este script en Python se conecta a un nodo de Bitcoin Core mediante JSON-RPC para obtener información de los bloques de la blockchain de Bitcoin.
# Funcionalidades Principales:
# 1. Establece una conexión con un nodo de Bitcoin Core usando credenciales y dirección predefinidas.
# 2. Extrae datos de cada bloque, como altura, número de transacciones, tamaño, peso y tiempo de creación.
# 3. Genera comandos SQL para insertar estos datos en una base de datos, estructurando la información relevante de cada bloque.
# 4. Almacena estos comandos SQL en un archivo, agrupándolos para optimizar la escritura en la base de datos.
# 5. Incluye una advertencia para no ejecutar el script en un servidor de producción y que se debe usar solo una vez al iniciar la explotación.
# 6. Realiza un seguimiento del tiempo de ejecución del script, proporcionando actualizaciones periódicas del progreso.
#
# Nota: Este script está diseñado para ser utilizado en contextos donde se requiere un análisis detallado 
# y almacenamiento de la información de los bloques de Bitcoin, como parte de un sistema de monitoreo o análisis de datos.
#
# Para ejecutar el script, debes tener instalado Python 3 y el paquete
# python-bitcoinrpc. Para instalarlo, ejecuta:
# pip install python-bitcoinrpc


from bitcoinrpc.authproxy import AuthServiceProxy
import time

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




    #Avisar que este script no se debe ejecutar en el servidor de producción
    print("Este script no se debe ejecutar en el servidor de producción")
    print("Solamente se debe ejecutar una sola vez al comenzar la explotación.")
    #salir del script
    exit()






    # Hora a la que comienza el script
    hora_inicio = time.time()
    print("Inicio del script " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(hora_inicio)))
    
    nombre_archivo_sql = "./sql2BBDD/resumenBlock.sql"
    buffer_comandos = ""

    rpc_client = connect_rpc()

    # Obtén el número del último bloque
    best_block_height = rpc_client.getblockcount()

    #for height in range(best_block_height, 821613, -1):
    for block_number in range(best_block_height, 0, -1):
        # Aquí deberías obtener los datos del bloque. Esto es solo un ejemplo.
        block_data = obtener_datos_bloque(block_number, rpc_client)

        # Generar y acumular el comando SQL
        buffer_comandos += generar_comando_sql(block_data)

        # Guardar cada 100 bloques
        if block_number % 10000 == 0:
            with open(nombre_archivo_sql, "a") as file:
                file.write(buffer_comandos)
            buffer_comandos = ""
            ahora = time.time()
            print(f"Guardados los bloques {block_number} a {block_number-9999} . A las {time.strftime('%H:%M:%S', time.localtime(ahora))}")

    # Guardar los comandos restantes si los hay
    if buffer_comandos:
        with open(nombre_archivo_sql, "a") as file:
            file.write(buffer_comandos)



if __name__ == "__main__":
    main()

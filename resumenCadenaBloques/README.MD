# Resumen Cadena de Bloques

## Descripción
Este repositorio contiene dos scripts de Python diseñados para interactuar con la blockchain de Bitcoin. Estos scripts permiten extraer datos de bloques y sincronizarlos con una base de datos SQLite, proporcionando un medio eficiente para el análisis y monitoreo de la blockchain de Bitcoin.

## Scripts Incluidos

### 1. Script de Extracción de Datos de Bloques de Bitcoin y Generación de Comandos SQL
Este script se conecta a un nodo de Bitcoin Core mediante JSON-RPC para obtener información detallada de los bloques de la blockchain de Bitcoin y genera comandos SQL para su almacenamiento.

**Funcionalidades Principales:**
- Conexión con un nodo Bitcoin Core.
- Extracción de datos de bloques.
- Generación de comandos SQL.
- Almacenamiento de comandos SQL en un archivo.

### 2. Script para Sincronizar y Almacenar Datos de Bloques de Bitcoin en SQLite
Este script sincroniza los datos de bloques con una base de datos SQLite, manteniendo una copia local actualizada de la información de la blockchain.

**Funcionalidades Principales:**
- Conexión con un nodo Bitcoin Core.
- Sincronización con la última altura de bloque en la base de datos.
- Extracción y almacenamiento de información de bloques recientes.
- Ejecución de comandos SQL para la actualización de la base de datos.

## Requisitos
- Python 3
- Paquete python-bitcoinrpc
  - Instalación: `pip install python-bitcoinrpc`
- SQLite3

## Instalación y Ejecución
1. Clona el repositorio.
2. Instala las dependencias requeridas.
3. Ejecuta cada script individualmente según la necesidad:
   - `python script_extraccion_datos.py`
   - `python script_sincronizacion_sqlite.py`

## Uso
- Asegúrate de tener acceso a un nodo Bitcoin Core operativo.
- Configura las credenciales y el puerto para la conexión JSON-RPC en cada script.
- Ejecuta los scripts según las instrucciones detalladas en sus respectivos comentarios.

## Advertencias
- Estos scripts están diseñados para fines de desarrollo y análisis. No se recomienda su uso en un entorno de producción sin las debidas modificaciones y pruebas.
- Verifica siempre los permisos y la seguridad al conectarte a un nodo Bitcoin Core.

## Contribuciones
Las contribuciones al código y mejoras en la documentación son bienvenidas. Por favor, envía tus pull requests a la rama principal.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

---

Desarrollado con ❤️ por [b2p5]

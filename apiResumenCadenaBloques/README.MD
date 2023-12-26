# API Resumen Cadena de Bloques

## Descripción
La API "Resumen Cadena de Bloques" es una aplicación Flask diseñada para proporcionar información sobre transacciones preprocesadas de la blockchain de Bitcoin. Utiliza SQLite para la consulta de datos y ofrece endpoints para obtener resúmenes de transacciones y para servir un archivo de política de privacidad.

## Características
- **Consulta de Transacciones**: Permite a los usuarios obtener el total, mínimo y máximo de transacciones entre dos alturas de bloque específicas.
- **Política de Privacidad**: Incluye un endpoint para servir un archivo de política de privacidad.
- **Base de Datos SQLite**: Utiliza SQLite para almacenar y consultar los datos de la blockchain.

## Endpoints
- **Transacciones**
  - `GET /transactions?start_height=XXX&end_height=YYY`
  - Devuelve el total, el mínimo y el máximo de transacciones entre las alturas de bloque especificadas.
- **Política de Privacidad**
  - `GET /privacy_policy`
  - Sirve el archivo de política de privacidad si está disponible.

## Requisitos
- Flask
- SQLite3
- Python 3.x

## Instalación y Ejecución
1. Clonar el repositorio.
2. Instalar las dependencias: `pip install flask sqlite3`.
3. Ejecutar el script: `python api.py`.

## Uso
Para realizar una consulta de transacciones, envía una solicitud GET al endpoint `/transactions` con los parámetros `start_height` y `end_height`. Por ejemplo:



## Advertencias
- Este script está diseñado para usos educativos y de desarrollo; no se recomienda su uso en un entorno de producción.
- Asegúrate de tener la base de datos y el archivo de política de privacidad correctamente configurados antes de ejecutar la aplicación.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, envía tus pull requests a la rama principal.

## Licencia
[MIT](LICENSE)

---

Desarrollado con ❤️ por [b2p5]

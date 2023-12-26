#
# Programa de Extracción y Almacenamiento de Enlaces Web
#
# Este script en Python utiliza `requests` y `BeautifulSoup` para raspar enlaces web desde una URL específica, procesarlos y almacenarlos en una base de datos SQLite.
# Funcionalidades Principales:
# 1. Creación de una base de datos SQLite y una tabla para almacenar enlaces.
# 2. Extracción de enlaces de una página web dada, utilizando técnicas de web scraping.
# 3. Recursivamente, recopila enlaces hasta un nivel de profundidad definido.
# 4. Almacena los enlaces recopilados en la base de datos con información sobre su nivel de profundidad.
# 5. Está diseñado para trabajar específicamente con la URL 'https://academy.bit2me.com/' y extraer enlaces relacionados.
#
# Nota: Las secciones de código comentadas al final del script permiten visualizar los enlaces almacenados en la base de datos.
#


import requests
from bs4 import BeautifulSoup
import sqlite3

# Nombre de la base de datos
nombreBBDD = './BBDD/aiB2M.db'

# Función para crear la base de datos y la tabla si no existen
def crear_bd_y_tabla():
    conexion = sqlite3.connect(nombreBBDD)
    cursor = conexion.cursor()

    # Elimina la tabla si existe 
    # Crea la tabla enlacesB2M si no existe
    cursor.execute('''DROP TABLE IF EXISTS enlacesB2M''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS enlacesB2M
                      (id INTEGER PRIMARY KEY, url TEXT, nivel INTEGER)''')
    conexion.commit()
    conexion.close()

# Función para extraer los enlaces de una página
def extraer_enlaces(url):
    try:
        respuesta = requests.get(url, timeout=5)
        if respuesta.status_code != 200:
            return []
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        enlaces = set()
        for etiqueta in soup.find_all('a', href=True):
            enlace = etiqueta['href']
            if enlace.startswith(url) and len(enlace) > 33:
                enlaces.add(enlace)
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud a {url}: {e}")
        return []
    return list(enlaces)[:20]

# Función para obtener los enlaces de los niveles
def obtener_enlaces_niveles(url, niveles=3):
    enlaces_nivel = {0: [url]}
    for nivel in range(niveles):
        enlaces_nivel[nivel + 1] = []
        for enlace in enlaces_nivel[nivel]:
            enlaces_obtenidos = extraer_enlaces(enlace)
            enlaces_nivel[nivel + 1].extend(enlaces_obtenidos)
            enlaces_nivel[nivel + 1] = list(set(enlaces_nivel[nivel + 1]))
    return enlaces_nivel

# Función para guardar los enlaces en la base de datos
def guardar_en_bd(url, nivel):
    conexion = sqlite3.connect(nombreBBDD)
    cursor = conexion.cursor()
    cursor.execute("INSERT OR REPLACE INTO enlacesB2M (url, nivel) VALUES (?, ?)", (url, nivel))
    conexion.commit()
    conexion.close()

# Crear la base de datos y la tabla
crear_bd_y_tabla()

# Uso de la función
url = 'https://academy.bit2me.com/'
enlaces_por_nivel = obtener_enlaces_niveles(url)

# Guardar enlaces en la base de datos
for nivel, enlaces in enlaces_por_nivel.items():
    for enlace in enlaces:
        guardar_en_bd(enlace, nivel)


# # Recorremos la tabla enlacesB2M 
# conexion = sqlite3.connect(nombreBBDD)
# cursor = conexion.cursor()
# cursor.execute("SELECT * FROM enlacesB2M")
# enlaces = cursor.fetchall()
# # Bucle para mostrar los enlaces
# for enlace in enlaces:
#     print(enlace)
#     # 

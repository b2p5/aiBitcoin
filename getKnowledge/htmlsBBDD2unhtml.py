import sqlite3
import requests

# Nombre de la base de datos
nombreBBDD = './BBDD/aiB2M.db'

html_salida = "./paginas/todo.html"
# abrir el archivo html_salida en modo escritura 
f = open(html_salida, "w")
# borrar contenido que pueda tener el archivo html_salida
f.write("Compendio de webs de B2M")
f.write("<br>")


# Función para generar un solo archivo html 
def generar_html(url , f):
    # Descarga el contenido de la página
    respuesta = requests.get(url)
    # Si la descarga ha sido correcta se añade al archivo html html_salida
    if respuesta.status_code == 200:
        f.write(respuesta.text)
         
    return respuesta.text

# Recorremos la tabla enlacesB2M 
conexion = sqlite3.connect(nombreBBDD)
cursor = conexion.cursor()
cursor.execute("SELECT * FROM enlacesB2M ")
enlaces = cursor.fetchall()
# Bucle para mostrar los enlaces
for enlace in enlaces:
    print(enlace[1])

    resultado = generar_html(enlace[1], f)

    print(resultado)

    
